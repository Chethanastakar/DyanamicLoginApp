from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def input(request):
    return render(request,'base.html')
def compute(request):
    username=request.GET['t1']
    password=str(request.GET['t2'])
    x=datetime.datetime.now()
    v="pass"
    k=chr(65)
    l=str(ord(k))
    y=str(v.capitalize()+x.strftime("%I%M")+k+l)
    if (password==y):
        return HttpResponse("<html><body><a href='https://timesofindia.indiatimes.com/politics/news'>LOgin is successfull</a></body></html>")
    else:
        z="PASSWORD IS INCORRECT PLEASE TRY AGAIN"
    dict={'username':username,'password':password,'z':z}
    return render(request,'base2.html',context=dict)
