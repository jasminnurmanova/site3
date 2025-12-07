from .views import home_page,markazlar_func,detail_markazlar,create_markaz,update_markaz
from django.urls import path

urlpatterns=[
    path('',home_page,name='home_page'),
    path('markazlar/<int:pk>',markazlar_func,name='markazlar'),
    path('details/<int:pk>', detail_markazlar, name='details'),
    path('markaz_create', create_markaz, name='create'),
    path('markaz_update/<int:pk>', update_markaz, name='update')

]