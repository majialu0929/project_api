from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
import uuid
# from execute.models import *
# from Common.Common_task import *
from .models import *
from Common.Common_task import *
from Common.requests import *
from Common.Common_api import *
from Common.assertapi import *

"""
问题：
1.case_id；还有interface_id和自动生成的id是不是一个字段
测试查询
from execute.models import *
stu = Environments.objects.filter(id = 1)
stu.values()

stepId = 1
stepData = Interface_Case.objects.filter(id=stepId).values("interface_id",'case_name')[0]

case_id = 1
case_name = "接口_01"
step_list_data=Interface_Case.objects.filter(interface_id=case_id,status=1,case_name=case_name).values("id","case_name")
step_list_data=Interface_Case.objects.filter(interface_id=case_id）


interface = "1"
data = Interface_Case.objects.get(interface_id=interface)
step_list_data=Interface_Case.objects.filter(interface=interface)

interface_name = 1
data=Interface_Case.objects.filter(interface_name=interface_name,status=1).values("id","case_name")
data=Interface_Case.objects.filter(interface_name=interface_name,status=1)

"""


# http://127.0.0.1:8000/execute/httpapi/
def httpapi_views(request):
    try:
        ret = http(method=method,url=url,params={},headers=header)
        print(type(ret))  #<class 'tuple'>
        responseJson = ret[0]   #<class 'dict'>
        print(responseJson)
        # status_code = ret[1]   #200

        # filenumber = 0
        carry_assert(assert_response, responseJson)
        judge(assert_response)

        return  HttpResponse('ok')
    except Exception as e:
        print("没有链接上")
        print(e)

# 调接口
# 执行
# 校验：
# 报告
# LOG

# 接口拼接

def execute_views(request):
    stepId = 1 # stepId = request.POST.get("id")  # 用例id,（首先要有用例信息）
    task_name = "debug"  # 任务名：debug
    env_desc = 'ceshi_host'  # env_desc = request.POST.get("env_desc") #环境名称

    newUuid = str((uuid.uuid1()))
    task_nameUuid = task_name + "---" + newUuid  # 根据uuid自动生成debug--uuid编号名称


    # 获取旧uuid:<QuerySet [{'uuid': 'mayun'},{'uuid': 'mayun'}]>
    oldUuidList = Task.objects.filter(task_name=task_name).values("uuid")
    # 删除任务目录以及文件
    for oldUuid in oldUuidList:
        rm_task(task_name + "---" + oldUuid['uuid'])
        Task.objects.filter(task_name=task_name).delete()


    #创建数据和脚本
    # 1.注意case_id
    stepData = Interface_Case.objects.filter(id=stepId).values("interface_name", 'case_name')[0]#查出=stepId 的测试案例信息：对应第几个接口+测试用例名称
    case_ids=[]
    case_ids.append(stepData['interface_name'])

    # 创建任务表
    create_task(case_ids, task_name, "", newUuid)

    # 创建对应目录 ：测试案例及测试报告
    testcasedir = crate_task(task_nameUuid)
    # 整合数据：读取接口信息+测试案例信息整合
    get_py_data(case_ids, testcasedir, task_name,case_name=stepData['case_name'])





    return HttpResponse("OK")


