from starlette.requests import Request
from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.applications import Starlette

from instance.const import SECRET_KEY, DOMAIN
from src.templating import HttpBase
from src.routing import routes


async def error(request: Request, exc):
    if not hasattr(exc, "status_code"):
        setattr(exc, "status_code", 500)
    return await HttpBase(request=request).error(status_code=exc.status_code)


def kwargs(domain):
    return {
        "middleware": [
            Middleware(TrustedHostMiddleware, allowed_hosts=[domain, f"*.{domain}"]),
            Middleware(SessionMiddleware, secret_key=SECRET_KEY),
        ],
        "exception_handlers": {
            404: error,
            500: error,
        },
    }


app = Starlette(routes=routes, **kwargs(domain=DOMAIN))
