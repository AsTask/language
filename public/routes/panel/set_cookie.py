from src.templating import Request, set_header, set_cookie, render_template
from instance.utils import generate_secret_key

lang = {
    "en": {
        "title": "Set cookies",
        "route": {
            "panel": "Control panel",
            "set_cookie": "Set cookies",
        },
    },
    "ru": {
        "title": "Установить куки",
        "route": {
            "panel": "Панель управления",
            "set_cookie": "Установить куки",
        },
    },
}


async def response(request: Request) -> render_template:
    key, value = "key", generate_secret_key(length=32)
    set_header(key=key, value=value)
    set_cookie(key=key, value=value)
    return await render_template("routes/panel/set_cookie.html", context={
        "lc": lang[request.lang],
    })
