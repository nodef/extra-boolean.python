from extra_boolean import nor


def test_nor():
  assert nor(False, False)               == True
  assert nor(True, False)                == False
  assert nor(False, False, False, False) == True
  assert nor(False, False, True, False)  == False
