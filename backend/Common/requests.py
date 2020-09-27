#-*-coding:utf-8-*-
import requests,json
# from public.script_function import *
import datetime,json,re,jsonpath
def echo(*args):  #不限数量的单值参数,请求链接后等到的响应信息没有转换成json格式，记录每条数据创建时间及信息；
    for i in args:
        print ("[time:{asctime}] - INFO : {message}".format(asctime=  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),message=i))

class Http:
    def __init__(self,model):
        self.model=model
    def __request(self,**kwargs):
        if self.model.lower() == "get":
            response = requests.request("get", kwargs["url"], params=kwargs["params"], headers=kwargs["headers"])
            print(response.text)
        # post的参数名要为data
        elif self.model.lower() == "put":
            # 转换成字符串传入
            params = json.dumps(kwargs["params"], ensure_ascii=False).encode()
            response = requests.request("put", kwargs["url"], data=params, headers=kwargs["headers"])
        elif self.model.lower() == "delete":
            # 转换成字符串传入
            params = json.dumps(kwargs["params"], ensure_ascii=False).encode()
            response = requests.request("delete", kwargs["url"], data=params, headers=kwargs["headers"])
        elif self.model.lower() == "postbody":
            # 转换成字符串传入
            params = json.dumps(kwargs["params"], ensure_ascii=False).encode()
            response = requests.request("post", kwargs["url"], data=params, headers=kwargs["headers"])
        elif self.model.lower() == "postform":
            response = requests.request("post", kwargs["url"], data=kwargs["params"], headers=kwargs["headers"])
        elif self.model.lower() == "postfile":
            response = requests.request("post", kwargs["url"], data=kwargs["params"], headers=kwargs["headers"],
                                        files=kwargs["files"])

        print("打印数据")


        return response

    # 文本转换成json字符串
    def __changeJson(self,response,**kwargs):
        try:
            responseJson = json.loads(response.text)
            return responseJson
        except:
            echo(kwargs["url"], self.model, kwargs["headers"], kwargs["params"],
                 '请求返回值为: ' + str(response.text))
            errormessage = '返回值非json格式'
            raise RuntimeError(errormessage)

    def __call__(self,fuc):
        def wrapper(*args,**kwargs):
            fuc(*args, **kwargs)
            response=self.__request(**kwargs)
            responseJson=self.__changeJson(response,**kwargs)
            return responseJson,response.status_code
        return wrapper

@Http(model="GET")
def get(url,params,headers):
    pass

@Http(model="PUT")
def put(url,params,headers):
    pass

@Http(model="DELETE")
def delete(url,params,headers):
    pass

@Http(model="POSTFORM")
def postform(url,params,headers):
    pass

@Http(model="POSTBODY")
def postbody(url,params,headers):
    pass

@Http(model="POSTFILE")
def postfile(url,params,headers,files):
    pass


def http(method,url,params,headers):
    if method=="postbody":
        postbody(url=url, params=params, headers=headers)

    elif method=="get":
        a = get(url=url, params=params, headers=headers)
        print(a)
        return a
    elif method=="put":
        put(url=url, params=params, headers=headers)
    elif method=="delete":
        delete(url=url, params=params, headers=headers)
    elif method=="postform":
        postform(url=url, params=params, headers=headers)




