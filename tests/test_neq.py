from extra_boolean import neq


def test_neq():
  assert neq(True, False)  == True
  assert neq(False, True)  == True
  assert neq(True, True)   == False
  assert neq(False, False) == False
