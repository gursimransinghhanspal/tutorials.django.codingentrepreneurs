from django.shortcuts import render

from .forms import SignUpForm


# Create your views here.
def home(request):
	title = 'Welcome'
	if request.user.is_authenticated:
		title = 'Hello {:s}'.format(str(request.user))

	context = {
		'title': title,
		'form': SignUpForm(request.POST or None)
	}
	return render(request, "home.html", context)
