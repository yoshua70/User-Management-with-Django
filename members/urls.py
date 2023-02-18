from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name="homepage"),
    path('login_user', views.login_user, name="login"),
    path('dashboard', views.dashboard, name="dashboard")
]
