from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .models import Post, Rating
from .filters import MoversFilter
from .forms import RateForm, ContactForm
from django.urls import reverse
from django.db.models import Avg


# Create your views here.
def homepage(request):
    return render(request, 'smartmovers/home.html')


@login_required
def movers_list(request):
    context_object_name = 'posts'
    posts = Post.objects.all()
    myFilter = MoversFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    context = {
        'posts': posts,
        'myFilter': myFilter,
    }
    return render(request, 'smartmovers/movers.html', context)


@login_required
def PostDetail(request, pk):
    post = Post.objects.get(id=pk)
    ratings = Rating.objects.filter(post=post)
    average_ratings = ratings.aggregate(Avg('rate'))
    total_ratings = ratings.count()
    context = {
        'post': post,
        'average_ratings': average_ratings,
        'ratings': ratings,
        'total_ratings': total_ratings,
    }
    return render(request, 'smartmovers/details.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'smartmovers/new_post.html'
    fields = ['name', 'location', 'phone', 'availability', 'vehicle_type', 'image', 'description', 'least_price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'smartmovers/new_post.html'
    fields = ['name', 'location', 'phone', 'availability', 'image', 'vehicle_type', 'description', 'least_price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'smartmovers/post_delete_confirm.html'
    success_url = '/post/movers'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


@login_required
def Rate(request, pk):
    # getting post objects by their id
    post = Post.objects.get(id=pk)
    user = request.user
    # form method
    if request.method == 'POST':
        form = RateForm(request.POST)
        # validating the form.
        if form.is_valid():
            rate = form.save()
            rate.post = post
            rate.user = user
            rate.save()
            return HttpResponseRedirect(reverse('detail', args=[pk]))
    else:
        form = RateForm()
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'smartmovers/rate.html', context)

def contact(request):
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
    else:
        c_form = ContactForm()

    context = {
        'c_form':form,
    }
    return render(request,'smartmovers/details.html',context)
