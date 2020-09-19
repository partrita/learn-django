from django.urls import path, include
from .views import frontpage, search, submit, newest, vote, story

app_name="hackernews"

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('<int:story_id>/vote/', vote, name='vote'),
    path('<int:story_id>/', story, name='story'),
    # path('u/', include('apps.userprofile.urls')),
    path('newest/', newest, name='newest'),
    path('search/', search, name='search'),
    path('submit/', submit, name='submit'),
]

## user profile

from .views import userprofile, votes, submissions

urlpatterns += [
    path('<str:username>/', userprofile, name='userprofile'),
    path('<str:username>/votes/', votes, name='votes'),
    path('<str:username>/submissions/', submissions, name='submissions'),
]