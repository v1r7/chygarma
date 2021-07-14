from django.views.generic import TemplateView, ListView

from apps.verse.models import Verse, Author


class IndexView(TemplateView):
    model = Verse
    template_name = 'pages/index_page.html'




class VerseListView(ListView):
    queryset = Verse.objects.all()

    print(queryset)

class AuthorListView(ListView):
    template_name = 'pages/control_panel.html'
    model = Author
    context_object_name = 'authors_page'

# class WorksView(TemplateView):
#     template_name = 'pages/works.html'


class AuthorsView(TemplateView):
    template_name = 'pages/desktop.html'



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


