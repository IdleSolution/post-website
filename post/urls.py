from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<pk>', views.post, name='post'),
    path('user/<pk>', views.user, name='user'),
    path('post/<pk>/like',views.like, name='like'),
    path('user/<pk>/follow', views.follow, name='follow'),
    path('new_post', views.new_post, name='new_post'),
    path('post/<pk>/edit', views.edit_post, name='edit_post'),
    path('post/<pk>/delete', views.delete_post, name='delete_post')
]