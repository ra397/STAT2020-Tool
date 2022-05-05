from calculate import *

assert Bin(5, 4, 0.8) == 'X must be 0, 1, ..., n'
assert Bin(-1, 4, 0.8) == 'X must be 0, 1, ..., n'
assert Bin(2.5, 4, 0.8) == 'X must be 0, 1, ..., n'
assert Bin(4.2, 4, 0.8) == 'X must be 0, 1, ..., n'
assert Bin(0.8, 4, 0.8) == 'X must be 0, 1, ..., n'
assert Bin(2, 4, 1.1) == '0 <= p <= 1'
assert Bin(2, 4, -0.1) == '0 <= p <= 1'
assert Bin(2, -1, 0.1) == 'N must be a natural number'
assert Bin(2, -0.5, 0.5) == 'N must be a natural number'
assert Bin(2, 0.5, 0.50) == 'N must be a natural number'
assert Bin(5, 10, 0.5) == 0.2461
assert Bin(5, 1000, 0.05) == 0
assert Bin(1, 10, 0.4) == 0.0403
