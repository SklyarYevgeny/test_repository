from django.shortcuts import render, redirect
from .forms import Articles, ArticlesForms
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView


# def home_news(request):
#     news = Articles.objects.order_by('name')
#     return render(request, 'news/home_news.html', {
#         'news': news
#     })

#
# def add_news(request):
#     error = ""
#     if request.method == 'POST':
#         form = ArticlesForms(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('news')
#         else:
#             error = "Ошибка заполения формы, повторите попытку!"
#     form = ArticlesForms()
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'news/create_news.html', data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'articles'


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/article_list'
    template_name = 'news/delete_news.html'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create_news.html'
    form_class = ArticlesForms


class ArticleListView(ListView):
    model = Articles
    queryset = Articles.objects.all()
    template_name = 'news/article_list.html'


class NewsCreateView(CreateView):
    model = Articles
    template_name = 'news/create_news.html'
    form_class = ArticlesForms
    success_url = '/news/article_list'
