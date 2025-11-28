from functools import wraps
from typing import Callable
from datetime import datetime

def logger(txtfile:str='logs.txt',
           printlog:bool=False,
           raiseexc:bool=False,
           time:bool=False,
           ):
    def wrapper(func:Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal txtfile,printlog,raiseexc
            exc,res=None,None
            try:
                res=func(*args, **kwargs)
            except Exception as e:
                exc=e
            if printlog:
                print(f"Func nme:{func.__name__}"
                      f"\nargs:{args}\nkwargs:{kwargs}"
                      f"\nres:{res}"
                      f"{f'\nexc:{exc}' if exc else '' }")
            with open(txtfile, 'a') as f:
                f.write(f"\n"
                        f"{f"\n{datetime.now()}" if time else ''}"
                        f"\nFunc nme:{func.__name__}"
                        f"\nargs:{args}"
                        f"\nkwargs:{kwargs}"
                        f"\nres:{res}"
                        f"\n{f"\n{'-'*10}\nexc:{exc}\n{'-'*10}\n" if exc else ''}")
            if exc and raiseexc: raise exc
            return res
        return inner
    return wrapper

