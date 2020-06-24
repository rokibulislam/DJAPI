"""
 Create a Module "api" and create an empty file __init__.py in the persons app
 [simple create a folder named "api" and create "__init__.py" file containes nothing. It will help to detect this folder
 as a module by the system]
 Then create views.py file here
 This is done because it's better to separate api's view logic from normal views as well as url patterns
"""
import json  #python's library

from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from persons.models import Person, Post

class CSRFExcemptHandler(object):  #Disable CSRF protection
    @method_decorator(csrf_exempt)
    def dispatch(self,*args, **kwargs):
        return super().dispatch(*args,**kwargs)


class SingleApiView(CSRFExcemptHandler,View):  #Disabled CSRF Protection For Whole Class

    def get_object(self,id=None):
        qs = Post.published.filter(id=id)
        if qs.count() == 1:
            return qs
        return None


    def get(self, request, id, *args, **kwargs): #get single item
        obj = self.get_object(id=id)
        if obj is None:
            reponse = json.dumps({"message":"Not Found"})
            return HttpResponse(reponse, content_type="application/json",status=404)

        response = obj.serialize()
        print(response);
        return HttpResponse(response, content_type="application/json",status=200)

    def post(self, request, *args, **kwargs):
        print(request);
        response = json.dumps({"message":"Not Allowed"})
        return HttpResponse(
             response,
             content_type='application/json',
             status=400
             )
class ListAPIView(CSRFExcemptHandler,View): #Disabled CSRF Protection For Whole Class

    def get(self, request, *args, **kwargs):  #get all items
        qs = Post.published.all()
        response = qs.serialize()

        return HttpResponse(response,  content_type='application/json')