from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp


# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'timestamp', 'updated']
	form = SignUpForm

	# class Meta:
	# 	model = SignUp
	pass


admin.site.register(SignUp, SignUpAdmin)
