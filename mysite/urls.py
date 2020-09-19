from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings

urlpatterns = [
    path('hackernews/', include('hackernews.urls')),
    path('todo/', include('bulma_todo.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    # path('profile/', user_views.profile, name='profile'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('tools/', include('tools.urls')),
    path('lotto/', include('mylotto.urls')),
    # path('users/', include('users.urls')),
    path('polls/', include('polls.urls')),
    path('cal/', include('cal.urls')),
    path('boards/', include('boards.urls')),
    path('schedule/', include('schedule.urls')),
    # path('events/', include('events.urls')),
    path('crud/', include('crud.urls')),
    path('news/', include('news.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('wordcount/', include('wordcount.urls')),
    path('csv/', include('csv_app.urls')),
    path('catalog/', include('catalog.urls')),
    path('', include('blog.urls')),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
