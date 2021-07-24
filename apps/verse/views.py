import json
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, TemplateView
from apps.verse.models import Verse, Author, AuthorProfile, Category, Comment


class IndexView(TemplateView):
    template_name = 'pages/index_page.html'

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        context['verse_list'] = Verse.objects.filter(recommend=True).order_by("id")[:5]
        context['author_banner'] = Author.objects.order_by("id")[:3]

        return context


class VerseListView(ListView):
    model = Verse
    paginate_by = 7

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verses"] = Verse.objects.all()

        return context


class AuthorDetailView(DetailView):
    template_name = 'pages/author_profile_list.html'
    model = Verse
    context_object_name = 'author_detail'

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['author_profile'] = AuthorProfile.objects.first()
        author_profile = AuthorProfile.objects.first()
        context['readers_count'] = author_profile.readers.count()
        context['profile_name'] = AuthorProfile.objects.first()


        return context


class AuthorlistView(ListView):
    template_name = 'pages/author_list.html'
    model = Author
    context_object_name = 'author_detail'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors_list'] = Author.objects.all()

        return context


class AsyncVerseSearchListView(ListView):
    queryset = Verse.objects.all()

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())
        verse_list = self.queryset.filter(name__icontains=data.get('value'))
        context = {'verses_list': verse_list}
        html = render_to_string(template_name='partials/verses_search.html',
                                context=context,
                                request=request)

        return JsonResponse({'html': html}, status=200)


class AsyncAuthorSearchListView(ListView):
    queryset = Author.objects.all()

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())
        author_search_list = self.queryset.filter(Q(author__first_name__icontains=data.get('value')) |
                                                  Q(author__last_name__icontains=data.get('value')))
        context = {'author_search_list': author_search_list}
        html = render_to_string(template_name='partials/author_search_list.html',
                                context=context,
                                request=request)

        return JsonResponse({'html': html}, status=200)

class AsyncAllVerseSearchListView(ListView):
    queryset = Verse.objects.all()

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())
        print(data)
        all_verses_list = self.queryset.filter(name__icontains=data.get('value'))

        context = {'all_verses_list': all_verses_list}
        html = render_to_string(template_name='partials/verse_search_all.html',
                                context=context,
                                request=request)

        return JsonResponse({'html': html}, status=200)

# class CategoryListView(ListView):
#     queryset = Category.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super(CategoryListView).get_context_data(**kwargs)
#         context['category_list'] = Category.objects.all()
#         print(context)
#
#         return context

class AllVersesListView(ListView):
    template_name = 'pages/works.html'
    model = Verse

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["all_verses"] = Verse.objects.all()[:7]

        return context

class VerseDetailView(DetailView):
    template_name = 'pages/verse_detail_view.html'
    model = Verse

    def get_context_data(self, **kwargs):
        context = super(VerseDetailView, self).get_context_data(**kwargs)
        context['verse_detail_view'] = Verse.objects.first()

        verse = context.get('verse')
        # context['first_picture'] = product.get_first_picture
        context['comments'] = Comment.objects.filter(
            verse__id=verse.id
        ).order_by('-create_at')

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())
        verse = Verse.objects.filter(id=data.get('product_id')).first()

        if verse is None:
            return JsonResponse({'detail': 'error'}, status=404)

        Comment.objects.create(
            author=request.user,
            verse=verse,
            text=data.get('comment'),
        )

        return JsonResponse({'detail': 'success'}, status=201)