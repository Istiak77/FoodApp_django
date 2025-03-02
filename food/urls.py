from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    # Foods
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # Adding foods
    path('add/', views.CreateItem.as_view(), name='create_item'),
    # Editing foods
    path('update/<int:id>/', views.update_item, name='update_item'),
    # Delete Food
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]