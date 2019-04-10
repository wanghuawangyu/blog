from django.shortcuts import render,HttpResponse

# Create your views here.
import sys
sys.path.append('..')
from database import models

def friend_list(request):
    # return HttpResponse('HELLO')
    return render(request,'friend/friend_list.html')