from src.templating import Request, render_template

lang = {
    "en": {
        "title": "Delete session",
        "route": {
            "panel": "Control panel",
            "delete_session": "Delete session",
        },
    },
    "ru": {
        "title": "Удалить сессию",
        "route": {
            "panel": "Панель управления",
            "delete_session": "Удалить сессию",
        },
    },
}


async def response(request: Request) -> render_template:
    request.session.clear()
    return await render_template("routes/panel/delete_session.html", context={
        "lc": lang[request.lang],
    })
