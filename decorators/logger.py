from functools import wraps
from typing import Callable
from datetime import datetime

def logger(
        txtfile:str="log.txt",
        print_log:bool=False,
        time_log:bool=False,
        raise_exc:bool=True,
        only_exc:bool=True,
):
    def wrapper(func:Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            res, exc = None, None
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                exc = e
            if (not only_exc) or exc:
                log = (f"{ datetime.now() if time_log else '' } "
                       f"\nfunc:{func.__name__}->{res}"
                       f"\nargs:{args} kwargs:{kwargs}"
                       f"{f'\n\nexc{exc}\n' if exc else '' }")
                if print_log:
                    print(log)
                with open(txtfile, "a") as f:
                    f.write(log)
                if raise_exc and exc:
                    raise exc
            return res
        return inner
    return wrapper


