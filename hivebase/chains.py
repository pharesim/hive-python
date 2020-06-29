default_prefix = "STM"

known_chains = {
    "HIVE": {
        "chain_id": "0" * int(256 / 4),
        "prefix": "STM",
        "hive_symbol": "HIVE",
        "hbd_symbol": "HBD",
        "vests_symbol": "VESTS",
    },
    "STEEM": {
        "chain_id": "0" * int(256 / 4),
        "prefix": "STM",
        "hive_symbol": "STEEM",
        "hbd_symbol": "SBD",
        "vests_symbol": "VESTS",
    },
    "GOLOS": {
        "chain_id": "782a3039b478c839e4cb0c941ff4eaeb7df40bdd68bd441afd444b9da763de12",
        "prefix": "GLS",
        "hive_symbol": "GOLOS",
        "hbd_symbol": "GBG",
        "vests_symbol": "GESTS",
    },
    "TESTS": {
        "chain_id":
            "46d82ab7d8db682eb1959aed0ada039a6d49afa1602491f93dde9cac3e8e6c32",
        "prefix":
            "TST",
        "hive_symbol":
            "TESTS",
        "hbd_symbol":
            "TBD",
        "vests_symbol":
            "VESTS",
    },
}
