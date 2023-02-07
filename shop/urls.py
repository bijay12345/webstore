from .views import home,about,contact,\
CartApi,productDetail,add_to_cart,remove_from_cart,orderDetail,\
ShopApiView,CheckoutView,remove_single_item_from_cart,LikeView
from django.urls import path


urlpatterns = [
	path("",home,name="home"),
	path("about/",about,name="about"),
	path("contact/",contact,name="contact"),
	path("cart/",CartApi.as_view(),name="cart"),
	path("product/<int:id>/",productDetail,name="detail"),
	path("addToCart/<int:id>/",add_to_cart,name="add_to_cart"),
	path("remove_from_cart/<int:id>/",remove_from_cart,name="remove_from_cart"),
	path("orderDetail/<int:id>/",orderDetail,name="orderDetail"),
	path("shop/",ShopApiView.as_view(),name="shop"),
	path("CheckoutView/",CheckoutView.as_view(),name="checkoutView"),
	path("remove_single_item_from_cart/<int:id>/",remove_single_item_from_cart,name="remove_single_item_from_cart"),
	path("like/",LikeView.as_view(),name="like"),
]
