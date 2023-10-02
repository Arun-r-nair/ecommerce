from django.urls import path

from . import views
app_name='shop'
urlpatterns = [
    path('',views.allproduct,name='allproduct'),
    path('<slug:c_slug>/',views.allproduct,name='products_by_category'),
    path('<slug:c_slug>/<slug:Product_slug>/', views.proDetail, name='procatdetail'),

]