# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-10 下午 7:10'

import sys
import datetime
import threading
import time

import itchat
from itchat.content import *

from ZFJW_Help import Schedule


#
# def time_run(sched_timer = datetime.datetime.now()+ datetime.timedelta(seconds=30)):
#     time.sleep(5)
#     itchat.send('定时器启动：{0}'.format(sched_timer), toUserName=u'wanxiaoba123')
#     flag = 0
#     while True:
#         now = datetime.datetime.now()
#         remind_eat(now)
#         if now == sched_timer:
#             run_task(sched_timer)
#             flag = 1
#         else:
#             if flag == 1:
#                 sched_timer = sched_timer + datetime.timedelta(hours= 1)
#                 flag = 0
#
# def run_task(sched_timer):
#     now = datetime.datetime.now()
#     if now == sched_timer:
#         itchat.send('现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
#         time.sleep(3)
#        # get_today_course()
#
# def get_today_course():
#     schedule = Schedule()
#     schedule.read_schedule()
#     data,code = schedule.get_day_schedule()
#     if code == 0:
#         itchat.send('大佬今天没课哟', toUserName=u'wanxiaoba123')
#         print u'大佬今天没课哟'
#     else:
#         itchat.send('大佬今天要上的课有', toUserName=u'wanxiaoba123')
#         print u'今天要上的课有'
#         for course in data:
#             time.sleep(1)
#             itchat.send('{0} {1} {2}'.format(course['course_name'],course['course_position'],course['course_time']), toUserName=u'wanxiaoba123')
#             print course['course_name'].decode('utf-8')
#     del schedule
#
# def remind_eat(now):
#     if now.hour == 8 and now.minute == 00 and now.second == 0:
#         itchat.send('记得吃早餐呦', toUserName=u'iimCar2')
#         itchat.send('来自低配吴彦祖的关怀', toUserName=u'iimCar2')
#         itchat.send('信息已发送，现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
#         time.sleep(5)
#         return
#     if now.hour == 12 and now.minute == 20 and now.second == 0:
#         itchat.send('记得吃午餐呦', toUserName=u'iimCar2')
#         itchat.send('来自低配吴彦祖的关怀', toUserName=u'iimCar2')
#         itchat.send('信息已发送，现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
#         time.sleep(5)
#         return
#     if now.hour == 18 and now.minute == 30 and now.second == 0:
#         itchat.send('记得吃晚餐呦', toUserName=u'iimCar2')
#         itchat.send('来自低配吴彦祖的关怀', toUserName=u'iimCar2')
#         itchat.send('信息已发送，现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
#         time.sleep(5)
#         return
#     if now.hour == 24 and now.minute == 0 and now.second == 0:
#         itchat.send('晚安呦', toUserName=u'iimCar2')
#         itchat.send('来自低配吴彦祖的关怀', toUserName=u'iimCar2')
#         itchat.send('信息已发送，现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
#         time.sleep(5)
#         return
#     if now.hour == 20 and now.minute == 30 and now.second == 0:
#         get_today_course()
#         time.sleep(5)
#         return
#
# def star_time():
#     # 开启多线程时间器
#     threads = []
#     t1 = threading.Thread(target=time_run,)
#     threads.append(t1)
#     for t in threads:
#         t.setDaemon(True)
#         t.start()


class WX:

    def __init__(self,gf_wechat = u'iimCar2',self_wechat = u'wanxiaoba123'):
        self.gf_wechat = gf_wechat
        self.self_wechat = self_wechat

    def login(self):
        itchat.auto_login(hotReload=True)
        itchat.send(u'大佬，你的小管家启动了', toUserName=self.self_wechat)

    def  start_thread(self):
        threads = []

        # 线程绑定到time_run函数
        t1 = threading.Thread(target=self.time_run, )
        threads.append(t1)
        for t in threads:
            t.setDaemon(True)
            t.start()

    def time_run(self):
        itchat.send(u'定时器启动：{0}'.format(datetime.datetime.now()), toUserName=self.self_wechat)
        while True:
            self.remind_fun()

    def remind_fun(self):
        self.remind_breakfast()
        self.remind_lunch()
        self.remind_dinner()
        self.remind_all_course()

    def remind_breakfast(self):
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute == 00 and now.second == 0:
            itchat.send(u'记得吃早餐呦', toUserName=self.gf_wechat)
            itchat.send(u'来自低配吴彦祖的关怀', toUserName=self.gf_wechat)
            itchat.send(u'信息已发送，现在时间是：{0}'.format(now), toUserName=self.self_wechat)
            time.sleep(5)
            return

    def remind_lunch(self):
        now = datetime.datetime.now()
        if now.hour == 12 and now.minute == 20 and now.second == 0:
            itchat.send(u'记得吃午餐呦', toUserName=self.gf_wechat)
            itchat.send(u'来自低配吴彦祖的关怀', toUserName=self.gf_wechat)
            itchat.send(u'信息已发送，现在时间是：{0}'.format(now), toUserName=self.self_wechat)
            time.sleep(5)
            return

    def remind_dinner(self):
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute == 00 and now.second == 0:
            itchat.send(u'记得吃晚餐呦', toUserName=self.gf_wechat)
            itchat.send(u'来自低配吴彦祖的关怀', toUserName=self.gf_wechat)
            itchat.send(u'信息已发送，现在时间是：{0}'.format(now), toUserName=self.self_wechat)
            time.sleep(5)
            return

    def good_night(self):
        now = datetime.datetime.now()
        if now.hour == 24 and now.minute == 0 and now.second == 0:
            itchat.send(u'晚安呦', toUserName=self.gf_wechat)
            itchat.send(u'来自低配吴彦祖的关怀', toUserName=self.gf_wechat)
            itchat.send(u'信息已发送，现在时间是：{0}'.format(now), toUserName=self.self_wechat)
            time.sleep(5)
            return

    def remind_all_course(self):
        now = datetime.datetime.now()
        if now.hour == 19 and now.minute == 46 and now.second == 0:
            schedule = Schedule()
            schedule.read_schedule()
            course_data = schedule.get_day_schedule()
            print course_data
            if course_data is None:
                itchat.send(u'大佬今天没课哟', toUserName=self.self_wechat)
            else:
                itchat.send(u'大佬今天要上的课有', toUserName=self.self_wechat)
                for course in course_data:
                    time.sleep(1)
                    print course['course_name']
                    itchat.send(
                        '{0} {1} {2}'.format(course['course_name'], course['course_position'], course['course_time']),
                        toUserName=self.self_wechat)
                    print course['course_name'].decode('utf-8')

    def main(self):
        self.login()
        self.start_thread()
        itchat.run(debug=True)

    @itchat.msg_register(FRIENDS)
    def add_friend(msg):
        itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
        itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

    @itchat.msg_register(TEXT)
    def simple_reply(msg):
        print msg['Text']
        if msg["FromUserName"] != '@e2e1ce68718ccfc0e3a3bc4eb388e1703e6b6097554003cfd01d5f243f4e19e4':
            itchat.send(u'收到信息：{0}'.format(msg['Text']), toUserName=u'wanxiaoba123')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    wx = WX()
    wx.main()
