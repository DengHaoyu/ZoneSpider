import urllib
import requests
import re
import Loginfo
import demjson
import HTMLParse

class CookieOutOfDateError(Exception):
    def __init__(self):
        Exception.__init__(self)
    def __str__(self):
        return "Cookie out of date"
baseurl = 'https://user.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_act_all?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
# 我也不知到哪些是有用的，干脆全打上
data = {
    'uin': Loginfo.info.usr,
    'hostuin': Loginfo.info.host,
    'scope': '0',
    'filter': 'all',
    'falg': '1',
    'refresh': '0',
    "firstGetGroup": '0',
    'mixnocache': '0',
    'scene': '0',
    'begintime': 'undefined',
    'icServerTime': '',
    'start': '0',  # 起始下标
    'count': '20',
    'sidomain': 'qzonestyle.gtimg.cn',
    'useutf8': '1',
    'outputhtmlfeed': '1',
    'format': 'jsonp',
    # 这里少了一个r参数
    'g_tk': '1'
}


def loads_jsonp(_jsonp):
    try:
        return demjson.decode(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')


def getUserInfo(uin):
    url = "https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/user/cgi_personal_card?"
    info = {}
    data = {
        'uin': uin,
        'g_tk': str(Loginfo.getg_tk(Loginfo.info.cookie['p_skey'])),
    }
    response = requests.get(url + urllib.parse.urlencode(data),headers = headers,cookies = Loginfo.info.cookie)
    result = loads_jsonp(response.text)
    if 'nickname' in result:
        info['nickname'] = result['nickname']
    else:
        info['nickname'] = "木有查询到"
    if 'isFriend' in result:
        info['isFriend'] = result['isFriend']
    else:
        info['isFriend'] = '没有查询到'
    if 'gender' in result:
        if result['gender'] == 1:
            info['gender'] = 'Boy'
        else:
            info['gender'] = 'Girl'
    else:
        info['gender'] = 'Unknown'
    return info


def spide(start, count):
    data['g_tk'] = str(Loginfo.getg_tk(Loginfo.info.cookie['p_skey']))
    data['start'] = start
    data['count'] = count
    data['uin'] = Loginfo.info.usr
    data['hostuin'] = Loginfo.info.host
    response = requests.get(baseurl + urllib.parse.urlencode(data), headers=headers, cookies=Loginfo.info.cookie)
    res = loads_jsonp(response.text)
    try:
        reda = res['data']['friend_data']
    except KeyError:
        raise CookieOutOfDateError()
    leng = len(reda)
    for i in range(0,leng-1):
        HTMLParse.countLike(reda[i]['html'])
        HTMLParse.countComment(reda[i]['html'])
    return len(res['data']['friend_data'])

def checkCookieAndRight(uin):
    data['g_tk'] = str(Loginfo.getg_tk(Loginfo.info.cookie['p_skey']))
    data['start'] = 0
    data['count'] = 1
    data['uin'] = Loginfo.info.usr
    data['hostuin'] = Loginfo.info.host
    response = requests.get(baseurl + urllib.parse.urlencode(data), headers=headers, cookies=Loginfo.info.cookie)
    res = loads_jsonp(response.text)
    if res['code'] != 0:
        return False
    else:
        return True

