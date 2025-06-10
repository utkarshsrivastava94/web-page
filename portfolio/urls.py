from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work_portfolio, name='work_portfolio'),
    path('photography/', views.photography_portfolio, name='photography_portfolio'),
    path('photography/<int:category_id>/', views.photo_gallery, name='photo_gallery'),
]

