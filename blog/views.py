from django.views.generic import ListView, DetailView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic import DayArchiveView, TodayArchiveView

from blog.models import Post

from django.views.generic import FormView 
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render 


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


#--- DetailView
class PostDV(DetailView):
    model = Post


#--- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'


#---FormView

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        search_Word = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=search_Word) | Q(description__icontains=search_Word) | Q(content__icontains=search_Word)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = search_Word 
        context['object_list'] = post_list
        
        return render(self.request, self.template_name, context)