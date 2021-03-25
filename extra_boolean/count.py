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
