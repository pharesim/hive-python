from hive.amount import Amount


def test_amount_init():
    a = Amount('1 HIVE')
    assert dict(a) == {'amount': 1.0, 'asset': 'HIVE'}
