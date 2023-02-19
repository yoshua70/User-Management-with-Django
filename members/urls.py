from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name="homepage"),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user_by_admin',
         views.register_user_by_admin, name="register_by_admin"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('users/delete/<str:id>/', views.delete_user, name="delete_user")
]
