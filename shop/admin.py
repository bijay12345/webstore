from django.contrib import admin
from .models import Items, Features, Blog,Banner,AboutItems,HomeBanner,Logo,Buttons,FooterInfos,FeedBack,OrderItem,Order,BillingAddress,Rating


class OrderItemAdmin(admin.ModelAdmin):
	list_display=['id',"item","dateadded",'user','ordered']


class OrderAdmin(admin.ModelAdmin):
	list_display=['id','user','ordered']


admin.site.register(Items)
admin.site.register(Features)
admin.site.register(Blog)
admin.site.register(Banner)
admin.site.register(FooterInfos)
admin.site.register(AboutItems)
admin.site.register(HomeBanner)
admin.site.register(Logo)
admin.site.register(Buttons)
admin.site.register(FeedBack)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(BillingAddress)

admin.site.register(Rating)