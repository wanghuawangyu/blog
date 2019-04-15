from django.shortcuts import render,redirect,HttpResponse

# import sys
# sys.path.append('..')

# Create your views here.

from database import models

from public_function_blog import *

@login_check
def comment_list(request):
    # 数据库查询
    uid = request.COOKIES.get('uid', '')

    category_objs = models.Category.objects.filter(account_id=uid).order_by("orderNo")  # 给侧边栏和网页主体用

    # 获取我对文章的评论列表
    comment_objs=models.Comment.objects.filter(account_id=uid,comment_type='1').order_by('comment_date')
    # print(comment_objs)
    # for comment in comment_objs:
    #     print(comment.account_id,comment.comment_text)

    # 分页处理
    page_html, comment_objs_slice = page_html_create(request, comment_objs, 9, 10)

    # 获取分组对应文章数量
    artical_counts = article_counts_category(request)

    return render(request,"comment/comment_list.html",{"category_objs":category_objs, #必须要
                                                         "request":request, #必须要
                                                         'artical_counts':artical_counts, #必须要
                                                         "comment_objs_slice":comment_objs_slice, #如果有分页 必须要
                                                         'page_html': page_html #如果有分页 必须要
                                                         })

@login_check
def comment_edit(request):
    pass

@login_check
def comment_add(request):
    print()
    comment_type=1
    comment_text=request.POST.get('comment_text')
    account_id=request.COOKIES.get('uid')
    article_id=request.GET.get("article_id")

    models.Comment.objects.create(
        comment_type=comment_type,
        comment_text=comment_text,
        article_id=article_id,
        account_id=account_id,
    )

    return redirect('/article/article_detail?article_id={}'.format(article_id))


@login_check
def comment_delete(request):
    delete_id=request.GET.get('comment_id')
    delete_comment_obj=models.Comment.objects.get(id=delete_id)
    delete_comment_obj.delete()
    return redirect('/comment/comment_list')

@login_check
def comment_detail(request):
    pass

@login_check
def comment_retry_me(request):
    # 数据库查询
    uid = request.COOKIES.get('uid', '')

    category_objs = models.Category.objects.filter(account_id=uid).order_by("orderNo")  # 给侧边栏和网页主体用

    # 获取我对文章的评论列表
    comment_retry_me_objs=models.Comment.objects.filter(article__account_id=uid,comment_type='1').exclude(account_id=uid).order_by('comment_date')
    # for comment in comment_retry_me_objs:
    #     print(comment.account_id,comment.comment_text)

    # print(comment_retry_me_objs)
    # print(comment_retry_me_objs.count())

    # 分页处理
    page_html, comment_objs_slice = page_html_create(request, comment_retry_me_objs, 5, 10)

    # 获取分组对应文章数量
    artical_counts = article_counts_category(request)

    return render(request,"comment/comment_retry_me.html",{"category_objs":category_objs,
                                                         "request":request,
                                                         'artical_counts':artical_counts,
                                                         "comment_objs_slice":comment_objs_slice,
                                                         'page_html': page_html
                                                         })
