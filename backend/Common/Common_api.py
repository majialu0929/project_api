assert_response={'code': {'assertEqual': '200'}, 'result': {'assertRegexpMatches': '成功'},'A':{'assertGreater':'4'}}
# assert_response = {'': {'': ''}}
url = 'https://api.apiopen.top/searchAuthors?name=李白'
method = 'get'
header = {
        'Content-Type': 'application/json',
        'charset': 'charset=UTF-8'
    }
data ={}


"""

1.批量执行接口，勾选多个接口，加循环（取对应的api+host）
2.1个接口内，加循环(取几个测试案例，案例名称/ID/案例信息)
3.调执行接口，request+断言+日志+输出
# 

储存数据：
4.1 成功的接口还是失败的接口哪里加统计？ 断言里面添加

"""







