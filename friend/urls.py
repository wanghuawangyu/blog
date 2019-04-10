from django.conf.urls import url
from friend import views

urlpatterns = [
    url(r'friend_list/', views.friend_list),

]