from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# ListView: Display all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Customize template path
    context_object_name = 'posts'

# DetailView: Show a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# CreateView: Allow users to create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView: Allow authors to update their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# DeleteView: Allow authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')  # Redirect after deletion
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author







# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
# from .forms import CustomUserCreationForm

# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('profile')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'blog/register.html', {'form': form})

# @login_required
# def profile_view(request):
#     return render(request, 'blog/profile.html', {'user': request.user})

# @login_required
# def edit_profile_view(request):
#     if request.method == 'POST':
#         request.user.email = request.POST.get('email')
#         request.user.save()
#         return redirect('profile')
#     return render(request, 'blog/edit_profile.html', {'user': request.user})
