from django.urls import path
from .views import BlogView, BlogPostView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
	path('', BlogView.as_view(), name='blog'),
	path('blog_post/<int:pk>', BlogPostView.as_view(), name='blog_post'),
	path('add_post', AddPostView.as_view(), name='add_post'),
	path('blog_post/update/<int:pk>', UpdatePostView.as_view(), name='update_post'),
	path('blog_post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post')
]