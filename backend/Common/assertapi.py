import unittest
import logging

logger = logging.getLogger(__name__)  # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


# 断言内置方法
def getAssertWay(assertway,assert_content,response_content):
    if assertway=="assertEqual":
        Assertwaymessage="等于"
        try:
            assert assert_content == response_content
            logging.info("{}相等{}，断言成功".format(assert_content,response_content))
        except:
            print("{}不相等{}".format(assert_content,response_content))
            global filenumber
            filenumber +=1


    elif assertway=="assertNotEqual":
        Assertwaymessage="不等于"
        try:
            assert assert_content != response_content
        except:
            print("{}与{}断言错误".format(assert_content,response_content))
            filenumber += 1

    elif assertway=="assertRegexpMatches":
        Assertwaymessage="包含"
        try:
            assert assert_content in response_content
            print("包含")
        except:
            print("{}不包含{}".format(assert_content,response_content))
            filenumber += 1


    elif assertway=="assertNotRegexpMatches":
        Assertwaymessage="不包含"
        try:
            assert assert_content not in response_content
            print("包含")
        except:
            print("{}与{}包含关系断言错误".format(assert_content,response_content))
            filenumber += 1

    elif assertway=="assertGreater":
        Assertwaymessage="大于"
        try:
            assert assert_content > response_content
        except:
            print("{}不大于{}".format(assert_content,response_content))
            filenumber += 1

    elif assertway=="assertGreaterEqual":
        Assertwaymessage="大于等于"
        try:
            assert assert_content >= response_content
        except:
            print("{}与{}大小关系判断错误".format(assert_content,response_content))
            filenumber += 1

    elif assertway=="assertLess":
        Assertwaymessage="小于"
        try:
            assert assert_content < response_content
        except:
            print("{}不小于{}".format(assert_content,response_content))
            filenumber += 1

    elif assertway=="assertLessEqual":
        Assertwaymessage="小于等于"
        try:
            assert assert_content <= response_content
        except:
            print("{}与{}大小关系判断错误".format(assert_content,response_content))
            filenumber += 1

    elif assertway=="assertIn":
        Assertwaymessage="在列表中"
        try:
            assert assert_content in response_content
        except:
            print("{}在{}中".format(assert_content,response_content))
            filenumber += 1


    elif assertway=="assertNotIn":
        Assertwaymessage="不在列表中"
        try:
            assert assert_content not in response_content
        except:
            print("{}不在{}里面".format(assert_content,response_content))
            filenumber += 1

    return Assertwaymessage



filenumber = 0
def carry_assert(assert_response, responseJson):
    print(assert_response)  #{'code': {'assertEqual': '200'}, 'result': {'assertRegexpMatches': '成功'}, 'A': {'assertGreater': '4'}}
    print(responseJson)  #{'code': 200, 'message': '成功!', 'result': '因有人恶意刷接口，导致接口调用频繁，接口已经不能稳定运行，所以计划近期下线，积德吧朋友，如果长期如此，所有接口将面临关闭。'}

    for i in assert_response:  #key
        print(i)

        responseJson_list = list(responseJson.keys()) #keys放到列表中
        print(responseJson_list)
        if i not in responseJson_list:
            print("key错误,值是{}".format(i))
            global filenumber
            filenumber += 1
            print(filenumber)
        else:
            assert_method = list(assert_response[i].keys())[0]
            assert_content = assert_response[i][assert_method]
            response_content = str(responseJson[i])
            getAssertWay(assert_method,assert_content,response_content)



# 每个断言条件之间的关系（and/or）
# 控制开关 且=1 或=0
# 后期传值+接口id+测试用例id 返回结果时XX接口的XX用例执行成功/失败
# 将结果直接存储到两个表中
def judge (assert_response):
    global filenumber
    switch = 1
    assert_response_len = len(list(assert_response.keys()))
    
    if  switch == 1:
        if filenumber >0:
            print("存在断言失败的情况（且），案例执行失败")
        else:
            print("全部断言成功，案例执行成功")

    else:
        if filenumber == assert_response_len:
            print("全部断言失败（或），案例执行失败")
        else:
            print("断言成功，案例执行成功")
