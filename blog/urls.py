from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name ='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/publish/', views.post_publish, name="post_publish"),
    path('draft/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
]
