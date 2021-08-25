#!/bin/python3

import math
import os
import random
import re
import sys


def detect_weird(n):
    if n in range(6,21) and n%2==0:
        return "Weird"
    elif n%2==0:
        return "Not Weird"
    else:
        return "Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(detect_weird(n))
