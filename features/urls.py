from django.urls import path

from features import views

urlpatterns = [
    path('events/', views.event_list, name='events'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
]
