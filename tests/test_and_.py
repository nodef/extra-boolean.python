from extra_boolean import and_


def test_and_():
  assert and_(True, True)              == True
  assert and_(True, False)             == False
  assert and_(True, True, True, True)  == True
  assert and_(True, False, True, True) == False
