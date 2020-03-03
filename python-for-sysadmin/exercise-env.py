#!/usr/bin/env python3.6
from math import pi
import os

os.environ['DIGITS'] = "2"
digits = int(os.getenv("DIGITS",10))
if digits:
    print("%.*f" % (digits, pi))
