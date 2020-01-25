from django.urls import path
from . import views

urlpatterns = [
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('api/users/<int:pk>', views.message_list)
]