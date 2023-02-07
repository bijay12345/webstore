from django.shortcuts import render,redirect
from .models import Blog as HBlogs
from rest_framework.views import APIView
from .serializers import BlogSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib import messages

from django.db.models import Count
from django.core.paginator import Paginator



class BlogView(APIView):
	renderer_classes=[TemplateHTMLRenderer]
	def get(self,request,id=None,format=None):
		if id is not None:
			blog=HBlogs.objects.get(id=id)
			serializer=BlogSerializer(blog)
			return Response({"blog":serializer.data,"b_status":"active"},template_name="blog/blog-detail.html")
		blogs=HBlogs.objects.all()
		serializer=BlogSerializer(blogs,many=True)

		paginator=Paginator(serializer.data,10)
		page_number = request.GET.get('page')
		page_obj=paginator.get_page(page_number)


		return Response({"blogs":page_obj,"b_status":"active"},template_name="blog/blogs.html")



class BlogCreateView(APIView):
	def post(self,request,format=None):
		context=dict(request.POST.items())
		image=dict(request.FILES.items())
		data={
		"Title":context.get("Title"),
		"description":context.get("description"),
		"image":image.get("image")
		}
		serializer=BlogSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			messages.success(request,"Successfully Saved")
		else:
			messages.info(request,"Please fill all the details")
		return redirect("blog-home")

