"""Boolean data type has two possible truth values to represent logic."""

import re




# NOT (FIXED)
# -----------

def not_(a):
  """Checks if value is False. `📘`_

  - a: a boolean

  Example:
    >>> not_(False) == True
    >>> not_(True)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/not
  """
  return not a




# EQ (FIXED)
# ----------

def eq(a, b):
  """Checks if antecedent ⇔ consequent (a ⇔ b). `📘`_

  - a: antecedent
  - b: consequent

  Example:
    >>> eq(True, True)   == True
    >>> eq(False, False) == True
    >>> eq(True, False)  == False
    >>> eq(False, True)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/eq
  """
  return a == b




# NEQ (FIXED)
# -----------

def neq(a, b):
  """Checks if antecedent ⇎ consequent (a ⇎ b). `📘`_

  - a: antecedent
  - b: consequent

  Example:
    >>> neq(True, False)  == True
    >>> neq(False, True)  == True
    >>> neq(True, True)   == False
    >>> neq(False, False) == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/neq
  """
  return a != b




# IMPLY (FIXED)
# -------------

def imply(a, b):
  """Checks if antecedent ⇒ consequent (a ⇒ b). `📘`_

  - a: antecedent
  - b: consequent

  Example:
    >>> imply(True, True)   == True
    >>> imply(False, True)  == True
    >>> imply(False, False) == True
    >>> imply(True, False)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/imply
  """
  return (not a) or b




# NIMPLY (FIXED)
# --------------

def nimply(a, b):
  """Checks if antecedent ⇏ consequent (a ⇏ b). `📘`_

  - a: antecedent
  - b: consequent

  Example:
    >>> nimply(True, False)  == True
    >>> nimply(True, True)   == False
    >>> nimply(False, True)  == False
    >>> nimply(False, False) == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/nimply
  """
  return not imply(a, b)




# AND (VARIABLE)
# --------------

def and_(a=True, b=True, c=True, d=True, e=True, f=True, g=True, h=True):
  """Checks if all values are True. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> and_(True, True)              == True
    >>> and_(True, False)             == False
    >>> and_(True, True, True, True)  == True
    >>> and_(True, False, True, True) == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/and
  """
  return a and b and c and d and e and f and g and h




# OR (VARIABLE)
# -------------

def or_(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if any value is True. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> or_(True, False)                == True
    >>> or_(False, False)               == False
    >>> or_(False, True, False, True)   == True
    >>> or_(False, False, False, False) == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/or
  """
  return a or b or c or d or e or f or g or h




# XOR (VARIABLE)
# --------------

def xor(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if odd no. of values are True. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> xor(True, False)             == True
    >>> xor(True, True)              == False
    >>> xor(True, True, True, False) == True
    >>> xor(True, True, True, True)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/xor
  """
  return ((a != b) != (c != d)) != ((e != f) != (g != h))




# NAND (VARIABLE)
# ---------------

def nand(a=True, b=True, c=True, d=True, e=True, f=True, g=True, h=True):
  """Checks if any value is False. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> nand(True, False)             == True
    >>> nand(True, True)              == False
    >>> nand(True, True, False, True) == True
    >>> nand(True, True, True, True)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/nand
  """
  return not and_(a, b, c, d, e, f, g, h)




# NOR (VARIABLE)
# --------------

def nor(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if all values are False. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> nor(False, False)               == True
    >>> nor(True, False)                == False
    >>> nor(False, False, False, False) == True
    >>> nor(False, False, True, False)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/nor
  """
  return not or_(a, b, c, d, e, f, g, h)




# XNOR (VARIABLE)
# ---------------

def xnor(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if even no. of values are True. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> xnor(True, True)               == True
    >>> xnor(False, True)              == False
    >>> xnor(True, True, False, False) == True
    >>> xnor(True, True, True, False)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/xnor
  """
  return not xor(a, b, c, d, e, f, g, h)




# COUNT (VARIABLE)
# ----------------

def count(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Counts no. of True values. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> count(True, True)                == 2
    >>> count(True, False)               == 1
    >>> count(True, True, True, False)   == 3
    >>> count(False, True, False, False) == 1

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/count
  """
  return (1 if a else 0) + (1 if b else 0) + (1 if c else 0) + (1 if d else 0) \
       + (1 if e else 0) + (1 if f else 0) + (1 if g else 0) + (1 if h else 0)




# SELECT (VARIABLE)
# -----------------

def select(i, a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if ith value is True. `📘`_

  - i: index
  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> select(0, True, False)              == True
    >>> select(1, True, False)              == False
    >>> select(1, True, True, False, False) == True
    >>> select(2, True, True, False, False) == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/select
  """
  if i == 0: return a
  elif i == 1: return b
  elif i == 2: return c
  elif i == 3: return d
  elif i == 4: return e
  elif i == 5: return f
  elif i == 6: return g
  elif i == 7: return h
  return False




# EQV (SHORTCUT)
# --------------

def eqv(a, b):
  """Checks if antecedent ⇔ consequent (a ⇔ b). `📘`_

  - a: antecedent
  - b: consequent

  Example:
    >>> eqv(True, True)   == True
    >>> eqv(False, False) == True
    >>> eqv(True, False)  == False
    >>> eqv(False, True)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/eqv
  """
  return eq(a, b)




# IMP (SHORTCUT)
# --------------

def imp(a, b):
  """Checks if antecedent ⇒ consequent (a ⇒ b). `📘`_

  - a: antecedent
  - b: consequent

  Example:
    >>> imp(True, True)   == True
    >>> imp(False, True)  == True
    >>> imp(False, False) == True
    >>> imp(True, False)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/imp
  """
  return imply(a, b)




# PARSE
# -----

_RNUM = re.compile(r"^[-+]?\d+$")
_RTRU = re.compile(r"\b(?:t|y|1)\b|\b(?:\+|ay|go|on|up)|(?:tru|acc|asc|day|for|hot|inc|joy|new|pos|top|win|yes|dawn|full|safe|grow|high|just|real|some|know|live|love|open|pure|shin|warm|wis[de]|activ|admit|advan|agree|begin|brigh|build|creat|early|enter|float|f(?:i|ou)nd|grant|light|north|prett|prese|publi|start|succe|victr)", re.IGNORECASE)
_RFAL = re.compile(r"\b(?:f|n|0)\b|(?:fal|off|dim|end|low|old|back|cold|cool|dark|dead|decr|desc|dirt|down|dull|dusk|exit|late|sink|ugly|absen|botto|close|finis|night|priva|south|wrong)", re.IGNORECASE)
_RNEG = re.compile(r"\b(?:-|na|no|un|in|aft|bad|dis|lie|non|ben[dt]|den[iy]|empt|fail|fake|hate|los[es]|stop|decli|defea|destr|never|negat|refus|rejec|forget|shr[iu]nk|against|is.?nt|can.?(?:no)?t)|(?:hind)", re.IGNORECASE)

def parse(s):
  """Converts string to boolean. `📘`_

  - s: a string

  Example:
    >>> parse("1")            == True
    >>> parse("truthy")       == True
    >>> parse("Not Off")      == True
    >>> parse("Not Inactive") == True
    >>> parse("cold")         == False
    >>> parse("inactive")     == False
    >>> parse("Negative Yes") == False
    >>> parse("Negative Aye") == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/parse
  """
  if _RNUM.match(s): return int(s) > 0
  t = _RTRU.search(s) is not None
  f = _RFAL.search(s) is not None
  n = len(_RNEG.findall(s)) % 2 == 1
  return nimply(f, t) == n
