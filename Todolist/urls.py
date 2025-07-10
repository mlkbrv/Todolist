from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('<int:id>/delete',views.delete, name='delete'),
    path('<int:id>/edit',views.edit, name='edit'),
    path('<int:id>/complete',views.complete, name='complete'),
    path('<int:id>/undo',views.undo, name='undo'),
]
