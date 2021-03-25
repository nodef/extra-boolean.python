from extra_boolean import xor


def test_xor():
  assert xor(True, False)             == True
  assert xor(True, True)              == False
  assert xor(True, True, True, False) == True
  assert xor(True, True, True, True)  == False
