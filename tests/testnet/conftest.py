import time
import pytest

@pytest.fixture
def moss_coin(chain, coin_owner, total_supply):
    args = [total_supply]

    transaction = {
        'from' : coin_owner
    }

    contract, _ = chain.provider.deploy_contract('MossCoin', deploy_args=args, deploy_transaction=transaction)
    return contract

@pytest.fixture
def testernet_start():
    return 1410973381

@pytest.fixture
def moss_crowdsale(chain, moss_coin, coin_owner, testernet_start, period, min_invest, max_invest, cap, rate):
    start = testernet_start
    end = start + period

    args = [start, end, rate, cap, min_invest, max_invest, coin_owner, moss_coin.address]

    transaction = {
        "from" : coin_owner
    }

    contract, _ = chain.provider.deploy_contract('MossCrowdsale', deploy_args=args, deploy_transaction=transaction)
    moss_coin.transact({'from':coin_owner}).setCrowdsale(contract.address, True)

    return contract


@pytest.fixture
def upgrade_target(chain, moss_coin, coin_owner):
    args = [moss_coin.address]

    transaction = {
        "from" : coin_owner
    }

    contract, _ = chain.provider.deploy_contract('UpgradeTestToken', deploy_args=args, deploy_transaction=transaction)
    
    return contract

@pytest.fixture
def upgrade_target2(chain, moss_coin, coin_owner):
    args = [moss_coin.address]

    transaction = {
        "from" : coin_owner
    }

    contract, _ = chain.provider.deploy_contract('UpgradeTestToken', deploy_args=args, deploy_transaction=transaction)
    
    return contract