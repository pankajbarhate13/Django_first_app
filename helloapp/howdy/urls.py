# howdy/urls.py
from django.conf.urls import url
from howdy import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^posts/$', views.PostPageView.as_view()),
	url(r'^posts/(?P<post_id>\d+)/$', views.PostDetailView.as_view())
	# url(r'^posts/(?P<post_id>\d+)/$', 'PostDetailView', name='post_details')
]