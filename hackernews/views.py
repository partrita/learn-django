import datetime
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import StoryForm, CommentForm
from .models import Story, Vote, Comment

def frontpage(request):
    date_from = timezone.now() - datetime.timedelta(days=1)

    stories = Story.objects.filter(created_at__gte=date_from).order_by('-number_of_votes')[0:30]

    return render(request, 'hackernews/frontpage.html', {'stories': stories})

def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        stories = Story.objects.filter(title__icontains=query)
    else:
        stories = []
    
    return render(request, 'hackernews/search.html', {'stories': stories, 'query': query})

def story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.created_by = request.user
            comment.save()

            return redirect('hackernews:story', story_id=story_id)
    else:
        form = CommentForm()
    
    return render(request, 'hackernews/detail.html', {'story': story, 'form': form})

def newest(request):
    stories = Story.objects.all()[0:200]

    return render(request, 'hackernews/newest.html', {'stories': stories})

@login_required
def vote(request, story_id):
    story = get_object_or_404(Story, pk=story_id)

    next_page = request.GET.get('next_page', '')

    if story.created_by != request.user and not Vote.objects.filter(created_by=request.user, story=story):
        vote = Vote.objects.create(story=story, created_by=request.user)
    
    if next_page == 'story':
        return redirect('hackernews:story', story_id=story_id)
    else:
        return redirect('hackernews:frontpage')

@login_required
def submit(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)

        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()

            return redirect('hackernews:frontpage')
    else:
        form = StoryForm()

    return render(request, 'hackernews/submit.html', {'form': form})




## user profile

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def userprofile(request, username):
    user = get_object_or_404(User, username=username)

    number_of_votes = 0

    for story in user.stories.all():
        number_of_votes = number_of_votes + (story.number_of_votes - 1)
    
    return render(request, 'hackernews/userprofile.html', {'user': user, 'number_of_votes': number_of_votes})

def votes(request, username):
    user = get_object_or_404(User, username=username)
    votes = user.votes.all()

    stories = []

    for vote in votes:
        stories.append(vote.story)
    
    return render(request, 'hackernews/votes.html', {'user': user, 'stories': stories})

def submissions(request, username):
    user = get_object_or_404(User, username=username)

    stories = user.stories.all()

    return render(request, 'hackernews/submissions.html', {'user': user, 'stories': stories})