from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_user, name='create'),
    path('list/', views.user_list, name='list'),
    path('create/', views.create_user, name='create'),
    path('update/<pk>', views.update_user, name='update'),
    path('delete/<pk>', views.delete_user, name='delete'),
]