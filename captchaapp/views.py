from django.shortcuts import render, HttpResponse
# Create your views here.
import random, string, os
from captchaapp.captcha.image import ImageCaptcha


def getcaptcha(request):
    # 为验证码设置字体 获取当前目录下的xxx目录下的segoesc.ttf文件
    image = ImageCaptcha(fonts=[os.path.abspath("xxx/segoesc.ttf")])
    # 随机码
    # 大小写英文字母+数字，随机抽取5位作为验证码
    code = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 5)
    # 将验证码存入session，以备后续验证
    random_code = "".join(code)
    request.session['code'] = random_code
    # 将生成的随机字符拼接成字符串，作为验证码图片中的文本
    data = image.generate(random_code)
    # 写出验证图片 给客户端
    return HttpResponse(data, "image/png")
