from hivebase.exceptions import BlockDoesNotExistsException

from .instance import shared_hived_instance
from .utils import parse_time


class Block(dict):
    """ Read a single block from the chain

        :param int block: block number
        :param Hived hived_instance: Hived() instance to use when
            accessing a RPC

    """

    def __init__(self, block, hived_instance=None):
        self.hived = hived_instance or shared_hived_instance()
        self.block = block

        if isinstance(block, Block):
            super(Block, self).__init__(block)
        else:
            self.refresh()

    def refresh(self):
        block = self.hived.get_block(self.block)
        if not block:
            raise BlockDoesNotExistsException
        super(Block, self).__init__(block)

    def __getitem__(self, key):
        return super(Block, self).__getitem__(key)

    def items(self):
        return super(Block, self).items()

    def time(self):
        return parse_time(self['timestamp'])
