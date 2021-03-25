from extra_boolean import nimply


def test_nimply():
  assert nimply(True, False)  == True
  assert nimply(True, True)   == False
  assert nimply(False, True)  == False
  assert nimply(False, False) == False
