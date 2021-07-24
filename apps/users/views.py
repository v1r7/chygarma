import json

from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView

from apps.users.forms import LoginForm
from apps.users.models import User
from apps.users.services import authenticate, create_user, check_email

from apps.verse.models import Verse, Author, Category


class LoginView(TemplateView):
    template_name = 'pages/authorization.html'

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode())
        user = authenticate(
            login=data.get('login'), password=data.get('password'),
        )


        if user is None:
            return JsonResponse({'message': 'error'}, status=400)

        login(self.request, user)

        return JsonResponse({'success_url': reverse('index_page')}, status=200)





class RegisterView(TemplateView):
    template_name = 'pages/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['login_form'] = LoginForm()
        context['register_form'] = LoginForm()

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode())

        # if not data.get('pass1') == data.get('pass2'):
        #     return JsonResponse(
        #         {'message': 'Введенные пароли не совподают!', 'status': 400}
        #     )

        if not check_email(data.get('email')):
            return JsonResponse(
                {'message': 'Почта не верна!', 'status': 400},
            )

        user = authenticate(
            login=data.get('login'), password=data.get('password'),
        )

        if user:
            return JsonResponse({
                'message': 'Пользователь уже существует с таким номером',
                'status': 400,
            })

        user = create_user(data)

        if not user:
            return JsonResponse({
                'message': 'По техническим проблемам, '
                           'мы не смогли вас зарегестрировать:(',
                'status': 400,
            })

        login(self.request, user)

        return JsonResponse({
            'message': 'Вы удачно зарегестрировались на сайте!',
            'success_url': reverse('index_page'),
            'status': 200,
        })

class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)

        return HttpResponseRedirect(reverse('index_page'))


class CreateListVerseView(ListView):
    template_name = 'pages/control_panel.html'
    model = Verse

    def get_context_data(self, *args, **kwargs):
        context = super(CreateListVerseView, self).get_context_data(*args, **kwargs)
        context['author_id'] = Author.objects.filter(author=self.request.user).first().id
        context['verses'] = Verse.objects.filter(author__author_id=context.get('author_id'))[:7]
        context['category_list'] = Category.objects.all()

        return context



    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())
        author = Author.objects.filter(id=data.get('author_id')).first()
        Verse.objects.create(
            name=data.get('name'),
            content=data.get('content'),
            author=author,
            tags=data.get('tags'),
            category=data.get('category'),
            # picture=data.get('picture'),
            description=data.get('description')
        )

        return JsonResponse({'detail': 'success'}, status=201)




class UsersListView(ListView):
    model = User
    paginate_by = 3
    template_name = 'pages/index_page.html'
    context_object_name = 'authors_list'