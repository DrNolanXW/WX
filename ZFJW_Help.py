# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-10 下午 5:50'

import datetime
import re

class Schedule:

    def __init__(self):
        self.index = 0
        self.course_name = []
        self.course_teacher = []
        self.course_time = []
        self.course_position = []
        self.weekday_index = ''
        self.week_day_dict = {
            0: u'周一',
            1: u'周二',
            2: u'周三',
            3: u'周四',
            4: u'周五',
            5: u'周六',
            6: u'周天',
        }

        # 放置当天课程的引索，对应self.course_name的index
        self.day_couser_index = []


    def read_schedule(self):
        f = open("schedule1.txt","r")
        lines = f.readlines()

        self.index = 0

        # 将数据分出
        for line in lines:
            line = line.strip('\n')
            if self.index % 4 == 0:
                 self.course_name.append(line)
            if self.index % 4 == 1:
                 self.course_time.append(line)
            if self.index % 4 == 2:
                 self.course_teacher.append(line)
            if self.index % 4 == 3:
                 self.course_position.append(line)
            self.index += 1

    def is_odd(self):
        # 判断是否为双周
        d1 = datetime.datetime.now()
        d2 = datetime.datetime(2017, 2, 27)
        self.weekday_index = d1.weekday()
        if (d1 - d2).days % 14 >= 0 and (d1 - d2).days % 14 < 7:
            return False
        else:
            return True

    def get_day_schedule(self):
        # 放置当天课程
        day_couser = []

        # 如果为目前该周为双周则 not_week_type取单周
        if self.is_odd():
            not_week_type = u"单周"
        else:
            not_week_type = u'双周'

        week_day_pat = self.week_day_dict[self.weekday_index]

        index = 0
        if self.weekday_index == 5 or self.weekday_index == 6:
            code = 0
            data = dict()
            data['code'] = 0
            data['course_name'] = ''
            data['course_position'] = ''
            data['course_time'] = ''
            day_couser.append(data)
            return day_couser,code

        for time in self.course_time:
            if re.match(week_day_pat, time.decode("UTF-8")):
                if not re.search(not_week_type,time.decode("UTF-8")):
                    self.day_couser_index.append(index)
            index += 1

        not_course_pat = u'计算机编程新技术'
        for couser_index in self.day_couser_index:
            if not re.match(not_course_pat, self.course_name[couser_index].decode("UTF-8")):
                data = dict()
                data['code'] = 1
                data['course_name'] =  self.course_name[couser_index]
                data['course_position'] = self.course_position[couser_index]
                data['course_time'] = self.course_time[couser_index]
                day_couser.append(data)

        code = 1
        return day_couser,code


if __name__ == '__main__':
    schedule = Schedule()
    schedule.read_schedule()
    data = schedule.get_day_schedule()
    for course in data:
        print course['course_name']


