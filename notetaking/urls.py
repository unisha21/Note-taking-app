# notetaking/urls.py
from django.urls import path
from .views import note_list, note_detail, note_new, note_edit, note_delete, register, user_login, user_logout

urlpatterns = [
    path('', note_list, name='note_list'),
    path('note/<uuid:pk>/', note_detail, name='note_detail'),  # Updated pattern to accept UUID
    path('note/new/', note_new, name='note_new'),
    path('note/<uuid:pk>/edit/', note_edit, name='note_edit'),  # Updated pattern to accept UUID
    path('note/<uuid:pk>/delete/', note_delete, name='note_delete'),  # Updated pattern to accept UUID

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
