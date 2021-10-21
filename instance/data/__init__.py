import typing
import os
import pickle

from instance.utils import dir_path, pack_path


def get_object(name: str) -> typing.Any:
    assert \
        name.lower() in (pkl := ("language", "template")), \
        f"{pack_path(__file__)} 'get_pickle': добавьте название '{name}' в кортеж сериализованных объектов {pkl}"
    with open(os.path.join(dir_path(__file__), f"{name}.pkl"), "rb") as f:
        return pickle.loads(f.read())
