# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)



# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"



class PostPageView(TemplateView):
	def get(self, request, **kwargs):
		data = Post.objects.all()
		posts = {
		    "post_number": data
		}
		return render(request, 'posts.html', context=posts)


class PostDetailView(TemplateView):
	def get(self, request, **kwargs):
		data = Post.objects.get(id=kwargs['post_id'])
		post = {
			"post_details": data
		}
		return render(request, 'post_details.html', context=post)
