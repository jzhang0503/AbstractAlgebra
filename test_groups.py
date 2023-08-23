#test file for groups.py

import pytest
from groups import *

def test_check_add_inverse_mod_n():
    assert is_group("0,1,2,3,4,5,6,7,8,9,10", "add mod 11") == "Success: Set is a group under addition mod 11.0"
    assert is_group("1,2,3,4,5,6,7,8,9,10", "mult mod 11") != "Success: Set is a group under multiplication mod 11"