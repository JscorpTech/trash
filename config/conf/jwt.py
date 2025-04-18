from datetime import timedelta

# from rest_framework_simplejwt.authentication import JWTAuthentication

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": "your-secret-key",
    "VERIFYING_KEY": None,
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=30),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=7),
    "UPDATE_LAST_LOGIN": True,
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "CHECK_REVOKE_TOKEN": True,
    "REVOKE_TOKEN_CLAIM": "revoke_token",
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
}
