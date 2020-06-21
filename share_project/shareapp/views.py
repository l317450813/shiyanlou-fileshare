import datetime
import json
import random
import string

from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from shareapp.models import Upload

# Create your views here.

class HomeView(TemplateView):
    template_name='base.html'

    def post(self,request):
        if request.FILES:
            file=request.FILES.get('file')
            name=file.name
            size=int(file.size)
            path='shareapp/static/file/'+name
            with open(path,'wb') as f:
                f.write(file.read())
            code=''.join(random.sample(string.digits,8))
            upload=Upload(path=path,name=name,filesize=size,code=code,pcip=str(request.META['REMOTE_ADDR']))
            upload.save()
            return HttpResponsePermanentRedirect('/s/'+code)

class DisplayView(ListView):
    def get(self,request,code):
        uploads=Upload.objects.filter(code=code)
        print(111111111)
        if uploads:
            for upload in uploads:
                upload.downloadcount +=1
                upload.save()

        return render(request,'content.html',{'content':uploads,'host':request.get_host()})
