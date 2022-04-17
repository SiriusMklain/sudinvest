from django.shortcuts import render
from .models import InvestPost
from forms.forms import *
from django.core.paginator import Paginator


def projects(request):
    form = FeedBackForm(request.POST)
    form_lite = FeedBackLite(request.POST)
    posts = InvestPost.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'posts': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'form': form,
        'form_lite': form_lite
    }

    return render(request, 'project/projects.html', context=context)


