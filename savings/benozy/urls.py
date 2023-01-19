from django.urls import path
from . import views

urlpatterns = [
    path('saving-details/<int:pk>', views.SavingDetail.as_view(), name='savings_details'),
    path('history/', views.History.as_view(), name='history')
]
