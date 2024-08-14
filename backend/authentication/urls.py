from django.urls import path
from .views import get_users, create_user, alter_user

urlpatterns = [
    path("users/", get_users, name="get_users"),
    path("register/", create_user, name="create_user"),
    path('users/<int:primary_key>', alter_user, name='alter_user')
]