from src.templating import Request, render_template
from instance.utils import generate_secret_key

lang = {
    "en": {
        "title": "Set up session",
        "route": {
            "panel": "Control panel",
            "set_session": "Set up session",
        },
    },
    "ru": {
        "title": "Установить сессию",
        "route": {
            "panel": "Панель управления",
            "set_session": "Установить сессию",
        },
    },
}


async def response(request: Request) -> render_template:
    request.session.update({"key": generate_secret_key(length=32)})
    return await render_template("routes/panel/set_session.html", context={
        "lc": lang[request.lang],
    })
