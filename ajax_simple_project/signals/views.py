from django.http import HttpResponse
from django.views.generic import View
# Create your views here.


class SignalView(View):
    def get(self, request):
        return HttpResponse("<h1> sadasd </h1>")
