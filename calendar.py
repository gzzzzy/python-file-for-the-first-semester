class Calendar:
    # 月份名称
    month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
                  5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September',
                  10: 'October', 11: 'November', 12: 'December'}
    def __init__(self, y, m):
        self.year = y
        self.month = m

    # 判断是否为闰年
    def isLeapYear(self, year):
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False


    # 返回每个月的天数
    def getDayNum(self, month):
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30
        elif self.isLeapYear(self.year):
            return 29
        else:
            return 28


    # 返回距1990年1月1日的天数
    def getTotalDaysFrom1990(self):
        totalDays = 0
        for i in range(1990, self.year):
            if self.isLeapYear(i):
                totalDays += 366

            else:
                totalDays += 365

        for i in range(1, self.month):
            totalDays += self.getDayNum(i)

        return totalDays


    # 返回给定月的1日是星期几，由1990.01.01是星期一推算
    def getMonthStartDay(self):
        return 1 + self.getTotalDaysFrom1990() % 7


    # 返回给定月的名称
    def getMonthName(self):
        return Calendar.month_dict[self.month]

    def title2string(self):
        r = ""
        r += '       '+str(self.getMonthName()) +  '  ' + str(self.year) +  '    \n'
        r += '------------------------------\n'
        r += "Sun\tMon\tTue\tWed\tThu\tFri\tSat"
        return r
    # 打印日历的首部
    def printCalenderTitle(self):
        print(self.title2string())

    def calenderBody2string(self):
        r = ""
        m = self.getMonthStartDay()
        if m != 7:
            for d in range(1, self.getMonthStartDay() + 1):
                r += '\t'
        for dt in range(1, self.getDayNum(self.month) + 1):
            r+=str(dt) + '\t'
            m += 1
            if m % 7 == 0:
                r+=' \n'
        return r
    # 打印日历的正文
    def printCalenderBody(self):
        print(self.calenderBody2string())


# 程序入口函数
def main():
    year = int(input('请输入年:'))
    month = int(input('   请输入月份：'))
    c = Calendar(year, month)
    c.printCalenderTitle()
    c.printCalenderBody()

if __name__ == "__main__":
    main()

