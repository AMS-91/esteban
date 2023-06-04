from django.urls import path
from .views import hello

app_name = "accounts"


urlpatterns = [
    path('', hello, name="hello")
]