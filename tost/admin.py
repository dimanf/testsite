from django.contrib import admin
from testsite.tost.models import *


class FirstClassAdmin(admin.ModelAdmin):
	list_display = ('name', 'home')
	class Media:
	    js = [
	        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
	        '/static/grappelli/tinymce_setup/tinymce_setup.js',
	    ]

admin.site.register(FirstClass, FirstClassAdmin)	    