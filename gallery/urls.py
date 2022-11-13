from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('create/', views.create_gallery_item, name="create_gallery_item"),
    path('edit/', views.edit_gallery, name="edit_gallery"),
    path('edit/<int:gallery_item_id>', views.edit_gallery_item, name="edit_gallery_item"),
    path('delete/<int:gallery_item_id>', views.delete_gallery_item, name="delete_gallery_item"),
]
