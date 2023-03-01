from django.urls import path
from accounts import views
from django.shortcuts import redirect

# app_name = 'accounts'
urlpatterns = [
    path('', lambda request: redirect('login/', permanent=True)),
    path('login/', views.login, name="Login"),
    path('signup/', views.signup, name="Signup"),   
]