from django.urls import path
from Prophet import views

urlpatterns = [
    path('', views.LearnerListView.as_view(), name='list'),
    path('create/', views.LearnerCreateView.as_view(), name='create'),
    path('<int:pk>/', views.LearnerDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.LearnerUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.LearnerDeleteView.as_view(), name='delete'),
]
