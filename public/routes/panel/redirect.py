from src.templating import Request, routes, redirect, form, render_template

lang = {
    "en": {
        "title": "Redirect",
        "route": {
            "panel": "Control panel",
            "redirect": "Redirect",
        },
        "redirect_index": "Redirect to home",
    },
    "ru": {
        "title": "Редирект",
        "route": {
            "panel": "Панель управления",
            "redirect": "Редирект",
        },
        "redirect_index": "Редирект на главную",
    },
}


async def response(request: Request) -> render_template:
    if "redirect" in form():
        return redirect(url=routes("index"))
    return await render_template("routes/panel/redirect.html", context={
        "lc": lang[request.lang],
    })
