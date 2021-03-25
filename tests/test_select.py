from extra_boolean import select


def test_select():
  assert select(0, True, False)              == True
  assert select(1, True, False)              == False
  assert select(1, True, True, False, False) == True
  assert select(2, True, True, False, False) == False
