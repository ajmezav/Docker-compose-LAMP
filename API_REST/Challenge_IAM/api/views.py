from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Permission
from .models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
import json

# Create your views here.
class PermissionView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        permissions=list(Permission.objects.values())
        if len(permissions)>0:
            data = {'message':"Success",'permissions':permissions}
        else:
            data = {'message':"Permissions not found..."}

        return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Permission.objects.create(name = jd['name'],codename = jd["codename"],content_type_id = jd["content_type_id"])
        data = {'message':"permission created successfully"}

        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        permissions = list(Permission.objects.filter(id=id).values())
        if len(permissions)>0:
            permission = Permission.objects.get(id=id)
            permission.name = jd['name']
            permission.codename = jd['codename']
            permission.content_type_id = jd['content_type_id']
            permission.save()
            data = {'message':"permission updated successfully"}
        else:
            data = {'message':"Permissions not found..."}

        return JsonResponse(data)


class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request):
        users = list(User.objects.values())
        if len(users)>0:
            data = {'message':"Success",'users':users}
        else:
            data = {'message':"Users not found..."}

        return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        ct = ContentType.objects.get_for_model(User)
        permissions = Permission.objects.get(codename = jd['codename'],content_type_id = jd["content_type_id"])
        
        user = User.objects.create(username = jd['username'])
        user.user_permissions.add(permissions)

        data = {'message':"user created successfully"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        permissions = list(Permission.objects.filter(id=id).values())
        if len(permissions)>0:
            permissions = Permission.objects.get(codename = jd['codename'])
            user = User.objects.get(username = jd['username'])
            user.user_permissions.add(permissions)
            user.save()
            data = {'message':"user updated successfully"}
        else:
            data = {'message':"User not found..."}

        return JsonResponse(data)

    def delete(self, request, id):
        jd = json.loads(request.body)
        permissions = list(Permission.objects.filter(id=id).values())
        if len(permissions)>0:
            permissions = Permission.objects.get(codename = jd['codename'])
            user = User.objects.get(username = jd['username'])
            user.user_permissions.remove(permissions)
            user.save()
            data = {'message':"user updated successfully"}
        else:
            data = {'message':"User not found..."}

        return JsonResponse(data)