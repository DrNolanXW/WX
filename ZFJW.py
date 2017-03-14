# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-9 上午 11:00'

import codecs
import requests

from bs4 import BeautifulSoup


class ZhengFangSpider:

    def __init__(self,url,txtUserName,TextBox2,RadioButtonList1):
        self.baseUrl = url
        self.url = url + "/default2.aspx"
        # 学号
        self.txtUserName = txtUserName
        # 密码
        self.TextBox2 = TextBox2
        # 登陆界面选项学生，gb2316编码
        self.RadioButtonList1 = RadioButtonList1
        self.txtSecretCode = ''
        self.session = requests.session()

        # 学生信息
        self.student_name = ''
        self.student_xh = ''

    def get_VIEWSTATE(self, html):
        try:
            soup = BeautifulSoup(html,"html.parser")
            VIEWSTATE = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
            return VIEWSTATE
        except Exception, e:
            print u'网络未连接'

    def get_checkcode(self):
        captcha_content = self.session.get('http://jw.jluzh.com/CheckCode.aspx').content
        with open('CheckCode.gif', 'wb') as fp:
            fp.write(captcha_content)
        return raw_input('CheckCode : ')

    def get_student_base_info(self):
        # Referer :"http://jw.jluzh.com/xs_main.aspx?xh=04140226"
        self.session.headers['Referer'] = self.baseUrl+"/xs_main.aspx?xh="+self.txtUserName
        info_url = self.baseUrl+"/xsgrxx.aspx?xh="+self.txtUserName+"&"
        student_info_page = self.session.get(info_url).text
        soup = BeautifulSoup(student_info_page)
        self.student_name = soup.find('span', attrs={'id': 'xm'}).getText()
        self.student_xh = soup.find('span', attrs={'id': 'xh'}).getText()
        student_zyfx = soup.find('span', attrs={'id': 'lbl_zyfx'}).getText()
        student_xb = soup.find('span', attrs={'id': 'lbl_xb'}).getText()
        student_rxrq = soup.find('span', attrs={'id': 'lbl_rxrq'}).getText()
        student_csrq = soup.find('span', attrs={'id': 'lbl_csrq'}).getText()
        student_zkzh = soup.find('span', attrs={'id': 'lbl_zkzh'}).getText()
        student_sfzh = soup.find('span', attrs={'id': 'lbl_sfzh'}).getText()
        print self.student_name,self.student_xh,student_zyfx,student_xb,student_rxrq,student_csrq,student_zkzh,student_sfzh
        print "读取学生基本信息成功"

    def login(self):
        html = self.session.get(self.url).content
        VIEWSTATE = self.get_VIEWSTATE(html)
        code = self.get_checkcode()
        data = {
            "__VIEWSTATE": VIEWSTATE,
            "txtUserName": self.txtUserName,
            "TextBox2": self.TextBox2,
            "txtSecretCode": code,
            "RadioButtonList1": self.RadioButtonList1,
            "Button1": "",
            "lbLanguage": "",
            "hidPdrs": "",
            "hidsc": ""
        }
        print "验证码是：%s" % code
        Loginresponse = self.session.post(self.url, data=data)

    def get_class_schedule(self):
        self.session.headers['Referer'] = self.baseUrl + "/xs_main.aspx?xh=" + self.student_xh
        schedule_url = self.baseUrl + "/xskbcx.aspx?xh=" + self.student_xh + "&xm=" + self.student_name+ "&gnmkdm=N121603"
        class_schedule_page = self.session.get(schedule_url).text
        soup = BeautifulSoup(class_schedule_page)

        # 将课表信息放置在schedule.txt
        with codecs.open('schedule.txt', 'wb', encoding='utf-8')as fp:
            for td in soup.find_all('td',attrs={'rowspan': '2'}):
                str = td.getText('\r\n')
                print str
                fp.write(u'{schedule}\r\n'.format(schedule=''.join(str)))

    def main(self):
        self.login()
        self.get_student_base_info()
        self.get_class_schedule()


if __name__ == '__main__':

    url = "http://jw.jluzh.com"
    # 填写学号
    txtUserName = " "
    # 填写密码
    TextBox2 = " "
    RadioButtonList1 = u"学生".encode('gb2312')
    student = ZhengFangSpider(url, txtUserName, TextBox2, RadioButtonList1)
    student.main()


