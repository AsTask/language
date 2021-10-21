from src.templating import Request, render_template

lang = {
    "en": {
        "title": "Home page",
        "route": "Home page",
        "not_found": "Page not found",
        "server_error": "Server error",
    },
    "ru": {
        "title": "Главная страница",
        "route": "Главная страница",
        "not_found": "Страница не найдена",
        "server_error": "Ошибка сервера",
    },
}


async def response(request: Request) -> render_template:
    return await render_template("routes/index.html", context={
        "lc": lang[request.lang],
    })
