import typing
import os

from starlette.requests import Request
from starlette.responses import RedirectResponse

from instance.data import get_object
from src import templating


class Language:
    language = {
        "base": {
            "index": {
                "en": {
                    "sign_in": "Sign in",
                },
                "ru": {
                    "sign_in": "Войти",
                },
            },
            "not_found": {
                "en": {
                    "title": "Error 404",
                    "content": "Error 404. Page not found.",
                },
                "ru": {
                    "title": "Ошибка 404",
                    "content": "Ошибка 404. Страница не найдена.",
                },
            },
            "server_error": {
                "en": {
                    "title": "Error 500",
                    "header": "500. Server error.",
                    "content": "The server crashed on the given request.",
                    "back": "Back to site",
                },
                "ru": {
                    "title": "Ошибка 500",
                    "header": "500. Ошибка сервера.",
                    "content": "Сервер упал по данному запросу.",
                    "back": "Вернуться на сайт",
                },
            },
        },
    }

    @classmethod
    def initial_language(cls, main: str, template: str, request: Request) -> RedirectResponse | typing.Tuple:
        def query():
            nonlocal request
            return f"?{url_query}" if (url_query := request.url.query) else url_query

        current, ext, lang, http = (split := os.path.splitext(request.url.path))[0], split[1], (
            data := get_object(name="template")[template]
        )["lang"], getattr(templating, "Http")
        if data["multilingual"]:
            true, not_found, post, cookie, url_lang, lang_list = True, True, http.get(name="form").get(
                key := f"{template}-lang"
            ), request.cookies.get(key), ext[1:], True
            if post:
                if post != cookie and post in data["list"] or ext and url_lang not in data["list"]:
                    templating.set_cookie(key=key, value=post)
                    ext = f".{post}" if ext else ext
                    if not ext:
                        current = f"{main}{post}"
                    return RedirectResponse(url=f"{current}{ext}{query()}")
            if ext:
                lang_list = url_lang in data["list"]
                if lang_list:
                    templating.set_cookie(key=key, value=url_lang)
                    true, not_found, lang = False, False, url_lang
            if true:
                if cookie:
                    if cookie in data["list"]:
                        templating.set_cookie(key=key, value=cookie)
                        true, lang = False, cookie
                    else:
                        templating.delete_cookie(key=key)
            if true:
                templating.set_cookie(key=key, value=lang)
            if lang_list:
                not_found = False
            if main == current:
                return RedirectResponse(url=f"{main}{lang}")
            main = f"{main}{lang}"
            if not ext and (current_lang := current[1:]) in data["list"]:
                templating.set_cookie(key=key, value=current_lang)
                lang, current = current_lang, main
            ext = f".{lang}"
        else:
            not_found = False
        http.set(name="index", value=True if main == current else False)
        http.set(name="not_found", value=not_found)
        return lang, main, current, ext
