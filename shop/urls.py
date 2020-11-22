from django.contrib import admin
from django.urls import path
from . import views
app_name="shop"
urlpatterns = [
    path("",views.basepage),
    path("company/",views.companyListView.as_view(),name="company"),
    path("companyview/<int:code>/",views.company_view,name="company_view" ),
    path("shop/",views.shopListView.as_view(),name="shop"),
    path('shop/<int:code>',views.shop_view,name='shopview'),
    path('404/',views.error, name='error'),
    path('about/',views.about,name='about'),
    path('salessite/',views.salessiteListView.as_view(),name='salessite'),
    path('salessite/<int:code>/',views.salessite_view,name='salessiteview'),


    #test
   path('fuck/',views.fuck,name='fuck')
]
