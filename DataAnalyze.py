import xlwt
import os
import Network


class Visitor:
    uin = '木有找到QQ号'
    sex = '未知'
    comment = 0
    like = 0
    isFriend = False
    nickname = '木有查询到'

    def __init__(self, uin, sex='未知'):
        self.uin = uin
        self.sex = sex

    def __lt__(self, other):
        return self.like > other.like

    def spideInfo(self):
        dic = Network.getUserInfo(self.uin)
        self.sex = dic['gender']
        self.nickname = dic['nickname']
        self.isFriend = bool(dic['isFriend'])


Item = ['QQ号', 'Nickname', '点赞数', '评论数', '是否是好友', '性别']


class Sheet:
    def __init__(self):
        self.users = []

    def append(self, vis):
        self.users.append(vis)

    def writeToExcel(self):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("INFO")
        pos = 0
        for i in Item:
            sheet.write(0, pos, i)
            pos += 1
        col = 1
        self.users.sort()
        for i in self.users:
            i.spideInfo()
            sheet.write(col, 0, i.uin)
            sheet.write(col, 1, i.nickname)
            sheet.write(col, 2, i.like)
            sheet.write(col, 3, i.comment)
            sheet.write(col, 4, "Yes" if i.isFriend else 'No')
            sheet.write(col, 5, i.sex)
            col += 1
        if not os.path.exists('result'):
            os.mkdir('result')
        workbook.save('result/Result.xls')
