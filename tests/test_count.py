from extra_boolean import count


def test_count():
  assert count(True, True)                == 2
  assert count(True, False)               == 1
  assert count(True, True, True, False)   == 3
  assert count(False, True, False, False) == 1
