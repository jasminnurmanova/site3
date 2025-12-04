from .views import home_page,markazlar_func,detail_markazlar
from django.urls import path

urlpatterns=[
    path('',home_page,name='home_page'),
    path('markazlar/<int:pk>',markazlar_func,name='markazlar'),
    path('details/<int:pk>', detail_markazlar, name='details')

]