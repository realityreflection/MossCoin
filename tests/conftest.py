import pytest

@pytest.fixture(scope='session')
def total_supply():
    return 500000000

@pytest.fixture(scope='session')
def token_name():
    return "Moss Coin"

@pytest.fixture(scope='session')
def token_symbol():
    return "MOC"

@pytest.fixture(scope='session')
def token_decimals():
    return 18

@pytest.fixture(scope='session')
def invest_decimals(token_decimals):
    return token_decimals - 3

@pytest.fixture(scope='session')
def pre_period():
    return 600 # for test, real : 2*7*24*60*60 # 2 weeks

@pytest.fixture(scope='session')
def main_period():
    return 4*60 # for test, real : 4 weeks

@pytest.fixture(scope='session')
def main_bonus_change_period():
    return 60 # for test, real : 1 week

@pytest.fixture(scope='session')
def min_invest():
    return 100

@pytest.fixture(scope='session')
def max_invest():
    return 10000

@pytest.fixture(scope='session')
def cap_pre():
    return 25000000

@pytest.fixture(scope='session')
def cap_main():
    return 100000 # for test, real : 24999451

@pytest.fixture(scope='session')
def rate():
    return 10000