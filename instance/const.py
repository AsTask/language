import os
import pickle

from starlette.config import Config
from starlette.datastructures import Secret

from instance.utils import dir_path, generate_secret_key


class Configuration(Config):
    def __init__(self) -> None:
        if not os.path.isfile(environ := os.path.join(path := dir_path(__file__), "data", ".environ")):
            with open(environ, "w") as f:
                f.write(
                    f"PUBLIC_PATH={os.path.abspath(os.path.join(path, os.pardir, 'public'))}\n"
                    f"DOMAIN=127.0.0.1\n"
                    f"SECRET_KEY={generate_secret_key(length=32)}\n"
                )
        if not os.path.isfile(template := os.path.join(path, "data", "template.pkl")):
            with open(template, "wb") as f:
                f.write(pickle.dumps({
                    "base": {
                        "lang": "ru",
                        "multilingual": True,
                        "list": ["en", "ru"],
                    },
                }))
        Config.__init__(self, environ)


config = Configuration()

PUBLIC_PATH = config("PUBLIC_PATH", cast=str)
DOMAIN = config("DOMAIN", cast=str)
SECRET_KEY = config("SECRET_KEY", cast=Secret)
