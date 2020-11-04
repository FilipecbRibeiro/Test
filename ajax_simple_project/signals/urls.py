from django.urls import path
from .views import SignalView

app_name = 'signal'

urlpatterns = [
    path('', SignalView.as_view(), name='sign'),
]
