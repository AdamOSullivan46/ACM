#!/usr/bin/env python3

import random
from sys import argv

s = int(argv[1])
n = argv[2]
string= ""
for i in range(s):
    string += str(random.randint(0, 9))
print(string, n, end='')
