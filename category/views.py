from django.shortcuts import render,redirect,HttpResponse

# import sys
# sys.path.append('..')

# Create your views here.

from database import models

def category_list(request):
    category_obj=models.Category.objects.all()
    category_objs = models.Category.objects.all()
    print(category_obj)
    print(request.path_info)
    return render(request,"category/category_list.html",{"category_objs":category_objs,
                                                         "request":request,
                                                         "categorys":category_obj,
                                                         })

def category_edit(request):
    if request.method=='GET':
        category_objs = models.Category.objects.all()
        edit_id=request.GET.get('id')
        category_obj=models.Category.objects.get(id=edit_id)
        return render(request,'category/category_edit.html',{ "category_objs":category_objs,
                                                              "category_obj":category_obj,
                                                            })
    if request.method=='POST':
        edit_id=request.POST.get('id')
        new_description=request.POST.get('category_description')
        category_obj = models.Category.objects.get(id=edit_id)
        category_obj.description=new_description
        category_obj.save()
        return redirect('/category/category_list/')

def category_add(request):
    if request.method=='GET':
        category_objs = models.Category.objects.all()
        return render(request,'category/category_add.html',{"category_objs":category_objs})
    if request.method == 'POST':
        # add_id = request.POST.get('id')
        add_description = request.POST.get('category_description')
        models.Category.objects.create(description=add_description)
        return redirect('/category/category_list/')

def category_dele(request):
    dele_id=request.GET.get("id")
    category_obj = models.Category.objects.get(id=dele_id)
    category_obj.delete()
    return redirect('/category/category_list/')

