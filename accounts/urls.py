from django.urls import path
from .views import LogInView, LogOutView, RegisterView

app_name='accounts'

urlpatterns = [
    path('login/', LogInView, name="login"),
    path('register/', RegisterView, name="register"),
]
