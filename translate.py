#coding=utf-8
#autor:katios
#date:2017/5/25

import sys
import requests
import json
import chardet

get_url='https://translate.google.cn/translate_a/single'

data={
"client":"it",
"dt":["t"],
"dj":1,
"q":"",
"ie":"UTF-8",
"sl":"en",
"tl":"zh-CN"
}

headers={
        'user-agent': 'GoogleTranslate',
         }

def translator():
    result = requests.get(get_url, params=data, headers=headers)
    dict_google =json.loads(result.content)
    print "原文： ",dict_google['sentences'][0]['orig']
    print "译文： ",dict_google['sentences'][0]['trans']

if __name__ =='__main__':
    print 'google_translate'
    params = sys.argv
    params_q = ''
    for param in params[1:]:
        if param.isalpha():
            params_q +=param+' '
        else:
            params_q = ''.join(params[1:])
            data['sl'] = 'zh_CN'
            data['tl'] = 'en'
            break
    data['q'] = params_q

    translator()


