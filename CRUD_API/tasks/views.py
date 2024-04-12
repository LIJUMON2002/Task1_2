from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import User
import json

def user_list(request):
    users = User.objects.all()
    data = [{'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age} for user in users]
    return render(request,'list.html',{'users' : data})
    

def create_user(request):
    if request.POST: 
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        if not name or not email or not age:
            return HttpResponse('error')
        user = User(name=name,email=email,age=age)
        user.save()
        return redirect('list')
    return render(request,'create.html')


def update_user(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse('User not found')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        user.name = name
        user.email = email
        user.age = age
        user.save()
        return redirect('list')
    return render(request,'create.html',{'user': user})


def delete_user(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse('User not found')
    user.delete()
    return redirect('list')