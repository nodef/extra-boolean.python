from extra_boolean import or_


def test_or_():
  assert or_(True, False)                == True
  assert or_(False, False)               == False
  assert or_(False, True, False, True)   == True
  assert or_(False, False, False, False) == False
