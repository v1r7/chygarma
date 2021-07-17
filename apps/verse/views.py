from django.template import loader
from django.views.generic import ListView, DetailView, TemplateView

from apps.verse.models import Verse


class IndexView(TemplateView):
    template_name = 'pages/index_page.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verse'] = Verse.objects.filter(recommend=True)

        return context




class VerseListView(ListView):
    model = Verse
    paginate_by = 7

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verses"] = Verse.objects.all()
        print(context)
        return context


class VerseDetailView(DetailView):
    template_name = 'pages/control_panel.html'
    model = Verse
    context_object_name = 'verses_detail'

    # def get_context_data(self, **kwargs):
    #     context = super(VerseDetailView, self).get_context_data(**kwargs)
    #     print('yes')
    #     verse = context.get('verse')
    #     context['first_picture'] = verse.get_first_picture
    #     print(context)
    #     return context







