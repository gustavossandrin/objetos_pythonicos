from functools import wraps
from time import sleep, strftime


def logar(fmt='%H:%M:%S'):
    def decorator(f):
        @wraps(f)
        def executar_com_tempo(*args, **kwargs):
            print(strftime(fmt))
            return f(*args, **kwargs)

        return executar_com_tempo

    return decorator


@logar(fmt='%H:%M:%S')
def mochileiro():
    return 42


@logar(fmt='%d/%m/%Y %H:%M:%S')
def ola(nome):
    return f'ola {nome}'


if __name__ == '__main__':
    print(mochileiro())
    print(mochileiro.__name__)
    print(ola('gustavo'))
    print(ola.__name__)
    sleep(1)
    print(mochileiro())
    print(ola('renzo'))
