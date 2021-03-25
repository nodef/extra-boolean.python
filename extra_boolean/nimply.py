from .imply import imply


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
