from extra_boolean import parse


def test_parse():
  assert parse("1")        == True
  assert parse("truthy")   == True
  assert parse("not off")  == True
  assert parse("not true") == False
  assert parse("inactive") == False
  assert parse("disabled") == False
