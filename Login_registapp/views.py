import os
import random
import string
import time
import uuid

from django.db import transaction
from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
from Login_registapp.captcha.image import ImageCaptcha
from Login_registapp.models import User


def login(request):
    name = request.COOKIES.get('name')
    pwd = request.COOKIES.get('pwd')
    u_user = User.objects.filter(name=name, password=pwd)
    if u_user:
        request.session['login'] = 'ok'
        return redirect('Staffapp:emplist')
    return render(request, 'login.html')  # 登录页面


def regist(request):
    return render(request, 'regist.html')  # 注册页面


def login_l(request):
    username = request.POST.get('name')
    pwd = request.POST.get('pwd')
    rem = request.POST.get('remember')
    number = request.POST.get('number')
    user = User.objects.filter(username=username, password=pwd )
    if user:
        red = HttpResponse("ok")
        if rem:
            red.set_cookie('name', username, max_age=7 * 24 * 60 * 60)
            red.set_cookie('pwd', pwd, max_age=7 * 24 * 60 * 60)
        request.session['login'] = 'ok'
        code_session = request.session.get('code')  # 获取缓存的验证码
        if number.lower() == code_session.lower():  # 判断输入的验证码是否和生成的一致
            return red
        return HttpResponse("验证码输入有误,请重新输入。。。")
    return HttpResponse("error")


def regist_r(request):
    # try:
    with transaction.atomic():
        username = request.POST.get('username')  # 获取h5中用户名框中内容
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        sex = request.POST.get('sex')
        number = request.POST.get('number')
        print(username, name, pwd, sex, number)
        code_session = request.session.get('code')  # 获取缓存的验证码
        if number.lower() == code_session.lower():  # 判断输入的验证码是否和生成的一致
            user = User.objects.create(username=username, name=name, password=pwd, gender=sex)
            if user:
                return HttpResponse("ok")
            return HttpResponse('error')
        return HttpResponse('error')


def checkName(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print("post:", name)
    elif request.method == "GET":
        name = request.GET.get("name")
        print("get:", name)
    user = User.objects.filter(name=name)
    print(user)
    if user:
        return HttpResponse('error')
    return HttpResponse('ok')


def getcapthca(request):
    # 构建一个图片验证码对象
    image = ImageCaptcha()
    # 生成一个随机码
    codes = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 4)
    codes = ''.join(codes)  # 拼接成4位字符串的验证码
    print(codes)
    request.session['code'] = codes  # session 缓存验证码
    data = image.generate(codes)
    return HttpResponse(data, 'image/png')  # 显示验证码


def checkcaptcha(request):
    code = request.GET.get("captcha")
    print(code)
    if (code.lower() == request.session['code'].lower()):
        return HttpResponse("   验证码正确")
    return HttpResponse("   验证码错误")
