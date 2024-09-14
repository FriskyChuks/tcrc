from django.urls import path

from .views import *


urlpatterns = [
    path('image_gallery/', image_gallery, name='image_gallery'),
    path('collection_gallery/', collection_gallery_view, name='collection_gallery'),
    path('image_detail/<image_id>/', image_detail_view, name='image_detail'),
    path('file_uploads/', file_uploads_view, name='file_uploads'),
    path('file_list/', file_list_view, name='file_list'),
]
