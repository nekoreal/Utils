from functools import singledispatch

@singledispatch
def fun(arg):
    print("default:", arg)

@fun.register(int)
def _(arg):
    print("int:", arg)

fun(10)      # int: 10
fun("hello") # default: hello

"""
Позволяет делать перегрузку функций по типу первого аргумента.
"""