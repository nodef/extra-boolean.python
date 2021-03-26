from extra_boolean import parse


def test_parse():
  assert parse("1")            == True
  assert parse("truthy")       == True
  assert parse("Not Off")      == True
  assert parse("Not Inactive") == True
  assert parse("cold")         == False
  assert parse("inactive")     == False
  assert parse("Negative Yes") == False
  assert parse("Negative Aye") == False
