from src.templating import Request, delete_cookie, render_template

lang = {
    "en": {
        "title": "Delete cookies",
        "route": {
            "panel": "Control panel",
            "delete_cookie": "Delete cookies",
        },
    },
    "ru": {
        "title": "Удалить куки",
        "route": {
            "panel": "Панель управления",
            "delete_cookie": "Удалить куки",
        },
    },
}


async def response(request: Request) -> render_template:
    delete_cookie(key="key")
    return await render_template("routes/panel/delete_cookie.html", context={
        "lc": lang[request.lang],
    })
