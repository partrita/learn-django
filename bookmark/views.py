from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy # 타이밍 로딩 문제로 generic view에서는 reverse는 사용할 수 없고 reverse_lazy를 사용해야한다.

class BookmarkListView(ListView):
    model = Bookmark
    # paginate_by = 5 # 페이지 만들기, 지금은 별로 필요없어서 안함
    # template_name = 'bookmark_list.html'
    # context_object_name = 'bookmark_list'
    # def get_queryset(self):
    #     return Bookmark.objects.all()

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('bookmark:list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')
