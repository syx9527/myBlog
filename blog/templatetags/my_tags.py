from django import template
from django.conf import settings

from blog.models import Article

register = template.Library()


@register.simple_tag
def muilti_tag(x, y):
    """
    模板中直接继承函数返回值
    :param x:
    :param y:
    :return:
    """
    return x * y


@register.inclusion_tag("Tale/article_list.html")
def query_article_list(id, name, username):
    """
    模板继承选然后的html内容
    :param id:
    :param name:
    :param username:
    :return:
    """
    if username != settings.ALL_USER:
        if name == 'tag':
            article_list = Article.objects.filter(user__username=username, tags__title=id)
        elif name == "cate":
            article_list = Article.objects.filter(user__username=username, category__title=id)
        elif name == "month":
            year, month = id.split('-')
            article_list = Article.objects.filter(user__username=username).filter(
                create_time__year=year, create_time__month=month)

        elif name == "all":
            article_list = Article.objects.filter(user__username=username)


    else:

        if name == 'tag':
            article_list = Article.objects.filter(tags__title=id)
        elif name == "cate":
            article_list = Article.objects.filter(category__title=id)
        elif name == "month":
            year, month = id.split('-')
            article_list = Article.objects.filter().filter(
                create_time__year=year, create_time__month=month)
        else:
            article_list = Article.objects.filter()

    return article_list
