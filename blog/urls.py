from django.urls import path
from .views import BlogCreateView,BlogView


urlpatterns = [
	path("create/",BlogCreateView.as_view(),name="create-blog"),
	path("",BlogView.as_view(),name="blog-home"),
	path("<int:id>/",BlogView.as_view(),name="blog-detail"),
]