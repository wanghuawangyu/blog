from django.conf.urls import url
from category import views
urlpatterns=[
    url(r'category_list',views.category_list),
    url(r'category_edit',views.category_edit),
    url(r'category_add',views.category_add),
    url(r'category_dele',views.category_dele),
    url(r'',views.category_list)
]