from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy


from .forms import PostCreateForm
from .models import Post



class PostList(ListView):
	model = Post
	template_name = 'posts/post_list.html'



class PostCreate(CreateView):
	model = Post
	form_class = PostCreateForm
	template_name = 'posts/post_create.html'
	success_url = reverse_lazy('post_list')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostDetail(DetailView):
	model = Post
	template_name = 'posts/post_detail.html'
	
