from django.conf import settings

URL_GITHUB_ACCESS_TOKEN = "https://github.com/login/oauth/access_token"
URL_GITHUB_USER_INFO = "https://api.github.com/user"
URL_GITHUB_LOGIN = (
    f"https://github.com/login/oauth/authorize?scope=user:email&client_id={ settings.DJANGO_GITHUB_CLIENT_ID }"
)
