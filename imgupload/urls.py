from django.urls import path
from . import views

urlpatterns = [
    path('img_upload', views.ImageAdd.as_view(success_url='/img_list'), name='images-upload'),
    path('img_list', views.ImageList.as_view(), name='images-list'),
]
