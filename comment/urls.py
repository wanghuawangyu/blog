from django.conf.urls import url
from comment import views
urlpatterns=[
    url(r'comment_list',views.comment_list),
    url(r'comment_edit',views.comment_edit),
    url(r'comment_add',views.comment_add),
    url(r'comment_delete',views.comment_delete),
    url(r'comment_detail',views.comment_detail),
    # url(r'comment_login',views.comment_login),
    # url(r'comment_logout',views.comment_logout),
    url(r'',views.comment_list)
]