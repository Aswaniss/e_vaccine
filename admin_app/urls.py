from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_hotel,name='add_hotel'),
    path('view_hotel', views.view_hotel,name='view_hotel'),
    path('hoteldetails/<int:h_id>',views.hoteldetails,name='hoteldetails'),
    path('formupdate/<int:u_id>',views.formupdate,name='formupdate'),
    path('show_index/',views.show_index,name='show_index'),
]
