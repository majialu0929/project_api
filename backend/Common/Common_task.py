import os,shutil
from execute.models import *


#删除任务目录以及文件
def rm_task(task_name):
    #if os.name == 'nt':
    task_dir=os.getcwd()+r"/task/"+task_name
    if os.path.exists(task_dir):
        shutil.rmtree(task_dir)

#创建任务表(case_ids:列表里面是案例关联的接口ID + task_name=“debug”+ remark="" +  UUID)
#取接口信息值：接口名称，api
# 2.注意：接口表内的id 与 interface_id
def create_task(case_ids,task_name,remark,UUID):
    for case_id in case_ids:
        case_data=Interfaces.objects.filter(interface_id=case_id).values("interface_name_zh","interface_name_en")[0] #接口内得信息：接口名称+接口信息
        # 得到外键数据
        interfaces = Interfaces.objects.get(interface_id=case_id)  #case:接口名称
        Task.objects.create(task_name=task_name,uuid=UUID,interfaces=interfaces,remark=remark,status=0)

# 判断一个夹是否存在，不存在创建
def create_dir(dir):
    isexist = os.path.isdir(dir)
    if not isexist:
        os.mkdir(dir)
    else:
        pass

# 创建一个文件
def create_file(filename):
    with open(filename, "w") as fp:
        fp.close()


#判断是不是windows,在task目录下创建本次任务目录，再创建case
# task/task_name/report和testcase(__init__.py)
# task_name=task_nameUuid(debug--uuid编号名称)
def crate_task(task_name):
    if os.name=='nt':
        task_dir=os.getcwd()+r"\task"
        task_name=task_dir+r"/"+task_name
        testcase=task_name+r"\testcase"
        report=task_name+r"\report"
    else:
        task_dir = os.getcwd() + r"/task"
        task_name = task_dir + r"/" + task_name
        testcase = task_name + r"/testcase"
        report = task_name + r"/report"
    create_dir(task_name)
    create_dir(testcase)
    create_dir(report)
    #创建一个初始化文件__init__.py
    filename=testcase+"/__init__.py"
    create_file(filename)
    return testcase

#用例生成脚本，结合接口信息
#case_id:接口id  testcasedir：测试案例地址dubug-uuid  task_name:debug  step_name:测试案例名称
def get_py_data(case_ids,testcasedir,task_name,case_name=None):
    # #插入任务表的db和db_remark
    # db=set([])
    # db_remark=set([])
    str=','
    for case_id in case_ids:
        # 获取接口名称+接口api+接口描述信息
        interface_data=Interfaces.objects.filter(id=case_id).values("interface_name_zh","interface_name_en","content")[0]
        # 得到外键数据
        interface = Interfaces.objects.get(id=case_id)
        print(interface)

        # if case_name:
        #     step_list_data=Interface_Case.objects.filter(interface=interface,status=1,case_name=case_name).values("id","case_name")
        #     print(step_list_data)
        # else:
        #     step_list_data = Step.objects.filter(case=case, status=1).values("id", "step_name",
        #                                                                                           "method", "params",
        #                                                                                           "headers", "files",
    #                                                                                               "assert_response",
    #                                                                                               "api_dependency",
    #                                                                                               "step_desc")
    #     #     step_list_data：添加的测试案例信息id，请求头，断言，请求方式，api关联,案例名称，案例描述等
    #     # step：测试案例名称
    #     for step_data in step_list_data:
    #         #得到外键数据
    #         step = Step.objects.get(id=step_data['id'])
    #         #sql数据
    #         sql_list_data=Sql.objects.filter(step=step,status=1).values("sql_condition","is_select","variable","sql","db","db_remark")
    #         #将数据用到的几个数据库id和连接名写入任务表
    #         for sql_data in sql_list_data:
    #             db.add(sql_data['db'])
    #             db_remark.add(sql_data['db_remark'])
    #
    #         step_data['sql_list_data']=sql_list_data
    #
    #         # Nosql数据
    #         nosql_list_data = NoSql.objects.filter(step=step, status=1).values("Nosql_dataType","Nosql_condition", "is_select", "variable",
    #                                                                        "Nosql")
    #         step_data['sql_list_data'] = sql_list_data
    #         step_data['nosql_list_data'] = nosql_list_data
    #     case_data["step_list_data"]=step_list_data
    #     make_testcase=Make_testcase(testcasedir,case_data)
    #     #print (case_data)
    # # 将数据用到的几个数据库id和连接名写入任务表
    # dbstr=str.join(db)
    # db_remarkstr=str.join(db_remark)
    # Task.objects.filter(task_name=task_name).update(db=dbstr,db_remark=db_remarkstr)
