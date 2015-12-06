from django.shortcuts import render_to_response
from blogapp.models import Posts
from blogapp.forms import PostForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse



def login(request):
	auth.logout(request)
	c = {}
	c.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/')
	return render_to_response('login.html', c)


def logout(request):
	auth.logout(request)
	return render_to_response('login.html')	


@login_required(login_url='/login/')
def home(request):
	posts = Posts.objects.all().order_by('-time')[:10]
	return render_to_response('index.html', {'posts' : posts})

@login_required(login_url='/login/')
def create(request):
	if request.POST:
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()	
			return HttpResponseRedirect('/')
	else:
		form = PostForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('create_post.html', args)			

@login_required(login_url='/login/')
def delete(request):
	if request.POST:
		idList = request.POST.getlist("deleteItems")
		for id in idList:
			Posts.objects.get(id=id).delete()
		return HttpResponseRedirect('/delete')	
	posts = Posts.objects.all().order_by('-time')[:10]
	args = {}
	args.update(csrf(request))
 	args['posts'] = posts			
	return render_to_response('delete.html', args)	


