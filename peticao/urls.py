from django.urls import path

from peticao import views

urlpatterns = [
    path('', views.PeticaoListView.as_view(), name='peticoes'),
    path('<int:pk>/', views.PeticaoUpdateView.as_view(), name='peticao'),
    path('create/', views.PeticaoCreateView.as_view(), name='peticao_create'),
    path('delete/<int:pk>/', views.PeticaoDeleteView.as_view(), name='peticao_delete'),

]
