#!/usr/bin/env python3
"""
math_functions.py
实现常用的数学运算，目前包括指数运算，后续会增加对数和开平方功能。
"""
import math

def exponent(base, power):
    """返回 base 的 power 次方"""
    return base ** power


def logarithm(value, base):
    """
    返回 value 在 base 底下的对数
    当 value <= 0 或 base <= 0 或 base == 1 时, 抛出 ValueError
    """
    if value <= 0 or base <= 0 or base == 1:
        raise ValueError("请输入正确的正实数，并且底数不为1")
    return math.log(value, base)

def square_root(value):
    """
    返回 value 的开平方，如果 value 为负数则抛出 ValueError。
    """
    if value < 0:
        raise ValueError("负数不能开平方")
    return value ** 0.5


if __name__ == '__main__':
    a, b = 4, 2
    exponent = exponent(a, b)
    logarithm = logarithm(a, b)
    square_root = square_root(a)
    print(f"{a} 的 {b} 次方: {exponent}")
    print(f"以 {b} 为底 {a} 的对数: {logarithm}")
    print(f"{a} 的 平方根: {square_root}")