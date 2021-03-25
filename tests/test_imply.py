from extra_boolean import imply


def test_imply():
  assert imply(True, True)   == True
  assert imply(False, True)  == True
  assert imply(False, False) == True
  assert imply(True, False)  == False
