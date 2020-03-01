import Network
import Loginfo
import json

print("欢迎hxy小仙女使用，祝您撩汉成功")
print("请再次确定您的cookie正确并且有效QAQ，不然怪不了我2333")
print("现在先输入你的QQ")
usr = str(input())
print("那么现在开始输入你想撩的人的QQ吧：")
uin = str(input())
print("OK,现在开始工作啦")
Loginfo.info.usr = usr
Loginfo.info.host = uin
print("先检测一下您cookie是否正确233")
try:
    f = open('cookie.txt',"r")
    Loginfo.info.cookie = json.load(f)
except FileNotFoundError:
    print("Ooooooooooooooops,cookie.txt 文件丢失，请检查")
    exit()

# if not Network.checkCookieAndRight(uin):
#     print("Oooooooooooooooops,权限错误，请检查是否有权访问对方空间或者cookie错误")
#     print("如果您连对方空间都进不了，那我就哈哈哈哈哈哈哈哈哈哈")
#     for i in range(1,100):
#         print("疯狂嘲讽哈哈哈哈哈哈哈")
#     exit()

print("Emmmmmmmm,似乎一切正常开始工作啦")
print("输入爬取说说数量(不限量请输入99999)：")
limit = int(input())
cnt = 0
while True:
    print("目前爬取了%d条说说"%cnt)
    try:
        tmp = Network.spide(cnt, min(20,limit))
        limit-=tmp
    except Network.CookieOutOfDateError:
        print("Sorry,发生了错误，cookie可能过期了，请更新cookie，如果多次以后还是不行，请联系dhy")
        print("把已获得的数据储存")
        visitors = Loginfo.tempTable.values()
        for i in visitors:
            Loginfo.sheet.append(i)
        Loginfo.sheet.writeToExcel()
        print("Done,即将退出...")
        exit()
    cnt+=tmp-1
    if tmp<10 or limit<=0:
        break

visitors = Loginfo.tempTable.values()
for i in visitors:
    Loginfo.sheet.append(i)


Loginfo.sheet.writeToExcel()
print("爬完啦，祝您撩汉成功,爬取了%d条说说"%cnt)
