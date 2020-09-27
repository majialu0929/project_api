import os,re


class Make_testcase:
    # interface_data = case_name  整合的测试数据
    def __init__(self,testcasedir,interface_data):
        self.testcasedir=testcasedir
        self.interface_data=interface_data
        self.__getAttributes()
        #self.case_name=case_data['case_name']
        self.filename=self.testcasedir+r"/"+self.interface_name_zh+".py"
        self.__create_testcase()

    # 得到属性
    def __getAttributes(self):
        self.interface_name_zh = self.interface_data['interface_name_zh'] #取接口名称
        self.interface_name_en = self.interface_data['interface_name_en'] #取接口的API
        self.content = self.interface_data['content'] #取接口的描述信息
        print(self.interface_name_zh)
        print("没有写sql")

        """
        self.steplen = len(self.case_data['step_list_data'])
        # 得到每个脚本的sql数
        self.stepSqllen = []
        for i in range(self.steplen):
            self.stepSqllen.append(len(self.case_data['step_list_data'][i]['sql_list_data']))
            # self.step_name=self.case_data['step_list_data']['step_name']
           
        """

    # 生成用例
    def __create_testcase(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as self.testcase: #打开并写入测试案例.py文件
                # 调取__write()方法
                message = self.__write()
                # self.testcase.write(message)
                # self.testcase.close()
        except Exception as e:
            raise e

    # 编写用例内容
    def __write(self):
        try:
            print(self.testcasedir)  # D:\马嘉璐\自动化\新矿建\requestnew - master\task / debug - --5b6d6a52 - fd68 - 11ea - 8139 - 7066551057d0\testcase
            templatedir = os.path.abspath(os.path.join(self.testcasedir, "../../template"))  #D:\WEB\project_api\project_api\backend\task\template

            with open(templatedir, 'r', encoding='utf-8') as self.template: #打开模板
                templatemessage = self.template.read()  #读取模板全部内容
                print("恭喜你，模板读取成功")

                regex = r"\${interface_name_zh}"
                message=self.__replaceVariable(regex,self.interface_name_zh,templatemessage) #替换变量接口名称
                print(message) #读取模板内容

                regex = r"\${content}"
                message = self.__replaceVariable(regex, self.content, message)  #替换变量备注名称

                # regex = r"\${api}"
                # message = self.__replaceVariable(regex, self.api, message)
                #
                # message = self.__replaceStep(message)
                self.template.close()
                return message
        except Exception as e:
            raise e


    #替换变量
    def __replaceVariable(self,regex,variable,message,count=0):
        try:
            message = re.sub(regex, variable, message,count)
        except:
            raise ("替换变量出错")
            message=None
        return message

    # def __replaceStep(self, message):
    #     # 根据step_list_data的长度创建几个step
    #     # for i in range(self.steplen):
    #     #     pass
    #     stepmessage = '''    def test_${step_name}(self):
    #             CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
    #             \'\'\'${step_desc}\'\'\'
    #             step_name="${step_name}"
    #             newVariableObj = {}
    #             sqlDatalist=${sqlDatalist}
    #             nosqlDatalist=${nosqlDatalist}
    #             api_dependency=${api_dependency}
    #             #查找接口依赖数据
    #             search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
    #             #追加替换变量字典
    #             newVariableObj.update(search_mongo_result)
    #
    #             #sql和nosql初始化执行自定义函数
    #             nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
    #             sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
    #
    #             #前置nosql的执行
    #             newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,0,newVariableObj)
    #             #前置sql的执行
    #             makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist,0,newVariableObj)
    #
    #             params=\'\'\'${params}\'\'\'
    #             params=json.loads(params)
    #             headers=${headers}
    #
    #             # params和headers初始化执行自定义函数
    #             params=replace_function(self.transferfunction,params)
    #             headers=replace_function(self.transferfunction,headers)
    #
    #             #replace variable
    #             params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
    #             headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
    #
    #             responseJson,status_code=${method}(url=self.url,params=params,headers=headers)
    #             #插入mongodb数据
    #             document={}
    #             document['test_carryid'] = self.transferlogname.test_carryid
    #             document['step_name']=step_name
    #             document['responseJson'] = responseJson
    #             self.transfermongodb.mongodb.insert_one(document)
    #
    #             assert_response=${assert_response}
    #             # assert_response初始化执行自定义函数
    #             assert_response=replace_function(self.transferfunction,assert_response)
    #
    #             #断言nosql的执行
    #             newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,1,newVariableObj)
    #             # 断言sql的执行
    #             makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 1,newVariableObj)
    #
    #             #replace assert_response
    #             assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
    #
    #             way="${way}"
    #
    #             #断言
    #             carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
    #                          self.transferlogname,self.transferlogname.test_carryid)
    #
    #             #后置nosql的执行
    #             carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,2,newVariableObj)
    #             # 后置sql的执行
    #             carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 2,newVariableObj)
    #     '''
    #     message += stepmessage
    #     regexlist = [r"\${step_name}", r"\${step_name}", r"\${step_desc}", r"\${params}", r"\${headers}", r"\${method}",
    #                  r"\${way}", r"\${assert_response}", r"\${sqlDatalist}", r"\${nosqlDatalist}",
    #                  r"\${api_dependency}"]















