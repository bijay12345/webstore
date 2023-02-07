from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import register,profile,ReviewApi

urlpatterns=[
	path("login/",LoginView.as_view(template_name="users/login.html"),name="login"),
	path("logout/",LogoutView.as_view(template_name="users/logout.html"),name="logout"),
	path("register/",register,name="register"),
	path("profile/",profile,name="profile"),
	path('review/',ReviewApi.as_view(),name="review")
]