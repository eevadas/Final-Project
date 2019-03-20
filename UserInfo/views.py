from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from Blogs.models import Blogs,Starred
# Create your views here.

def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			return render(request,'UserInfo/register.html',{'form':form})
	else:
		form=UserRegisterForm()
		return render(request,'UserInfo/register.html',{'form':form})

@login_required
def profile(request):
	if request.method=='POST':
		userform=UserUpdateForm(request.POST,instance=request.user)
		profileform=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if userform.is_valid() and profileform.is_valid():
			userform.save()
			profileform.save()
			return redirect('profile')

	else:
		userform=UserUpdateForm(instance=request.user)
		profileform=ProfileUpdateForm(instance=request.user.profile)
		context={
		'userform':userform,
		'profileform':profileform
		}
		return render(request,'UserInfo/profile.html',context)
@login_required
def starred(request):
	blogs=request.user.starred_set.all()
	text='You have no Starred posts yet!!!'
	context={'blogs':blogs,'text':text}
	return render(request,'UserInfo/starred.html',context)

@login_required
def myPost(request):
	blogs=request.user.blogs_set.all()
	text='You have not created any posts yet!!!'
	context={'blogs':blogs,'text':text}
	return render(request,'UserInfo/mypost.html',context)

@login_required
def addStar(request,id):
	user=request.user
	b=Blogs.objects.get(pk=id)
	if request.user.starred_set.filter(blog=b).count()==0 :
		x=Starred(person=user,blog=b)
		x.save()
	return redirect('starred')

@login_required
def removeStar(request,id):
	user=request.user
	b=Blogs.objects.get(pk=id)
	request.user.starred_set.filter(blog=b).delete();
	return redirect('starred')
