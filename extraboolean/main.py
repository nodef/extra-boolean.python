import re


# PARSE

def parse(s):
  """Converts string to boolean. `📘`_

  - s: a string

  Example:
    >>> parse("1")        == True
    >>> parse("truthy")   == True
    >>> parse("not off")  == True
    >>> parse("not true") == False
    >>> parse("inactive") == False
    >>> parse("disabled") == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/parse
  """
  rfal  = "(negati|never|refus|wrong|fal|off)|\\b(f|n|0)\\b"
  rneg = "\\b(nay|nah|no|dis|un|in)"
  f = re.search(rfal, s) is not None
  n = len(re.findall(rneg, s))%2 == 1
  return f == n




# NOT, EQ, NEQ, IMPLY, NIMPLY (FIXED)

def not(a):
  """Checks if value is false. `📘`_

  - a: a boolean

  Example:
    >>> not(False) == True
    >>> not(True)  == False

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/not
  """
  return not a


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


def neq(a, b):
  """Checks if antecedent ⇎ consequent (a ⇎ b). `📘`_

  - a: antecedent
  - b: consequent

  Example:
    >>> neq(true, false)  == true
    >>> neq(false, true)  == true
    >>> neq(true, true)   == false
    >>> neq(false, false) == false

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/neq
  """
  return a != b


def imply(a, b):
  """Checks if antecedent ⇒ consequent (a ⇒ b). `📘`_

  - a: antecedent
  - b: consequent

  Example:
    >>> imply(true, true)   == true
    >>> imply(false, true)  == true
    >>> imply(false, false) == true
    >>> imply(true, false)  == false

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/imply
  """
  return (not a) or b


def nimply(a, b):
  """Checks if antecedent ⇏ consequent (a ⇏ b). `📘`_

  - a: antecedent
  - b: consequent

  Example:
    >>> nimply(true, false)  == true
    >>> nimply(true, true)   == false
    >>> nimply(false, true)  == false
    >>> nimply(false, false) == false

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/nimply
  """
  return not imply(a, b)




# AND (VARIABLE)

def and(a=True, b=True, c=True, d=True, e=True, f=True, g=True, h=True):
  """Checks if all values are true. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> and(true, true)              == true
    >>> and(true, false)             == false
    >>> and(true, true, true, true)  == true
    >>> and(true, false, true, true) == false

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/and
  """
  return a and b and c and d and e and f and g and h




# OR (VARIABLE)

def or(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if any value is true. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> or(true, false)                == true
    >>> or(false, false)               == false
    >>> or(false, true, false, true)   == true
    >>> or(false, false, false, false) == false

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/or
  """
  return a or b or c or d or e or f or g or h




# XOR (VARIABLE)

def xor(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if odd no. of values are true. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> xor(true, false)             == true
    >>> xor(true, true)              == false
    >>> xor(true, true, true, false) == true
    >>> xor(true, true, true, true)  == false

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/xor
  """
  return a != b != c != d != e != f != g != h




# COUNT (VARIABLE)

def count(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Counts no. of true values. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> count(true, true)                == 2
    >>> count(true, false)               == 1
    >>> count(true, true, true, false)   == 3
    >>> count(false, true, false, false) == 1

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/count
  """
  return (1 if a else 0) + (1 if b else 0) + (1 if c else 0) + (1 if d else 0) \
       + (1 if e else 0) + (1 if f else 0) + (1 if g else 0) + (1 if h else 0)




# NAND (VARIABLE)

def nand(a=True, b=True, c=True, d=True, e=True, f=True, g=True, h=True):
  """Checks if any value is false. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> nand(true, false)             == true
    >>> nand(true, true)              == false
    >>> nand(true, true, false, true) == true
    >>> nand(true, true, true, true)  == false

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/nand
  """
  return not and(a, b, c, d, e, f, g, h)




# NOR (VARIABLE)

def nor(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if all values are false. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> nor(false, false)               == true
    >>> nor(true, false)                == false
    >>> nor(false, false, false, false) == true
    >>> nor(false, false, true, false)  == false

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/nor
  """
  return not or(a, b, c, d, e, f, g, h)




# XNOR (VARIABLE)

def xnor(a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if even no. of values are true. `📘`_

  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> xnor(true, true)               == true
    >>> xnor(false, true)              == false
    >>> xnor(true, true, false, false) == true
    >>> xnor(true, true, true, false)  == false

  .. _📘:
    https://github.com/python3f/extra-boolean/wiki/xnor
  """
  return not xor(a, b, c, d, e, f, g, h)




# SELECT (VARIABLE)

def select(i, a=False, b=False, c=False, d=False, e=False, f=False, g=False, h=False):
  """Checks if ith value is true. `📘`_

  - i: index
  - a: 1st boolean
  - b: 2nd boolean
  - ...

  Example:
    >>> select(0, true, false)              == true
    >>> select(1, true, false)              == false
    >>> select(1, true, true, false, false) == true
    >>> select(2, true, true, false, false) == false

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
