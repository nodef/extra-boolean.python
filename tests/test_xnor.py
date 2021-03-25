from extra_boolean import xnor


def test_xnor():
  assert xnor(True, True)               == True
  assert xnor(False, True)              == False
  assert xnor(True, True, False, False) == True
  assert xnor(True, True, True, False)  == False
