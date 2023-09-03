from django.urls import path
from users.api import api_view

urlpatterns = [
    path('users/', api_view.userList_api_view, name='get_users'),
    path('users/create', api_view.userCreate_api_view, name='user_create'),
    path('users/<int:id>', api_view.getUser_api_view, name='user_detail'),
    path('users/<int:id>/edit', api_view.getUser_api_view, name='user_edit'),
    path('users/<int:id>/delete', api_view.getUser_api_view, name='user_delete')
]
