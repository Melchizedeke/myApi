from django.urls import path, include
from . import views


urlpatterns = [
    path('persons/', views.personsList, name='person-list'),
    path('persons/<int:id>', views.personDetailView, name='person-detail')
]
