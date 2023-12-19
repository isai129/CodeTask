from django.shortcuts import render
from login import models  # 导入models文件

# Create your views here.


def index(request):  # 第一个参数必须是request，request参数封装了用户请求的所有内容。
    #  return HttpResponse('hello World!')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #  将数据保存到数据库
        models.UserInfo.objects.create(user=username, pwd=password)

    #  从数据库中读取所有数据，注意缩进
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})
    # 不能直接返回字符串，必须用类封装起来，才能被HTTP协议识别。
    # render方法使用数据字典和请求元数据，渲染一个指定的HTML模板。其多个参数中，第一个参数必须是request，第二个是模板。

