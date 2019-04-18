from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from database import models
from functools import wraps

from public_function_blog import *

#用户登录函数
import random
show=''

def login(request):
    global  show

    if request.method=='POST':
        name1=request.POST.get('uname')
        password1=request.POST.get('upwd')
        asdn2=request.POST.get('pid')
        # next_url = request.GET.get("next")
        print(name1,password1)
        try:
            user=models.Account.objects.get(name=name1)

        except Exception:
            return render(request, 'account/login.html', {'show': show, "res_str":"用户名不存在,请重新输入"})

        if user.password==password1 and asdn2==show:

            # if next_url:
            #     res = redirect(next_url)
            # else:


            # 得到响应对象
            res = redirect('/account')
            print('1*' * 10, user.id)
            # 设置cookie
            res.set_cookie("isLogin","True",max_age = 60 * 60 * 24 * 345 )
            res.set_cookie("uname",name1,max_age = 60 * 60 * 24 * 345)
            res.set_cookie("uid",user.id,max_age = 60 * 60 * 24 * 345)
            return res


        else:
            # return render(request, 'account/login.html', {'show': show})
            return redirect('/account/login')

    else:
        if show!='':
            show=''

        for i in range(4):
            res = str(random.randint(0, 9))
            show += res
        #
        # res = request.COOKIES.get("isLogin")
        #
        # uname = request.COOKIES.get("uname")
        # uid = request.COOKIES.get('uid')
        # if "uname" in request.COOKIES and res == "True":
        #     return redirect("/account/account/")
        # else:
        return render(request, 'account/login.html', {'show': show})

#登录后进入此函数
@login_check
def account(request):
    if request.method=='GET':
        uid=request.COOKIES.get('uid')
        account_obj=models.Account.objects.get(id=uid)

        category_objs = account_obj.category_set.all().order_by("orderNo")  # 给侧边栏和网页主体用

        # 获取分组对应文章数量
        artical_counts = article_counts_category(request)

        artc_obj=account_obj.article_set.all().order_by('create_date').reverse()
        artc_obj=artc_obj[0:10]

        # print(artc_obj)
        return render(request, 'account/account.html', {'artc_obj':artc_obj,
                                                        'account_obj':account_obj,
                                                        'request': request,
                                                        'category_objs':category_objs,
                                                        'artical_counts':artical_counts
                                                        })

#  注销cookies
def logout(request):
    # 如何删除Cookie
    rep = redirect("/")
    rep.delete_cookie("isLogin")
    rep.delete_cookie("uid")
    rep.delete_cookie("uname")
    # rep.delete_cookie("is_login")
    return rep

#用户注册函数
import random
showw = ''
def signup(request):
    # error=''
    global  showw

    if request.method=='POST':
        name1=request.POST.get('uname')
        password1=request.POST.get('upwd1')
        password2 = request.POST.get('upwd2')
        asdn1=request.POST.get('asdn')
        gender1 = request.POST.get('gender1')
        email3 = request.POST.get('email3')
        hobby3 = request.POST.get('hobby3')
        des = request.POST.get('des')



        if password1==password2 and asdn1==showw:

            models.Account.objects.create(name=name1,password=password1,
                                          hobby=hobby3,description=des,
                                          gender=gender1,email=email3,)

            return redirect('/account/login')
        else:
            # error='请重新输入'
            return render(request, 'account/signup.html', {'showw':showw})

    else:
        if showw != '':
            showw = ''
        for i in range(4):
            res = str(random.randint(0, 9))
            showw += res
        print('a'*10,'点击注册')
        return render(request, 'account/signup.html', {'showw':showw})

#修改个人信息的函数
@login_check
def profile(request):
    if request.method=='POST':
        uid = request.COOKIES.get('uid')
        name1 = request.POST.get('uname')
        gender1 = request.POST.get('gender1')
        email3 = request.POST.get('email3')
        hobby3 = request.POST.get('hobby3')
        des = request.POST.get('des')

        blogg_obj = models.Account.objects.get(id=uid)
        flag=True
        name_err='False'
        email_err='False'
        if models.Account.objects.filter(name=name1).exclude(name=blogg_obj.name).exists():
            name_err='用户名重复,未修改用户名'
            flag=False
        else:
            blogg_obj.name = name1

        if models.Account.objects.filter(email=email3).exclude(email=blogg_obj.email).exists():
            email_err='邮箱重复,未修改邮箱'
            flag = False
        else:
            blogg_obj.email = email3

        blogg_obj.gender=gender1
        blogg_obj.hobby=hobby3
        blogg_obj.description=des

        blogg_obj.save()
        if flag:
            return redirect('/account/profile')
        else:
            return redirect('/account/profile?name_err={}&email_err={}'.format(name_err,email_err))
            # return redirect('/account/profile',{"name_err":name_err,
            #                                     'email_err':email_err
            #                                     })

    else:
        uid=request.COOKIES.get('uid')

        name_err=request.GET.get('name_err','False')
        email_err=request.GET.get("email_err",'False')


        category_objs = models.Category.objects.filter(account_id=uid).order_by("orderNo")  # 给侧边栏和网页主体用
        # 获取分组对应文章数量
        artical_counts = article_counts_category(request)



        blogg=models.Account.objects.get(id=uid)
        return render(request, 'account/profile.html', {'category_objs':category_objs,
                                                        'artical_counts':artical_counts,
                                                        'blogg':blogg,
                                                        'request':request,
                                                        'name_err':name_err,
                                                        "email_err":email_err
                                                        })

@login_check
def password(request):
    if request.method=='POST':
        ide=request.COOKIES.get('uid')
        upwd=request.POST.get('upwd')
        upwd1=request.POST.get('upwd1')
        upwd2 = request.POST.get('upwd2')

        mysert_obt=models.Account.objects.get(id=ide)
        if mysert_obt.password==upwd and upwd1==upwd2:
            mysert_obt.password=upwd1
            mysert_obt.save()
            return redirect('/account')

        else:
            return redirect('/account')


    else:
        uid=request.COOKIES.get('uid')
        category_objs = models.Category.objects.filter(account_id=uid).order_by("orderNo")  # 给侧边栏和网页主体用
        # 获取分组对应文章数量
        artical_counts = article_counts_category(request)


        mysert_obj=models.Account.objects.get(id=uid)
        return render(request, 'account/password.html', {'mysert_obj':mysert_obj,
                                                         'request': request,
                                                         'category_objs': category_objs,
                                                         "artical_counts":artical_counts
                                                         })
@login_check
def friendInfos(request):
    id = request.GET.get('user_id')
    # 获取对应id的account属性
    account_objs = models.Account.objects.get(id=id)
    # 查询id对应的文章,并显示其中的前十条
    art_objs= account_objs.article_set.all().order_by('create_date').reverse()
    art_objs = art_objs[0:10]
    print(account_objs)
    print('$'*100)
    print(art_objs)
    category_objs = account_objs.category_set.all().order_by("orderNo")  # 给侧边栏和网页主体用
    print(category_objs)

    # 获取分组对应文章数量
    artical_counts = article_counts_category(request,uid=id)
    print(artical_counts)

#     print(id)ss

    return render(request,'account/friendInfos.html',{"account_objs":account_objs,
                                                       "request":request,
                                                       "art_objs":art_objs,
                                                       "category_objs":category_objs,
                                                       "artical_counts":artical_counts


                                                       })






