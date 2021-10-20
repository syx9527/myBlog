import json

from django.conf import settings
from django.contrib import auth
from django.db.models import Count
from django.db.models import F
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template

from .models import *


# Create your views here.


def index(request):
    return render(request, "Tale/base.html", {"user": {"username": settings.ALL_USER}})
    # html = '<h1>标题</h1>'
    # return render(request, "test.html", {"html": html})


def about(request):
    article_list = Article.objects.all()

    # return render(request, "blog/index.html", {"article_list": article_list})
    return render(request, "Tale/about.html", )


def other(request, htmlname):
    # article_list = Article.objects.all()
    template_name = f"Tale/{htmlname}"
    # return render(request, "blog/index.html", {"article_list": article_list})
    return render(request, template_name=template_name, )


# 登录
def login(request):
    """登录"""

    if request.is_ajax():
        response = {"user": None, "msg": None, "code": None}
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        # 检验验证码

        user = auth.authenticate(username=user, password=pwd)
        if user:
            auth.login(request, user)  # request.user==当前登录对象
            response['user'] = user.username
            response['code'] = 1

        else:
            response['msg'] = "用户名密码错误!"
            response['code'] = -1

        return JsonResponse(response)

    return render(request, 'login_out/index.html')


# 用户注销

def logout(request):
    auth.logout(request)  # request.session.flush()
    referer_url = request.headers.get("Referer")
    if referer_url:
        return HttpResponseRedirect(referer_url)
    return HttpResponseRedirect("/")


def get_ValidCode_img(request):
    from .utils.validCode import get_valid_code_img

    data = get_valid_code_img(request)

    return HttpResponse(data)


# 注册
def register(request):
    if request.is_ajax():

        response = {"user": None, "msg": "cuowu", "code": None}
        username = request.POST.get("user")

        pwd = request.POST.get("pwd")
        re_pwd = request.POST.get("re_pwd")

        user = UserInfo.objects.filter(username=username).values()
        if not (username and pwd and re_pwd):
            response['msg'] = "字段不允许为空"

        if not user:
            if pwd == re_pwd:
                response['user'] = username

                user_obj = UserInfo.objects.create_user(username=username, password=pwd, )
            else:
                response['msg'] = "两次密码不一致！"

        else:

            response['msg'] = "账户已经存在"
        return JsonResponse(response)


def home_site(request, site_name):
    """
    个人站点视图函数
    """

    user = UserInfo.objects.filter(blog__site_name=site_name).first()

    # 判断用户是否存在
    if not user:
        return render(request, "blog/not_found.html")
    # 查询当前站点对象
    blog = user.blog
    return render(request, "Tale/author.html",
                  {"user": user, "blog": blog, })


# 查询文章列表
def query_article_list(request):
    """
    查询文章列表
    :param request:
    :return:
    """
    if request.is_ajax():

        id = request.POST.get("id")
        name = request.POST.get("name")
        username = request.POST.get("username")

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
                return JsonResponse({"code": 0})
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

        t = get_template("Tale/article_list.html")
        content_html = t.render({'article_list': article_list, })

        response = {"content_html": content_html, "code": 1}

        return JsonResponse(response)


# 获取标签列表
def query_tag_list(request):
    """
    查询文章列表
    :param request:
    :return:
    """
    if request.is_ajax():
        # id = request.POST.get("id")
        # name = request.POST.get("name")

        username = request.POST.get("username")
        response = {"content_html": None, "code": 0}
        if username:
            if username != settings.ALL_USER:
                user = UserInfo.objects.filter(username=username).first()

                # 查询当前站点对象
                blog = user.blog
                userid = user.nid
                nid = blog.nid  # 用作原地跳转标签匹配
                # 查询当前站点的每一个标签名称以及对应的文章数
                tag_list = Tag.objects.values('pk').annotate(c=Count("article")).values("title", "c").filter(
                    blog_id=nid)

            else:
                tag_list = Tag.objects.values('pk').annotate(c=Count("article")).values("title", "c")

            t = get_template("Tale/tag_list.html")
            content_html = t.render({'tag_list': tag_list, })

            response = {"content_html": content_html, "code": 1}

        return JsonResponse(response)


# 获取分类列表
def query_cate_list(request):
    """
    获取分类列表
    :param request:
    :return:
    """
    if request.is_ajax():
        # id = request.POST.get("id")
        # name = request.POST.get("name")
        username = request.POST.get("username")
        response = {"content_html": None, "code": 0}
        if username:
            if username != settings.ALL_USER:

                user = UserInfo.objects.filter(username=username).first()

                # 查询当前站点对象
                blog = user.blog
                userid = user.nid
                nid = blog.nid  # 用作原地跳转标签匹配
                # 查询当前站点的每一个标签名称以及对应的文章数
                cate_list = Category.objects.filter(
                    blog__nid=nid).values("title").annotate(c=Count("Article_category"))
            else:
                cate_list = Category.objects.filter().values("title").annotate(c=Count("Article_category"))

            t = get_template("Tale/cate_list.html")
            content_html = t.render({'cate_list': cate_list, })

            response = {"content_html": content_html, "code": 1}

        return JsonResponse(response)


# 获取归档列表
def query_month_list(request):
    """
    获取归档列表
    :param request:
    :return:
    """
    if request.is_ajax():
        username = request.POST.get("username")

        response = {"content_html": None, "code": 0}
        if username:
            if username != settings.ALL_USER:
                user = UserInfo.objects.filter(username=username).first()

                # 查询当前站点对象
                blog = user.blog
                userid = user.nid
                nid = blog.nid  # 用作原地跳转标签匹配
                # 查询当前站点的每一个标签名称以及对应的文章数
                year_month = Article.objects.filter(user=userid).annotate(month=TruncMonth("create_time")).values(
                    "month").annotate(
                    c=Count(nid)).values("month", 'c')
            else:
                year_month = Article.objects.filter().annotate(month=TruncMonth("create_time")).values(
                    "month").annotate(
                    c=Count('nid')).values("month", 'c')

            t = get_template("Tale/year_month.html")
            content_html = t.render({'year_month': year_month, })

            response = {"content_html": content_html, "code": 1}
        return JsonResponse(response)


def article(request, article_id):
    """文章详情页"""
    # 文章
    article = Article.objects.filter(pk=article_id).first()
    # 所属标签
    tags = article.tags.values().first().get("title")
    # 所属分类
    category = article.category.title
    # 日期
    month = article.create_time.date()
    # 作者信息
    article_author = article.user

    return render(request, 'Tale/single-post-minimal.html',
                  {"article": article, "tags": tags, "category": category, "month": f"{month.year}-{month.month}",
                   "article_author": article_author})


# 处理点赞功能
def dig(request):
    """
    处理点赞功能
    :param request:
    :return:
    """
    if request.is_ajax():
        response = {"state": True, "msg": None}
        # id = request.POST.get("id")
        # is_up = request.POST.get("is_up")  # "true"/"false"
        is_up = json.loads(request.POST.get("is_up"))
        article_id = request.POST.get("article_id")
        user_id = request.user.pk
        if user_id:
            obj = ArticleUpDown.objects.filter(user_id=user_id, article_id=article_id).first()
            if not obj:
                ard = ArticleUpDown.objects.create(user_id=user_id, article_id=article_id, is_up=is_up)
                queryset = Article.objects.filter(pk=article_id)
                if is_up:

                    queryset.update(up_count=F("up_count") + 1)
                else:
                    queryset.update(down_count=F("down_count") + 1)
            else:
                response['state'] = False
                response['handed'] = obj.is_up
        else:
            response['state'] = False
            response['msg'] = "您尚未登录，请先<a href='/login/'>登录</a>"

        return JsonResponse(response)


def query_comment_list(request):
    """
    获取评论
    :param request:
    :return:
    """
    if request.is_ajax():
        article_id = request.POST.get("article_id")
        comment_list = Comment.objects.filter(article_id=article_id)
        t = get_template("Tale/comment.html")
        content_html = t.render({'comment_list': comment_list, "article_id": article_id})

        response = {"content_html": content_html, "code": 1}
        return JsonResponse(response)


def comment(request):
    """
    提交评论
    :param request:
    :return:
    """
    print(request.POST)
    if request.is_ajax():
        article_id = request.POST.get("article_id")
        content = request.POST.get("content")
        pid = request.POST.get("pid")
        user_id = request.user.pk
        comment_obj = Comment.objects.create(user_id=user_id, article_id=article_id, content=content,
                                             parent_comment_id=pid)
    return JsonResponse({"comment": "ok"})


# 用户初始化设置

def default_settings(request):
    if request.is_ajax():
        return JsonResponse({'code': 1})
    return render(request, "Tale/default_settings.html")
