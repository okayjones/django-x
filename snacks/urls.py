from django.urls import path

from .views import SnackListView, SnackDeleteView, SnackCreateView, SnackUpdateView, SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete'),
    path('add/', SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/edit/', SnackUpdateView.as_view(), name='snack_update'),
]