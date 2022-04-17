"""
To render html web page
"""

import random
from django.http import HttpResponse
from articles.models import Article

from django.template.loader import render_to_string

def home_view(request,  *args, **kwargs):
    random_id = random.randint(1, 3)
    #print(random_id)
    article_obj = Article.objects.get(id=random_id)
    
    article_queryset = Article.objects.all()

    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """

    # """.format(**context)

    return HttpResponse(HTML_STRING)