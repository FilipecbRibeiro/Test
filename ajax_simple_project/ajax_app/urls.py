from django.urls import path
from .views import FirstPage
from .views import ValidationView
# from .views import validate_username

app_name = 'ajax'

urlpatterns = [
    path("", FirstPage.as_view(), name="first_page"),
    path("validate", ValidationView.as_view(), name="validate")
]
