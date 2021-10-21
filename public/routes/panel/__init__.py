from src.templating import Request, render_template

lang = {
    "en": {
        "title": "Control panel",
        "route": "Control panel",
        "set_cookie": "Set cookies",
        "delete_cookie": "Delete cookies",
        "set_session": "Set up session",
        "delete_session": "Delete session",
        "redirect": "Redirect",
    },
    "ru": {
        "title": "Панель управления",
        "route": "Панель управления",
        "set_cookie": "Установить куки",
        "delete_cookie": "Удалить куки",
        "set_session": "Установить сессию",
        "delete_session": "Удалить сессию",
        "redirect": "Редирект",
    },
}


async def response(request: Request) -> render_template:
    request.session.update()
    return await render_template("routes/panel/index.html", context={
        "lc": lang[request.lang],
        "cookies_key": cookies if (cookies := request.cookies.get("key")) is None else "key",
        "cookies_value": cookies,
        "session_key": session if (session := request.session.get("key")) is None else "key",
        "session_value": session,
    })
