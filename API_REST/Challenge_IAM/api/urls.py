from django.urls import path
from .views import PermissionView
from .views import UserView

urlpatterns=[
    #GET
    path('permissions/',PermissionView.as_view(),name = 'permission_list'), 
    #GET Per id
    path('permissions/<int:id>',PermissionView.as_view(),name = 'permission_list'),
    #POST
    path('permissions/create',PermissionView.as_view(),name = 'permission_list'),
    #PUT
    path('permissions/update/<int:id>',PermissionView.as_view(),name = 'permission_list'),
    #GET
    path('users/',UserView.as_view(),name = 'permission_list'), 
    #POST
    path('users/create/',UserView.as_view(),name = 'user_list'),
    #PUT
    path('users/update/<int:id>',UserView.as_view(),name = 'user_list'),
    #DEL
    path('users/remove/<int:id>',UserView.as_view(),name = 'user_list'),
]