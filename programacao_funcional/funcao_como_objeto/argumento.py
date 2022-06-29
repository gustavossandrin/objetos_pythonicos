"""
>>> def ola():
...     print('olá')
...
>>> executar(ola)
olá
>>> executar(ola, 2)
olá
olá
>>> def ola_mundo():
...     print('olá mundo')
...
>>> executar(ola_mundo, 3)
olá mundo
olá mundo
olá mundo

"""


def executar(f, n=1):
    for _ in range(n):
        f()
