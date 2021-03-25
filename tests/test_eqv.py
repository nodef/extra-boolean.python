from extra_boolean import eqv


def test_eqv():
  assert eqv(True, True)   == True
  assert eqv(False, False) == True
  assert eqv(True, False)  == False
  assert eqv(False, True)  == False
