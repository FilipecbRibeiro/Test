import json
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.http import JsonResponse
from .models import Utilizador


class FirstPage(CreateView):

    template_name = 'signup.html'
    form_class = UserCreationForm


class ValidationView(View):
    http_method_names = ['post']

    def post(self, request):
        print("cheguei aqui!!!!!")
        response = self.validate_username(request)
        response_content_json = json.loads(response.content)

        if response_content_json['is_taken'] is False:
            Utilizador.objects.create(username=response_content_json['username'])

        return response

    def validate_username(self, request):

        username = request.POST.get('username', None)
        data = {
            'is_taken': Utilizador.objects.filter(username__iexact=username).exists()
        }
        if data['is_taken']:
            data['error_message'] = 'User with this username already exist'
        else:
            data['username'] = username
        return JsonResponse(data)

