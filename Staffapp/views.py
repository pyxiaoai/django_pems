from datetime import datetime
import os
import uuid

from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.urls import reverse

from Login_registapp.models import Staff


def emplist(request):
    time = datetime.now()

    n = request.GET.get('page', 1)
    p1 = request.session.get('page1')
    request.session['page1'] = None
    users = Staff.objects.all()
    pagtor = Paginator(users, per_page=3)
    p = pagtor.num_pages
    page = pagtor.page(n)
    if p1:
        if p1 == 'a' or int(p1) > p:  # 判断当session里的值等于a或当session值大于最大页面将最大页面值传入器前端
            page = pagtor.page(p)
        else:
            page = pagtor.page(p1)  # 如果不是传session值
    return render(request, 'emplist.html', {'page': page})

    # user = Staff.objects.all()
    # n = request.GET.get('number')
    # if n == None:
    #     n = 1
    # pagtor = Paginator(user, per_page=4)  # 每页几项
    # page = pagtor.page(n)  # 获取第几页
    # status = request.session.get('login')
    # if status == 'ok':
    #     return render(request, 'emplist.html', {'page': page})
    # return redirect('emsapp:login')


def updateEmp(request):
    req = request.GET.get('id')
    number = request.GET.get("number")
    user = Staff.objects.get(id=req)
    print(user)
    return render(request, 'updateEmp.html', {'user': user, "number": number})


def addEmp(request):
    return render(request, 'addEmp.html')  # 添加页面


def emplist_e(request):
    return redirect('Staffapp:addEmp')


def u(request):
    number = request.POST.get("num")

    id = request.POST.get('id')
    name = request.POST.get('name')
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    birthday = request.POST.get('birthday')
    headpic = request.FILES.get('headpic')

    print(id, name, salary, age, headpic, number)
    u = Staff.objects.get(pk=id)
    u.Name = name
    u.Salary = salary
    u.Age = age
    u.Birthday = birthday
    if headpic:
        headpic.name = str(uuid.uuid4()) + os.path.splitext(headpic.name)[1]  # 把上传的文件名更改为16进制 和  后缀名
        u.Headpic = headpic
    u.save()
    url = reverse("Staffapp:emplist") + "?page=" + number
    return redirect(url)


# def a(request):
#     return render(request,'a.html')
def a(request):
    try:
        with transaction.atomic():
            name = request.POST.get('name')
            salary = request.POST.get('salary')
            age = request.POST.get('age')
            birthday = request.POST.get('birthday')
            headpic = request.FILES.get('headpic')  # 获取h5中上传文件内容
            rand_name = str(uuid.uuid4()) + os.path.splitext(headpic.name)[1]  # 把上传的文件名更改为16进制 和  后缀名
            headpic.name = rand_name
            print(name, salary, age, birthday, headpic)
            request.session['page1'] = 'a'
            user = Staff.objects.create(Name=name, Age=age, Salary=salary, Birthday=birthday, Headpic=headpic)
            if user:
                return redirect('Staffapp:emplist')
    except:
        return HttpResponse('添加员工失败,请上传头像！')


def delete(request):
    page = request.GET.get('page')
    print(page)
    request.session['page1'] = page
    req = request.GET.get('id')
    Staff.objects.get(id=req).delete()
    return redirect('Staffapp:emplist')


def exit(request):
    response = redirect("emsapp:login")  # 改成重定向等都可以
    response.delete_cookie('name')
    response.delete_cookie('pwd')
    del request.session['login']
    return response
