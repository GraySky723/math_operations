#!/usr/bin/env python3
"""
math_functions.py
实现常用的数学运算，目前包括指数运算，后续会增加对数和开平方功能。
"""

def exponent(base, power):
    """返回 base 的 power 次方"""
    return base ** power

if __name__ == '__main__':
    a, b = 2, 3
    result = exponent(a, b)
    print(f"{a} 的 {b} 次方: {result}")
