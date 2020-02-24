from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('new',views.new,name='new'),
    path('create',views.create,name='create'),
    path('detail/<int:post_id>',views.detail,name='detail'),
    path('delete/<int:post_id>',views.delete,name='delete'),
    path('edit/<int:post_id>',views.edit,name='edit'),
    path('update/<int:post_id>',views.update,name='update'),
    path('search',views.search,name='search'),

]