import requests
url = 'http://www.hupu.cn/'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)
#import json
"""def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    From_data={'i':word,'from':'zh-CHS','to':'en','smartresult':'dict','client':'fanyideskweb','salt':'15477056211258','sign':'b3589f32c38bc9e3876a570b8a992604','ts':'1547705621125','bv':'b33a2f3f9d09bde064c9275bcb33d94e','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_REALTIME','typoResult':'false'}
    #请求表单数据
    response = requests.post(url,data=From_data)
    #将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)#
    #打印翻译后的数据
    #print(content['translateResult'][0][0]['tgt'])"""


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
