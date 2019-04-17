"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from account import views



urlpatterns = [

    url(r'login', views.login),
    url(r'logout',views.logout),
    url(r'signup', views.signup),
    url(r'account', views.account),
    url(r'profile', views.profile),
    url(r'password', views.password),
    url(r'friendInfos', views.friendInfos),
    url(r'',views.account)

]

