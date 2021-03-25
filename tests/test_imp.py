from extra_boolean import imp


def test_imp():
  assert imp(True, True)   == True
  assert imp(False, True)  == True
  assert imp(False, False) == True
  assert imp(True, False)  == False
