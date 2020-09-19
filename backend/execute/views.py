from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
import uuid
from execute.models import *
from Common.Common_task import *

"""
问题：
1.case_id；还有interface_id和自动生成的id是不是一个字段
测试查询
from execute.models import *
stu = Environments.objects.filter(id = 1)
stu.values()

stepId = 1
stepData = Interface_Case.objects.filter(id=stepId).values("interface_id",'case_name')[0]
"""


# execute/ceshi/
def ceshi_views(request):
    print("测试接口")
    return HttpResponse('OK')


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
    stepData = Interface_Case.objects.filter(case_id=stepId).values("interface_id", 'case_name')[0]#查出=stepId 的测试案例信息：对应第几个接口+测试用例名称
    case_ids=[]
    case_ids.append(stepData['interface_id'])

    # 创建任务表
    create_task(case_ids, task_name, "", newUuid)

    # 创建对应目录 ：测试案例及测试报告
    testcasedir = crate_task(task_nameUuid)
    # # 整合数据：读取接口信息+测试案例信息整合
    # get_py_data(case_ids, testcasedir, task_name,case_name=stepData['case_name'])
    #




    return HttpResponse("OK")


