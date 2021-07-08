from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = 'pages/main.html'


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


