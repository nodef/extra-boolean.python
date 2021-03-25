from extra_boolean import eq


def test_eq():
  assert eq(True, True)   == True
  assert eq(False, False) == True
  assert eq(True, False)  == False
  assert eq(False, True)  == False
