from bank_account import __version__
from bank_account.bank_account import *



def test_version():
    assert __version__ == '0.1.0'


def test_deposit():
    actual = 5000
    excepted = 5000
    assert actual == excepted 


def test_withdraw():
    actual = 2000
    excepted = 3000
    assert actual == excepted 


def test_enquiry():
    actual = 3000
    excepted = 3000
    assert actual == excepted 
    