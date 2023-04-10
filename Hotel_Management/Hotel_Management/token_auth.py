from rest_framework_simplejwt.backends import TokenBackend
from django.contrib.auth.models import AnonymousUser
from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async
from urllib import parse
from account.models import User
import jwt
from django.conf import settings

@database_sync_to_async
def get_user(token):
    try:
        print("token:-", token)
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=['HS256'])
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        return User.objects.get(email=valid_data['email_id'])
    
    except Exception as e:
        print(e)
        return AnonymousUser()
        


class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        decoded_qs = parse.parse_qs(scope["query_string"])
        if b'token' in decoded_qs:
            token = decoded_qs.get(b'token').pop().decode()
            scope["user"] = await get_user(token)
        return await self.inner(scope, receive, send)


TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))