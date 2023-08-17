from django.urls import path
from . import views

urlpatterns = [
	path('', views.DashboardView.as_view(), name='dashboard'),
	path('<int:pk>/', views.BookDetailView.as_view(), name='detail'),
	path('add', views.addBook, name='add'),
	path('<int:pk>/chapter<int:pk2>/', views.ChapterDetailView.as_view(), name='chapter-detail'),
	path('<int:pk>/add', views.addChapter, name='add-chapter'),
]