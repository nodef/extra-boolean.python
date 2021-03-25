from extra_boolean import not_


def test_not_():
  assert not_(False) == True
  assert not_(True)  == False
