from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Private


def register(request):
	if request.method =="POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'Your Account Has Been Created,Kindly Login With Your Credential')
			return redirect('login')
		else :
			messages.failure(request, f'Something went wrong try again ')
			return redirect('register')

	form=UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})




@login_required
def profile(request):
	return render(request, 'users/profile.html')


@login_required
def private(request):
	context={
	'private_posts':Private.objects.all()
	}
	return render(request, 'users/private.html', context)
'''
class PostListView(ListView):
	model=Post 
	template_name = 'users/private.html'
	context_object_name = 'posts'
	ordering= ['-date_posted']
	
class PostDetailView(DetailView):
	model=Private 
'''