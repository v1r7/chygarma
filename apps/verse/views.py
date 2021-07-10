from django.views.generic import TemplateView, ListView

from apps.verse.models import Verse


class MainView(TemplateView):
    template_name = 'base.html'

class VerseListView(ListView):
    model = Verse
    paginate_by = 6
    def get_queryset(self):
        return Verse.objects.filter(verse__pubdate=self.kwargs.get("-pubdate"))

# class WorksView(TemplateView):
#     template_name = 'pages/works.html'


# class AuthorsView(TemplateView):
#     template_name = 'pages/author.html'
#
#     def get_context_data(self, **kwargs):
#         pass
#
# class VerseView(TemplateView):
#     template_name = 'pages/works.html'
#
#     def get_context_data(self, **kwargs):
#         pass
#
# class DesktopView(TemplateView):
#     template_name = 'pages/desktop.html'
#
#     def get_context_data(self, **kwargs):
#         pass
#


