# Generated by Django 2.2.15 on 2020-09-21 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarryTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200, verbose_name='任务名')),
                ('htmlreport', models.CharField(default='', max_length=200)),
                ('successlogname', models.CharField(default='', max_length=200)),
                ('errorlogname', models.CharField(default='', max_length=200)),
                ('stepcountall', models.IntegerField(default=0)),
                ('stepcountnow', models.IntegerField(default=0)),
                ('out_id', models.CharField(default='', max_length=200)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'carrytask',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100, verbose_name='发送人')),
                ('receivers', models.CharField(max_length=100, verbose_name='接收人列表')),
                ('host_dir', models.CharField(max_length=100, verbose_name='邮件主机')),
                ('email_port', models.CharField(default='', max_length=20, verbose_name='邮件发送端口')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('passwd', models.CharField(max_length=100, verbose_name='密码')),
                ('Headerfrom', models.CharField(max_length=100, verbose_name='发送人头部信息')),
                ('Headerto', models.CharField(max_length=100, verbose_name='接收人头部信息')),
                ('subject', models.CharField(default='', max_length=100, unique=True, verbose_name='邮件标题')),
            ],
            options={
                'db_table': 'email',
            },
        ),
        migrations.CreateModel(
            name='Environments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(default='http', max_length=20)),
                ('env_ip', models.CharField(max_length=20)),
                ('env_host', models.CharField(max_length=40)),
                ('env_port', models.CharField(max_length=10)),
                ('env_desc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sys_environment',
            },
        ),
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_name_en', models.CharField(max_length=100, verbose_name='接口英文名称')),
                ('interface_name_zh', models.CharField(max_length=100, verbose_name='接口中文名称')),
                ('request_way', models.CharField(max_length=5, verbose_name='请求方式')),
                ('relation', models.CharField(max_length=500, verbose_name='依赖接口')),
                ('delete_flag', models.CharField(max_length=5, verbose_name='删除标志')),
                ('create_user', models.CharField(max_length=100, verbose_name='创建用户')),
                ('modify_user', models.CharField(max_length=100, verbose_name='修改用户')),
                ('content', models.CharField(max_length=225, verbose_name='说明')),
            ],
            options={
                'db_table': 'interface',
            },
        ),
        migrations.CreateModel(
            name='LogAndHtmlfeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_step', models.CharField(max_length=100, verbose_name='步骤名')),
                ('test_status', models.IntegerField(verbose_name='测试结果')),
                ('test_response', models.CharField(max_length=225, verbose_name='测试返回值的message信息')),
                ('test_carryTaskid', models.CharField(default='', max_length=40, verbose_name='第几次执行')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, verbose_name='项目名称')),
                ('content', models.CharField(max_length=225, verbose_name='说明')),
                ('status', models.BooleanField(verbose_name='状态')),
            ],
            options={
                'db_table': 'sys_project',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200, verbose_name='任务名')),
                ('uuid', models.CharField(default='', max_length=200)),
                ('out_id', models.CharField(default='', max_length=200)),
                ('carryId', models.IntegerField(default=0)),
                ('task_run_time_regular', models.CharField(max_length=100, verbose_name='定时')),
                ('ip', models.CharField(default='', max_length=40, verbose_name='Environments的ip')),
                ('Nosqldb', models.CharField(default='', max_length=40)),
                ('db', models.CharField(default='', max_length=40)),
                ('email', models.CharField(default='', max_length=40, verbose_name='eaail的id')),
                ('failcount', models.CharField(default='', max_length=40, verbose_name='执行失败次数')),
                ('remark', models.CharField(max_length=200, verbose_name='任务备注')),
                ('Nosqldb_desc', models.CharField(default='', max_length=400)),
                ('db_remark', models.CharField(default='', max_length=100, verbose_name='db的备注')),
                ('env_desc', models.CharField(default='', max_length=100, verbose_name='Environments的备注')),
                ('subject', models.CharField(default='', max_length=100, verbose_name='email的标题名')),
                ('status', models.BooleanField()),
                ('carrystatus', models.IntegerField(default=2)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('interface_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Interfaces', verbose_name='接口名')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100, verbose_name='模块名称')),
                ('content', models.CharField(max_length=225, verbose_name='说明')),
                ('Testers', models.CharField(blank=True, max_length=100, verbose_name='测试人员')),
                ('Developer', models.CharField(blank=True, max_length=100, verbose_name='开发人员')),
                ('status', models.BooleanField(verbose_name='状态')),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Projects', verbose_name='项目名')),
            ],
            options={
                'db_table': 'sys_model',
            },
        ),
        migrations.AddField(
            model_name='interfaces',
            name='Modules',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Models', verbose_name='模块名'),
        ),
        migrations.AddField(
            model_name='interfaces',
            name='Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Projects', verbose_name='项目名'),
        ),
        migrations.CreateModel(
            name='Interface_Param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_key', models.CharField(max_length=50, verbose_name='入参key')),
                ('param_type', models.CharField(max_length=5, verbose_name='入参类型')),
                ('interface_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Interfaces', verbose_name='接口名')),
            ],
            options={
                'db_table': 'interface_param',
            },
        ),
        migrations.CreateModel(
            name='Interface_Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_key', models.CharField(max_length=50, verbose_name='headKey')),
                ('interface_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Interfaces', verbose_name='接口名')),
            ],
            options={
                'db_table': 'interface_header',
            },
        ),
        migrations.CreateModel(
            name='Interface_Case_Param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_key', models.CharField(max_length=5, verbose_name='入参key')),
                ('param_value', models.CharField(max_length=100, verbose_name='入参值')),
                ('create_user', models.CharField(max_length=225, verbose_name='创建用户')),
                ('modify_user', models.CharField(max_length=225, verbose_name='修改用户')),
                ('interface_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Interfaces', verbose_name='接口名')),
            ],
            options={
                'db_table': 'interface_case_param',
            },
        ),
        migrations.CreateModel(
            name='Interface_Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=50, verbose_name='用例名称')),
                ('case_type', models.CharField(max_length=100, verbose_name='用例分类')),
                ('check_type', models.CharField(max_length=100, verbose_name='校验分类')),
                ('header_1', models.CharField(max_length=100, verbose_name='header1')),
                ('header_2', models.CharField(max_length=100, verbose_name='header2')),
                ('check_key', models.CharField(max_length=5, verbose_name='校验关键字')),
                ('check_condition', models.CharField(max_length=100, verbose_name='校验条件')),
                ('check_value', models.CharField(max_length=100, verbose_name='预期值')),
                ('action_condition', models.CharField(max_length=225, verbose_name='执行条件')),
                ('create_user', models.CharField(max_length=225, verbose_name='创建用户')),
                ('modify_user', models.CharField(max_length=225, verbose_name='修改用户')),
                ('status', models.BooleanField()),
                ('case_weights', models.IntegerField(default=0)),
                ('interface_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Interfaces', verbose_name='接口名')),
            ],
            options={
                'db_table': 'interface_case',
            },
        ),
        migrations.CreateModel(
            name='Interface_Action_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=50, verbose_name='执行批次号')),
                ('case_id', models.CharField(max_length=50, verbose_name='用例id')),
                ('param_in', models.CharField(max_length=225, verbose_name='入参')),
                ('param_out', models.CharField(max_length=225, verbose_name='出参')),
                ('check_key', models.CharField(max_length=50, verbose_name='校验关键字')),
                ('check_condition', models.CharField(max_length=10, verbose_name='校验条件')),
                ('check_value', models.CharField(max_length=225, verbose_name='预期值')),
                ('action_condition', models.CharField(max_length=10, verbose_name='执行条件')),
                ('out_value', models.CharField(max_length=225, verbose_name='实际返回值')),
                ('create_user', models.CharField(max_length=100, verbose_name='创建用户')),
                ('interface_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Interfaces', verbose_name='接口名')),
            ],
            options={
                'db_table': 'interface_action_detail',
            },
        ),
        migrations.CreateModel(
            name='Interface_Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=50, verbose_name='执行批次号')),
                ('environment_key', models.CharField(max_length=50, verbose_name='环境key')),
                ('interface_action', models.CharField(max_length=225, verbose_name='执行的接口')),
                ('interface_aciton_succcess', models.CharField(max_length=225, verbose_name='成功的接口')),
                ('interface_aciton_fail', models.CharField(max_length=225, verbose_name='失败的接口')),
                ('create_user', models.CharField(max_length=100, verbose_name='创建用户')),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='execute.Projects', verbose_name='项目名')),
            ],
            options={
                'db_table': 'interface_action',
            },
        ),
    ]
