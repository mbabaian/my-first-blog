# from django.conf.urls import url
# from . import views
# from django.shortcuts import render, get_object_or_404

# urlpatterns = [
#     url(r'^$', views.post_list, name='post_list'),
#     url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
# ]

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]