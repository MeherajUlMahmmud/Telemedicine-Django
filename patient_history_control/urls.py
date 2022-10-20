from django.urls import path

from .views import *

urlpatterns = [
    path('patient-history-home/', history_home_view, name='patient-history-home'),
    path('patient-history-home/create/', history_create_view, name='patient-history-create'),
    path('patient-history-home/<int:id>/', history_detail_view, name='patient-history-detail'),
    path('patient-history-home/update/<int:id>/', history_update_view, name='patient-history-update'),
    path('patient-history-home/delete/<int:id>/', history_delete_view, name='patient-history-delete'),
]
