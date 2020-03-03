import Network
import Loginfo
import json
import shutil
import os
import threading
import DataAnalyze
import random
import sys
MAX_THREADS = 4
def analyze():
    files = os.listdir('Catch')
    lock = threading.Lock()
    for f in files:
        while len(DataAnalyze.threadpool)>=MAX_THREADS:
            pass
        id = random.randint(1,152522155)
        while id in DataAnalyze.threadpool:id = random.randint(1,152522155)
        #防止线程id重复
        thr = DataAnalyze.Analyze(lock,open('Catch/'+f,'r',encoding='utf-8'),id,f)
        DataAnalyze.threadpool[id] = thr
        thr.start()
    while len(DataAnalyze.threadpool):pass
    visitors = Loginfo.tempTable.values()
    for i in visitors:
        Loginfo.sheet.append(i)
    Loginfo.sheet.writeToExcel()

if len(sys.argv)>1:
    if sys.argv[1] == '-last' or sys.argv[1] == 'last':
        print("开始分析上一次结果")
        analyze()
        print("分析完成")
        exit()


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

if not Network.checkCookieAndRight(uin):
   print("Oooooooooooooooops,权限错误，请检查是否有权访问对方空间或者cookie错误")
   exit()

print("Emmmmmmmm,似乎一切正常开始工作啦")
print("输入爬取说说数量(不限量请输入99999)：")
limit = int(input())+1
cnt = 0
if os.path.exists("Catch"):
    if os.listdir("Catch"):
        print("Catch文件夹不为空，是否清除（Y/N），如只需统计上一次爬取结果，在运行时加入参数-last")
        op = input()
        if op == 'Y':
            shutil.rmtree('Catch')
            os.mkdir('Catch')
        else:
            exit()
else:
    os.mkdir("Catch")
while limit>0:
    try:
        Network.spideToCatch(cnt + 1, min(limit, 20))
        cnt += min(limit, 20) - 1
        limit -= min(limit, 20)
        if limit==0:break
        else : limit+=1
    except Exception as e:
        print("Ooooops,爬取说说时发生了错误:",e)
        exit()
analyze()

print("爬完啦，祝您撩汉成功,爬取了%d条说说"%cnt)
