from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .models import Post
from .filters import MoversFilter


# Create your views here.
def homepage(request):
    return render(request, 'smartmovers/home.html')



@login_required
def movers_list(request):
    context_object_name = 'posts'
    posts = Post.objects.all()
    myFilter = MoversFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    context ={
        'posts': posts,
        'myFilter': myFilter,
    }
    return render(request,'smartmovers/movers.html',context)
#
# class PostListView(LoginRequiredMixin,ListView):
#     model = Post
#     template_name= 'smartmovers/movers.html'
#     context_object_name = 'posts'
#     paginate_by = 4
#
#     def get_queryset(self):
#         qs = self.model.objects.all()
#         myFilter= MoversFilter(self.request.GET, queryset=qs)
#         return myFilter.qs


class PostDetailView(DetailView):
    model = Post
    template_name = 'smartmovers/details.html'
    context_object_name='post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'smartmovers/new_post.html'
    fields =   ['name', 'location','phone','availability','vehicle_type','image','description','least_price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'smartmovers/new_post.html'
    fields =  ['name', 'location','phone','availability','image','vehicle_type','description','least_price']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
             return True
        else:
            return False


class PostDeleteView(DeleteView):
    model = Post
    template_name= 'smartmovers/post_delete_confirm.html'
    success_url = '/post/movers'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
