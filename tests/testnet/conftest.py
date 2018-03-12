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
def coin_owner(accounts):
    return accounts[0]

@pytest.fixture
def testernet_start(chain):
    block = chain.web3.eth.getBlock('latest')
    next_block = chain.web3.eth.getBlock(block.number+1)
    return next_block['timestamp']

@pytest.fixture
def ico_start(chain, test_crowdsale):
    block = chain.web3.eth.getBlock('latest')
    next_block = chain.web3.eth.getBlock(block.number+1)
    return next_block['timestamp']

@pytest.fixture
def moss_crowdsale(chain, moss_coin, coin_owner, ico_start, main_period, main_bonus_change_period, min_invest, max_invest, cap_main, rate, test_crowdsale):
    start = ico_start
    bonus1 = start + main_bonus_change_period
    bonus2 = bonus1 + main_bonus_change_period
    bonus3 = bonus2 + main_bonus_change_period
    end = start + main_period

    args = [start, bonus1, bonus2, bonus3, end, rate, cap_main, min_invest, max_invest, coin_owner, moss_coin.address, test_crowdsale.address]

    transaction = {
        "from" : coin_owner
    }

    contract, _ = chain.provider.deploy_contract('MossCrowdsale', deploy_args=args, deploy_transaction=transaction)
    moss_coin.transact({'from':coin_owner}).setCrowdsale(contract.address)

    return contract

@pytest.fixture
def test_crowdsale(chain, moss_coin, coin_owner, testernet_start, pre_period, min_invest, max_invest, cap_pre, rate):
    start = testernet_start
    end = start + pre_period

    args = [start, end, rate, min_invest, max_invest, coin_owner, moss_coin.address]

    transaction = {
        "from" : coin_owner
    }

    contract, _ = chain.provider.deploy_contract('Crowdsale', deploy_args=args, deploy_transaction=transaction)

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