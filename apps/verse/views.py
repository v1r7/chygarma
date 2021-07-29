import json

from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, TemplateView

from apps.verse.models import Verse, Author, AuthorProfile, Comment, News


class headerView(TemplateView):
    template_name = 'pages/base1.html'


class IndexView(TemplateView):
    template_name = 'pages/index_page.html'

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        context['popular_verses'] = Verse.objects.all().order_by('is_liked')[:5]
        context['verse_list'] = Verse.objects.filter(recommend=True).order_by("id")[:5]
        context['author_banner'] = AuthorProfile.objects.all().order_by('readers')[:3]
        context['news'] = News.objects.filter(main_page_filter=True)[:3]
        context['verse_count'] = Verse.objects.all().annotate(answer_count=Count('name'))
        context['author_count'] = Author.objects.filter(author_name__category__verse__isnull=False).annotate\
            (answer_count=Count('author'))

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
    model = Author
    paginate_by = 7
    # context_object_name = 'authors_pag'


    # def get_queryset(self):
    #     context = super(AuthorDetailView, self).get_queryset()
    #     author = context.get('author')
    #     _qs = Verse.objects.filter(author_id=author.id).\
    #         order_by('pubdate')
    #     return _qs

    def get_context_data(self, **kwargs, ):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        author = context.get('author')
        context['author'] = author
        context['detail_author_verses'] = Verse.objects.filter(author_id=author.id).\
            order_by('pubdate')
        context['verse_count'] = Verse.objects.filter(author_id=author.id).\
            annotate(answer_count=Count('name'))
        context['readers_count'] = AuthorProfile.objects.filter(author_id=author.id).\
            annotate(answer_count=Count('readers'))
        context['like_count'] = Verse.objects.filter(author_id=author.id).\
            annotate(answer_count=Count('is_liked'))



        # context['author_verses'] = Verse.objects.all()
        # context['author_profile'] = AuthorProfile.objects.first()
        # author_profile = AuthorProfile.objects.first()
        # context[] = author_profile.readers.count()
        # context['profile_name'] = AuthorProfile.objects.first()
        #
        # context['comments_list'] = Comment.objects.all().order_by('-create_at')

        return context

    # def post(self, request, *args, **kwargs):
    #     data = json.loads(request.body.decode())
    #     user = self.request.user
    #     instance = AuthorProfile.objects.get(id=data.get('author_id'))
    #     instance.readers.add(*[user.id])
    #     instance.save()
    #
    #     return redirect("/")

class AuthorlistView(ListView):
    template_name = 'pages/author_list.html'
    model = Author
    paginate_by = 7
    context_object_name = 'list_of_authors'

    def get_queryset(self):
        _qs = super(AuthorlistView, self).get_queryset()
        return _qs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors_list'] = Author.objects.all().order_by('author')

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
        all_verses_list = self.queryset.filter(name__icontains=data.get('value'))
        context = {'all_verses_list': all_verses_list}
        html = render_to_string(template_name='partials/verse_search_all.html',
                                context=context,
                                request=request)

        return JsonResponse({'html': html}, status=200)


class AllVersesListView(ListView):
    template_name = 'pages/works.html'
    model = Verse
    paginate_by = 7

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["all_verses"] = Verse.objects.all()

        return context

class VerseDetailView(DetailView):
    template_name = 'pages/verse_detail_view.html'
    model = Verse

    def get_context_data(self, **kwargs):
        context = super(VerseDetailView, self).get_context_data(**kwargs)
        context['verse_detail_view'] = Verse.objects.first()
        verse = context.get('verse')
        context['comments'] = Comment.objects.filter(
            verse__id=verse.id
        ).order_by('-create_at')
        # context['verse_likes'] = Verse.objects.filter(verse__id=verse.id).annotate(like_count=Count('is_liked'))
        # print(context)

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())
        verse = Verse.objects.filter(id=data.get('verse_id')).first()

        if verse is None:
            return JsonResponse({'detail': 'error'}, status=404)

        author = Author.objects.filter(author=self.request.user.id).first()

        if author is None:
            return JsonResponse({'detail': 'error'}, status=404)

        Comment.objects.create(
            author=author,
            verse=verse,
            content=data.get('comment'),
        )

        return JsonResponse({'detail': 'success'}, status=201)

    def patch(self, request, *args, **kwargs):
        if request.method == "PATCH":
            data = json.loads(request.body.decode())
            user = self.request.user
            instance = Verse.objects.get(id=data.get('verse_id'))
            instance.is_liked.add(*[user.id])
            instance.save()

            return JsonResponse({'detail': 'success'}, status=201)


class PoliticsView(TemplateView):
    template_name = 'pages/politics.html'


