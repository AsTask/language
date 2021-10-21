import typing
import os
import pickle
import random
import binascii


def dir_path(file: __file__) -> str:
    """Аргумент file принимает атрибут модуля __file__.
     Возвращает строку абсолютного пути от корневой до текущей директории.
    """
    return os.path.dirname(os.path.abspath(file))


def pack_name(file: __file__) -> str:
    """Аргумент file принимает атрибут модуля __file__.
     Возвращает название текущего корневого пакета.
    """
    return os.path.relpath(os.path.dirname(os.path.abspath(file)), start=os.getcwd()).split(os.sep)[0]


def pack_path(file: __file__) -> str:
    """Аргумент file принимает атрибут модуля __file__.
     Возвращает строку от текущего корневого пакета до текущего пакета. В качестве разделителей используются точки.
    """
    path, name = os.path.dirname(os.path.abspath(file)), os.path.basename(file).split(".")[0]
    return os.path.relpath(
        path if name == "__init__" else os.path.join(path, name),
        start=os.getcwd()
    ).replace(os.sep, '.')


def generate_secret_key(length: int) -> str:
    """Аргумент length принимает четное число из диапозона [ 8 - 256 ].
     Возвращает случайную строку, длиной определённой в аргументе length,
     состоящую из цифр и букв, из таблицы ascii, случайных по регистру.
    """
    assert \
        type(length) is int and 8 <= length <= 256 and not length % 2, \
        f"Значение аргумента length функции generate_secret_key должено быть четным числом из диапозона [ 8 - 256 ]"
    return "".join(
        [x if x.isdigit() else (x if random.getrandbits(1) else x.upper()) for x in binascii.hexlify(
            os.urandom((8 if length < 8 else (256 if length > 256 else length)) // 2)
        ).decode()]
    )
