from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from .models import Articles
from .forms import ArticleForm


def home_view(request):
    return render(request, 'home-view.html/')


def article_search_view(request):
    query_dict = request.GET
    #query = query_dict.get("q")
    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Articles.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html",
                  context=context)


def article_detail_view(request, slug=None):
    articles_obj = None
    if slug is not None:
        articles_obj = Articles.objects.get(slug=slug)
        try:
            articles_obj = Articles.objects.get(slug=slug)
        except Articles.DoesNotExist:
            raise Http404
        except Articles.MultipleObjectsReturned:
            articles_obj = Articles.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": articles_obj,
    }
    return render(request, "articles/detail.html",
                  context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        # simplified saving data
        article_object = form.save()
        context['form'] = ArticleForm()

        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # # print(title, content)
        # article_objects = Articles.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True
    return render(request, "articles/create.html", context=context)