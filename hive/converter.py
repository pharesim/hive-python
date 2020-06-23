import math

from .amount import Amount
from .instance import shared_hived_instance


class Converter(object):
    """ Converter simplifies the handling of different metrics of
        the blockchain

        :param Hived hived_instance: Hived() instance to
        use when accessing a RPC

    """

    def __init__(self, hived_instance=None):
        self.hived = hived_instance or shared_hived_instance()

        self.CONTENT_CONSTANT = 2000000000000

    def hbd_median_price(self):
        """ Obtain the hbd price as derived from the median over all
            witness feeds. Return value will be HBD
        """
        return (Amount(self.hived.get_feed_history()['current_median_history']
                       ['base']).amount / Amount(self.hived.get_feed_history(
        )['current_median_history']['quote']).amount)

    def hive_per_mvests(self):
        """ Obtain HIVE/MVESTS ratio
        """
        info = self.hived.get_dynamic_global_properties()

        # temporarily allow both steem and hive symbols until after HF24
        if 'total_vesting_fund_steem' in info:
            info['total_vesting_fund_hive'] = info['total_vesting_fund_steem']

        return (Amount(info["total_vesting_fund_hive"]).amount /
                (Amount(info["total_vesting_shares"]).amount / 1e6))

    def vests_to_hp(self, vests):
        """ Obtain HP from VESTS (not MVESTS!)

            :param number vests: Vests to convert to HP
        """
        return vests / 1e6 * self.hive_per_mvests()

    def hp_to_vests(self, hp):
        """ Obtain VESTS (not MVESTS!) from HP

            :param number sp: HP to convert
        """
        return hp * 1e6 / self.hive_per_mvests()

    def hp_to_rshares(self, hp, voting_power=10000, vote_pct=10000):
        """ Obtain the r-shares

            :param number hp: Hive Power
            :param int voting_power: voting power (100% = 10000)
            :param int vote_pct: voting participation (100% = 10000)
        """
        # calculate our account voting shares (from vests), mine is 6.08b
        vesting_shares = int(self.hp_to_vests(hp) * 1e6)

        # get props
        props = self.hived.get_dynamic_global_properties()

        # determine voting power used
        used_power = int((voting_power * vote_pct) / 10000);
        max_vote_denom = props['vote_power_reserve_rate'] * (5 * 60 * 60 * 24) / (60 * 60 * 24);
        used_power = int((used_power + max_vote_denom - 1) / max_vote_denom)

        # calculate vote rshares
        rshares = ((vesting_shares * used_power) / 10000)

        return rshares

    def hive_to_hbd(self, amount_hive):
        """ Conversion Ratio for given amount of HIVE to HBD at current
            price feed

            :param number hive: Amount of HIVE
        """
        return self.hbd_median_price() * amount_hive

    def hive(self, amount_hbd):
        """ Conversion Ratio for given amount of HBD to HIVE at current
            price feed

            :param number amount_hbd: Amount of HBD
        """
        return amount_hbd / self.hbd_median_price()

    def hbd_to_rshares(self, hbd_payout):
        """ Obtain r-shares from HBD

            :param number hbd_payout: Amount of HBD
        """
        hive_payout = self.hbd_to_hive(hbd_payout)

        reward_fund = self.hived.get_reward_fund()
        reward_balance = Amount(reward_fund['reward_balance']).amount
        recent_claims = int(reward_fund['recent_claims'])

        return int(recent_claims * hive_payout / (reward_balance - hive_payout))

    def rshares_2_weight(self, rshares):
        """ Obtain weight from rshares

            :param number rshares: R-Shares
        """
        _max = 2 ** 64 - 1
        return (_max * rshares) / (2 * self.CONTENT_CONSTANT + rshares)
