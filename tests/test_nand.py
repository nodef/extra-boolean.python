from extra_boolean import nand


def test_nand():
  assert nand(True, False)             == True
  assert nand(True, True)              == False
  assert nand(True, True, False, True) == True
  assert nand(True, True, True, True)  == False
