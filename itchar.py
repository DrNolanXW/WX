# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-10 下午 7:10'

import itchat
from itchat.content import *
import datetime
import threading
from ZFJW_Help import Schedule
import time


def time_run(sched_timer = datetime.datetime.now()+ datetime.timedelta(seconds=30)):
    time.sleep(5)
    itchat.send('定时器启动：{0}'.format(sched_timer), toUserName=u'wanxiaoba123')
    flag = 0
    while True:
        now = datetime.datetime.now()
        remind_eat(now)
        if now == sched_timer:
            run_task(sched_timer)
            flag = 1
        else:
            if flag == 1:
                sched_timer = sched_timer + datetime.timedelta(hours= 1)
                flag = 0

def run_task(sched_timer):
    now = datetime.datetime.now()
    if now == sched_timer:
        itchat.send('现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
        time.sleep(3)
       # get_today_course()

def get_today_course():
    schedule = Schedule()
    schedule.read_schedule()
    data,code = schedule.get_day_schedule()
    if code == 0:
        itchat.send('大佬今天没课哟', toUserName=u'wanxiaoba123')
        print u'大佬今天没课哟'
    else:
        itchat.send('大佬今天要上的课有', toUserName=u'wanxiaoba123')
        print u'今天要上的课有'
        for course in data:
            time.sleep(1)
            itchat.send('{0} {1} {2}'.format(course['course_name'],course['course_position'],course['course_time']), toUserName=u'wanxiaoba123')
            print course['course_name'].decode('utf-8')
    del schedule

def remind_eat(now):
    if now.hour == 8 and now.minute == 00 and now.second == 0:
        itchat.send('记得吃早餐呦', toUserName=u'iimCar2')
        itchat.send('来自低配吴彦祖的关怀', toUserName=u'iimCar2')
        itchat.send('信息已发送，现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
        time.sleep(5)
        return
    if now.hour == 12 and now.minute == 20 and now.second == 0:
        itchat.send('记得吃午餐呦', toUserName=u'iimCar2')
        itchat.send('来自低配吴彦祖的关怀', toUserName=u'iimCar2')
        itchat.send('信息已发送，现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
        time.sleep(5)
        return
    if now.hour == 18 and now.minute == 30 and now.second == 0:
        itchat.send('记得吃晚餐呦', toUserName=u'iimCar2')
        itchat.send('来自低配吴彦祖的关怀', toUserName=u'iimCar2')
        itchat.send('信息已发送，现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
        time.sleep(5)
        return
    if now.hour == 24 and now.minute == 0 and now.second == 0:
        itchat.send('晚安呦', toUserName=u'iimCar2')
        itchat.send('来自低配吴彦祖的关怀', toUserName=u'iimCar2')
        itchat.send('信息已发送，现在时间是：{0}'.format(now), toUserName=u'wanxiaoba123')
        time.sleep(5)
        return
    if now.hour == 20 and now.minute == 30 and now.second == 0:
        get_today_course()
        time.sleep(5)
        return



@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])


@itchat.msg_register(TEXT)
def simple_reply(msg):
    print msg['Text']
    if msg["FromUserName"] != '@e2e1ce68718ccfc0e3a3bc4eb388e1703e6b6097554003cfd01d5f243f4e19e4':
        itchat.send('收到信息：{0}'.format(msg['Text']), toUserName=u'wanxiaoba123')

def star_time():
    # 开启多线程时间器
    threads = []
    t1 = threading.Thread(target=time_run,)
    threads.append(t1)
    for t in threads:
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.send('大佬，你的小管家启动了', toUserName=u'wanxiaoba123')
    star_time()
    itchat.run(debug=True)
