from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^create/$', views.PostCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.PostUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.PostDeleteView.as_view(), name='delete'),
]
