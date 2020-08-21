from django.urls import path
from .views import CodeListView, CodeDetailView, CodeEditView, CodeDeleteView, CodeCreateView

urlpatterns = [
    path('', CodeListView.as_view(), name = 'code_list'),
    path('<int:pk>/', CodeDetailView.as_view(), name = 'code_detail'),
    path('<int:pk>/edit/', CodeEditView.as_view(), name = 'code_edit'),
    path('<int:pk>/delete/', CodeDeleteView.as_view(), name = 'code_delete'),
    path('post/', CodeCreateView.as_view(), name = 'code_post'),
]