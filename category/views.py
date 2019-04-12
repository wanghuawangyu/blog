from django.shortcuts import render,redirect,HttpResponse

# import sys
# sys.path.append('..')

# Create your views here.

from database import models




def category_list(request):

    # 数据库查询
    uid=request.COOKIES.get('uid','')
    print('uid',uid)
    category_objs = models.Category.objects.filter(account_id=uid).order_by("orderNo")

    print(category_objs)
    print(request.path_info)

    # 分页处理 开始
    page_num=request.GET.get('page','1')
    page_num = int(page_num)
    if page_num<=0:
        page_num=1
    print(page_num)

    # 每一页显示多少数据
    per_page=10

    # 总页码数
    total_count=category_objs.count()
    totol_page,m=divmod(total_count,per_page)
    totol_page=totol_page if m==0 else totol_page+1

    print(total_count, totol_page, m, '+' * 100)
    # 页面上总共展示多少页码
    max_page=11
    half_max_page=max_page//2

    prev_page=page_num-1 if page_num>=2 else page_num
    next_page=page_num+1 if page_num<totol_page else totol_page

    page_start=page_num-half_max_page
    if page_start<=1:
        page_start=1

    page_end = page_num + half_max_page
    if page_end>=totol_page:
        page_end=totol_page

    if page_num<=half_max_page:
        page_start=1
        # page_end=max_page

    if page_num >=totol_page-half_max_page:
        # page_start = totol_page-max_page+1
        page_end=totol_page
    if page_start==page_end:
        page_end +=1
    print(page_start,page_end,'*'*100)
    # 自己拼接一个分页html代码
    html_str_list=[]
    # 首页
    html_str_list.append('<li><a href="/category/category_list/?page=1">首页</a></li>')
    # 上一页
    html_str_list.append('<li><a href="/category/category_list/?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(prev_page))
    for i in range(page_start,page_end):
        tmp='<li><a href="/category/category_list/?page={0}">{0}</a></li>'.format(i)
        html_str_list.append(tmp)
    # 下一页
    html_str_list.append('<li><a href="/category/category_list/?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(next_page))
    # 尾页
    html_str_list.append('<li><a href="/category/category_list/?page={}">尾页</a></li>'.format(totol_page))
    page_html=''.join(html_str_list)

    category_objs_slice=category_objs[(page_num-1)*10:page_num*10]

    # 分页处理 结束--------------------------------

    artical_counts = []
    for category in category_objs:
        artical_count=category.article_set.filter(account_id=uid).count()
        artical_counts.append(artical_count)


    return render(request,"category/category_list.html",{"category_objs":category_objs,
                                                         "category_objs_slice": category_objs_slice,
                                                         "request":request,
                                                         'artical_counts':artical_counts,
                                                         'page_html': page_html
                                                         })

def category_edit(request):
    uid=request.COOKIES.get('uid','')
    if request.method=='GET':
        category_objs = models.Category.objects.filter(account_id=uid)
        category_edit_id=request.GET.get('category_id')
        category_edit_obj=models.Category.objects.get(account_id=uid,id=category_edit_id)
        return render(request,'category/category_edit.html',{ "category_objs":category_objs,
                                                              "category_edit_obj":category_edit_obj,
                                                              'request':request
                                                            })
    if request.method=='POST':
        category_edit_id=request.POST.get('category_id')
        new_category_name=request.POST.get('category_name')
        new_category_description=request.POST.get('category_description')
        new_category_orderNo=request.POST.get('category_orderNo')
        # print(new_category_name,new_category_description,new_category_orderNo)

        category_obj = models.Category.objects.get(id=category_edit_id,account_id=uid)
        category_obj.name=new_category_name
        category_obj.description=new_category_description
        category_obj.orderNo=new_category_orderNo
        # print(category_obj, category_obj.name, category_obj.description, category_obj.orderNo)
        category_obj.save()
        return redirect('/category/category_list/')

def category_add(request):
    uid = request.COOKIES.get('uid', '')
    if request.method=='GET':
        category_objs = models.Category.objects.filter(account_id=uid)
        return render(request,'category/category_add.html',{"category_objs":category_objs,
                                                            'request': request})
    if request.method == 'POST':
        add_category_name=request.POST.get('category_name')
        add_category_description=request.POST.get('category_description')
        add_category_orderNo=request.POST.get('category_orderNo')

        category_obj=models.Category(name=add_category_name,
                                     description=add_category_description,
                                     orderNo=add_category_orderNo
                                     )
        category_obj.account_id=uid
        models.Category.objects.bulk_create([category_obj], 1)
        return redirect('/category/category_list/')

def category_dele(request):
    uid = request.COOKIES.get('uid', '')
    dele_id=request.GET.get("category_id")
    category_obj = models.Category.objects.get(id=dele_id,account_id=uid)
    category_obj.delete()
    return redirect('/category/category_list/')



def category_login(request):
    res=redirect('/category/')
    res.set_cookie('uid',102,max_age=365*24*3600)
    res.set_cookie('uname',"E0",max_age=365*24*3600)
    res.set_cookie('isLogin',True,max_age=365*24*3600)
    return res

def category_logout(request):
    res=redirect('/category/')
    res.delete_cookie('uid')
    res.delete_cookie('uname')
    res.delete_cookie('isLogin')
    return res

