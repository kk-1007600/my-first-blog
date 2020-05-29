from django.template.defaulttags import url
from django.urls import path, include

import app
from . import views, admin
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

# アプリケーションのルーティング設定

urlpatterns = [
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('', ItemFilterView.as_view(), name='index'),
    path('master/', views.master, name='master'),
    path('edit/<editing_id>', views.edit, name='edit'),
]
