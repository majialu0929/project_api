from django.db import models

# Create your models here.


# 环境表（sys_environment）
class Environments(models.Model):
    # id = models.AutoField(primary_key=True)
    # environment_key = models.CharField(max_length=50, verbose_name="环境key")
    # address = models.CharField(max_length=100, verbose_name="环境地址")
    # content = models.CharField(max_length=225, verbose_name="说明")

    protocol = models.CharField(max_length=20,default="http")
    env_ip = models.CharField(max_length=20)
    env_host = models.CharField(max_length=40)
    env_port = models.CharField(max_length=10)
    env_desc = models.CharField(max_length=100) #唯一，环境名称

    #     定义表名
    class Meta:
        db_table = 'sys_environment'

    def __str__(self):
        return self.env_ip


# 项目表（sys_project）
class Projects(models.Model):
    # id = models.AutoField(primary_key=True)
    # project_id = models.CharField(max_length=50,verbose_name="项目id")
    project_name = models.CharField(max_length=100,verbose_name="项目名称")
    content = models.CharField(max_length=225,verbose_name="说明")
    status = models.BooleanField(verbose_name="状态")

#     定义表名
    class Meta:
        db_table = 'sys_project'

    def __str__(self):
        return self.project_name


# 模块表（sys_model）
class Models(models.Model):
    # id = models.AutoField(primary_key=True)
    # project_id = models.CharField(max_length=50, verbose_name="项目id")
    # model_id = models.CharField(max_length=50, verbose_name="模块id")
    Project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name="项目名")
    model_name = models.CharField(max_length=100,verbose_name="模块名称")
    content = models.CharField(max_length=225, verbose_name="说明")
    Testers=models.CharField(max_length=100,blank=True,verbose_name="测试人员")
    Developer = models.CharField(max_length=100,blank=True,verbose_name="开发人员")
    status = models.BooleanField(verbose_name="状态")

    #     定义表名
    class Meta:
        db_table = 'sys_model'

    def __str__(self):
        return self.model_name


# 接口信息表（interface）
class Interfaces(models.Model):
    # id = models.AutoField(primary_key=True)
    # project_id = models.CharField(max_length=50, verbose_name="项目id")
    # model_id = models.CharField(max_length=50, verbose_name="模块id")
    # interface_id = models.CharField(max_length=50, verbose_name="接口id")
    Project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name="项目名")
    Modules = models.ForeignKey(Models, on_delete=models.CASCADE,verbose_name="模块名")
    interface_name_en = models.CharField(max_length=100,verbose_name="接口英文名称") #api
    interface_name_zh = models.CharField(max_length=100, verbose_name="接口中文名称") #自定义得接口名称
    request_way = models.CharField(max_length=5, verbose_name="请求方式")
    relation = models.CharField(max_length=500, verbose_name="依赖接口")
    delete_flag = models.CharField(max_length=5, verbose_name="删除标志")
    create_user = models.CharField(max_length=100, verbose_name="创建用户")
    modify_user = models.CharField(max_length=100, verbose_name="修改用户")
    content = models.CharField(max_length=225, verbose_name="说明")
    # 增补字段
    # version = models.CharField(max_length=20)
    # interface_weights = models.IntegerField(default=0)


    #     定义表名
    class Meta:
        db_table = 'interface'


    def __str__(self):
        return self.interface_name_zh


# 接口header表（interface_header）：header是固定值
class Interface_Header(models.Model):
    # id = models.AutoField(primary_key=True)
    interface_name = models.ForeignKey(Interfaces, on_delete=models.CASCADE, verbose_name="接口名")
    head_key = models.CharField(max_length=50, verbose_name="headKey")

    #     定义表名
    class Meta:
        db_table = 'interface_header'





# 接口入参表（interface_param）
class Interface_Param(models.Model):
    # id = models.AutoField(primary_key=True)
    # interface_id = models.CharField(max_length=50, verbose_name="接口id")
    interface_name = models.ForeignKey(Interfaces, on_delete=models.CASCADE, verbose_name="接口名")
    param_key = models.CharField(max_length=50, verbose_name="入参key")
    param_type = models.CharField(max_length=5, verbose_name="入参类型") #text/file等类型
    #     定义表名
    class Meta:
        db_table = 'interface_param'



# 用例入参表（interface_case_param）：1个key存储1条记录
class Interface_Case_Param(models.Model):
    # id = models.AutoField(primary_key=True)
    # case_id = models.CharField(max_length=50, verbose_name="用例id")
    # interface_id = models.CharField(max_length=50, verbose_name="接口id")
    interface_name = models.ForeignKey(Interfaces, on_delete=models.CASCADE, verbose_name="接口名")
    param_key = models.CharField(max_length=5, verbose_name="入参key")
    param_value = models.CharField(max_length=100, verbose_name="入参值")
    create_user = models.CharField(max_length=225, verbose_name="创建用户")
    modify_user = models.CharField(max_length=225, verbose_name="修改用户")

    #     定义表名
    class Meta:
        db_table = 'interface_case_param'








# 用例信息表（interface_case）
class Interface_Case(models.Model):
    # id = models.AutoField(primary_key=True)
    # interface_id = models.CharField(max_length=50, verbose_name="接口id")
    # case_id = models.CharField(max_length=50, verbose_name="用例id")
    # case_id = models.ForeignKey(Interface_Case_Param, on_delete=models.CASCADE,verbose_name="用例id")
    interface_name = models.ForeignKey(Interfaces, on_delete=models.CASCADE,verbose_name="接口名")
    case_name = models.CharField(max_length=50, verbose_name="用例名称")
    case_type = models.CharField(max_length=100, verbose_name="用例分类")
    check_type = models.CharField(max_length=100, verbose_name="校验分类") #枚举类型，比如数据库校验等
    header_1 = models.CharField(max_length=100, verbose_name="header1") #当请求头是动态传值得时候
    header_2 = models.CharField(max_length=100, verbose_name="header2")
    check_key = models.CharField(max_length=5, verbose_name="校验关键字") #去key值，如code,message
    check_condition = models.CharField(max_length=100, verbose_name="校验条件") #属于断言分类
    check_value = models.CharField(max_length=100, verbose_name="预期值")
    action_condition = models.CharField(max_length=225, verbose_name="执行条件") #同时1条数据多个值校验得时候，多个结果是且/或得关系
    create_user = models.CharField(max_length=225, verbose_name="创建用户")
    modify_user = models.CharField(max_length=225, verbose_name="修改用户")
    status = models.BooleanField()
    case_weights = models.IntegerField(default=0)
    # update_time = models.DateTimeField(auto_now=True)
    # create_time = models.DateTimeField(auto_now_add=True)
    # stepCount = models.IntegerField(default=0)
    # version = models.CharField(max_length=20)
    # api = models.CharField(max_length=100)

    #     定义表名
    class Meta:
        db_table = 'interface_case'

    def __str__(self):
        return self.case_name



# 接口执行表（interface）:以接口得维度/类似于统计分析总表StatisticsData
class Interface_Action(models.Model):
    # id = models.AutoField(primary_key=True)
    # project_id = models.CharField(max_length=50, verbose_name="项目id")
    Project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name="项目名")
    batch_no = models.CharField(max_length=50, verbose_name="执行批次号")
    environment_key = models.CharField(max_length=50, verbose_name="环境key")
    interface_action = models.CharField(max_length=225, verbose_name="执行的接口")
    interface_aciton_succcess = models.CharField(max_length=225, verbose_name="成功的接口")
    interface_aciton_fail = models.CharField(max_length=225, verbose_name="失败的接口")
    create_user = models.CharField(max_length=100, verbose_name="创建用户")

    #     定义表名
    class Meta:
        db_table = 'interface_action'

# 接口执行详情表（interface_action_detail） ：以用例得维度
class Interface_Action_Detail(models.Model):
    # id = models.AutoField(primary_key=True)
    # interface_id = models.CharField(max_length=50, verbose_name="接口id")
    interface_name = models.ForeignKey(Interfaces, on_delete=models.CASCADE, verbose_name="接口名")
    batch_no = models.CharField(max_length=50, verbose_name="执行批次号")
    case_id = models.CharField(max_length=50, verbose_name="用例id")
    param_in = models.CharField(max_length=225, verbose_name="入参")
    param_out = models.CharField(max_length=225, verbose_name="出参")
    check_key = models.CharField(max_length=50, verbose_name="校验关键字")
    check_condition = models.CharField(max_length=10, verbose_name="校验条件")
    check_value = models.CharField(max_length=225, verbose_name="预期值")
    action_condition = models.CharField(max_length=10, verbose_name="执行条件")
    out_value = models.CharField(max_length=225, verbose_name="实际返回值")
    create_user = models.CharField(max_length=100, verbose_name="创建用户")


    #     定义表名
    class Meta:
        db_table = 'interface_action_detail'



#任务表
class Task(models.Model):
    # Interfaces接口外键
    interface_name=models.ForeignKey(Interfaces,on_delete=models.CASCADE, verbose_name="接口名")
    task_name = models.CharField(max_length=200,verbose_name="任务名") #唯一
    uuid = models.CharField(max_length=200, default="")
    out_id = models.CharField(max_length=200, default="")
    carryId = models.IntegerField(default=0)
    task_run_time_regular = models.CharField(max_length=100,verbose_name="定时")
    ip=models.CharField(max_length=40,default="",verbose_name="Environments的ip")
    Nosqldb = models.CharField(max_length=40,default="")
    db = models.CharField(max_length=40,default="")
    email = models.CharField(max_length=40,default="",verbose_name="eaail的id")
    failcount = models.CharField(max_length=40,default="",verbose_name="执行失败次数")
    remark = models.CharField(max_length=200,verbose_name="任务备注")
    Nosqldb_desc = models.CharField(max_length=400,default="")
    db_remark = models.CharField(max_length=100, default="",verbose_name="db的备注")
    env_desc = models.CharField(max_length=100, default="",verbose_name="Environments的备注")
    subject = models.CharField(max_length=100, default="",verbose_name="email的标题名")
    status = models.BooleanField()
    carrystatus = models.IntegerField(default=2)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    #     定义表名
    class Meta:
        db_table = 'task'


    def __str__(self):
        return self.task_name


#第几次执行任务
class CarryTask(models.Model):
    task_name = models.CharField(max_length=200,verbose_name="任务名")
    htmlreport = models.CharField(max_length=200, default="")
    successlogname = models.CharField(max_length=200, default="")
    errorlogname = models.CharField(max_length=200, default="")
    stepcountall = models.IntegerField(default=0)
    stepcountnow = models.IntegerField(default=0)
    out_id = models.CharField(max_length=200, default="")
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)


    #     定义表名
    class Meta:
        db_table = 'carrytask'

    def __str__(self):
        return self.task_name



#邮件配置表
class Email(models.Model):
    sender=models.CharField(max_length=100,verbose_name="发送人")
    receivers = models.CharField(max_length=100,verbose_name="接收人列表")
    host_dir = models.CharField(max_length=100,verbose_name="邮件主机")
    email_port=models.CharField(max_length=20, default="",verbose_name="邮件发送端口")
    username = models.CharField(max_length=100,verbose_name="用户名")
    passwd = models.CharField(max_length=100,verbose_name="密码")
    Headerfrom = models.CharField(max_length=100,verbose_name="发送人头部信息")
    Headerto = models.CharField(max_length=100,verbose_name="接收人头部信息")
    subject = models.CharField(max_length=100,default="",verbose_name="邮件标题",unique=True) #唯一

    def __str__(self):
        return self.username

    #     定义表名
    class Meta:
        db_table = 'email'

#邮件和日志的反馈
class LogAndHtmlfeedback(models.Model):
    test_step = models.CharField(max_length=100,verbose_name="步骤名")
    test_status = models.IntegerField(verbose_name="测试结果") #1表示成功 0表示接口内部错误500 2 表示断言错误
    test_response = models.CharField(max_length=225,verbose_name="测试返回值的message信息")
    test_carryTaskid = models.CharField(max_length=40,default="",verbose_name="第几次执行") #CarryTask的id
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)