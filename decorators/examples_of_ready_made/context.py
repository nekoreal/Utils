import contextlib

@contextlib.contextmanager
def func(*args,**kwargs):
    print(args,kwargs)
    yield
    print('finished')


with func(23,324,23,r=2,f=3) as f:
    print('inside func')

'''
Для запросов в бд удобно
в функции вписал создание сессии или подключения в начале 
потом yield
потом закрытие сессии, отключении или коммит в бд
'''
