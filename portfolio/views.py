from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from portfolio.forms import ContactForm
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.conf import settings

from portfolio.models import Portfolio, CategoryPrice
from settings.models import ProfessionalSkills


# Create your views here.


class HomeView(FormView):
    template_name = "portfolio/index-home.html"
    form_class = ContactForm
    http_method_names = ['get','post']

    def post(self,request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject_mail = 'Сообщение с формы Контактов с сайта BackEndDev'
            content_mail = f'Вам отправлено письмо с формы обратной связи сайта BackEndDev\nИмя: {form.cleaned_data["name"]}\nТелефон отправителя: {form.cleaned_data["phone"]}\nТекст сообщения: {form.cleaned_data["message"]}'
            mail = send_mail(subject_mail, content_mail, settings.EMAIL_HOST_USER, [settings.ADMIN_MAIL_ADDRESS],fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
        return TemplateResponse(request, self.template_name , {"form": form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = Portfolio.objects.filter(deleted=False, best=True)[:3]
        context['professionalskills'] = ProfessionalSkills.objects.filter(deleted=False)
        context['price'] = CategoryPrice.objects.all()
        return context



class PortfolioView(DetailView):
    template_name = "portfolio/portfolio-single.html"
    context_object_name = "portfolio"
    model = Portfolio

class PortfolioListView(ListView):
    template_name = "portfolio/portfolio-list.html"
    context_object_name = "portfolio"
    model = Portfolio