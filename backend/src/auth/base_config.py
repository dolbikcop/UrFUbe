from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from auth.manager import get_user_manager
from auth.models import User

from config import SECRET_KEY_JWT


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY_JWT, lifetime_seconds=60 * 60)


cookie_transport = CookieTransport(cookie_name="untasty_and_tochka", cookie_max_age=60 * 60, cookie_secure=False)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
