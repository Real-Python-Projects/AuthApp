from django.urls import path
from .views import (LogInView, LogOutView, 
                    RegisterView, ResetPasswordView, RequestResetEmail)

app_name='accounts'

urlpatterns = [
    path('login/', LogInView, name="login"),
    path('register/', RegisterView, name="register"),
    path("logout/", LogOutView, name="logout"),
    
    
]
