from django.shortcuts import render
from .models import Blogs
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin


def search(request):
	template='UserInfo/mypost.html'
	query=request.GET.get('q')
	results=Blogs.objects.filter(title__icontains=query)
	text='No posts matched your search for "'+query+'"'
	context={'blogs':results,'text':text}
	return render(request,template,context)

def search1(request):
	template='UserInfo/mypost.html'
	query=request.GET.get('q')
	results=request.user.blogs_set.filter(title__icontains=query)
	text='No posts matched your search for "'+query+'"'
	context={'blogs':results,'text':text}
	return render(request,template,context)

def search2(request):
	template='UserInfo/starred.html'
	query=request.GET.get('q')
	results=request.user.starred_set.filter(blog__title__icontains=query)
	text='No posts matched your search for "'+query+'"'
	context={'blogs':results,'text':text}
	return render(request,template,context)

class BlogsListView(LoginRequiredMixin,generic.ListView):
	model=Blogs
	template_name='Blogs/home.html'
	context_object_name='blogs'
	ordering=['-date']

class BlogsDetailView(LoginRequiredMixin,generic.DetailView):
	model=Blogs

class BlogsCreateView(LoginRequiredMixin,generic.CreateView):
	model=Blogs 
	fields=['title','description']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class BlogsUpdateView(LoginRequiredMixin,UserPassesTestMixin, generic.UpdateView):
	model=Blogs
	fields=['title','description']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		form=self.get_object()
		if self.request.user== form.author :
			return True
		return False

class BlogsDeleteView(LoginRequiredMixin,UserPassesTestMixin, generic.DeleteView):
	model=Blogs
	success_url='/'

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False

