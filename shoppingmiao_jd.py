#!usr/bin/python
# -*- coding: utf-8 -*-
# Author:Reg_coco
# www.qxn110.com
# Wechat: yikunzhu
# 京东专用
from selenium import webdriver
import datetime
import time

#创建浏览器对象
driver = webdriver.Chrome()
#窗口最大化显示
driver.maximize_window()

def login(url,mall):
    '''
    登陆函数
    
    url:商品的链接
    mall：商城类别
    '''
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)
    #京东专用
    if mall=='1':
        #找到并点击京东的登陆按钮
        driver.find_element_by_link_text("你好，请登录").click()
   
    print("请在30秒内完成登录")
    #用户扫码登陆
    time.sleep(30)
    
def buy(buy_time,mall):
    '''
    购买函数
    
    buy_time:购买时间
    mall:商城类别
    
    获取页面元素的方法有很多，获取得快速准确又是程序的关键
    在写代码的时候运行测试了很多次，css_selector的方式表现最佳
    '''
 
    if mall=='1':
        #"立即购买"的css_selector
        btn_buy='#InitCartUrl'
        #"中间到购物车"的css_selector
        btn_goon='#GotoShoppingCart'
        #"立即下单"的css_selector
        btn_order='#cart-floatbar > div > div > div > div.options-box > div.toolbar-right.toolbar-right-new > div.normal > div > div.btn-area > a'
        #"完成下单
        btn_allok='#order-submit'
    while True:
        #现在时间大于预设时间则开售抢购
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')>buy_time:
            try:
                #找到“立即购买”，点击
                if driver.find_element_by_css_selector(btn_buy):
                    driver.find_element_by_css_selector(btn_buy).click()
                    break
                time.sleep(0.1)
            except:
                time.sleep(0.3)

    # while True:
    # #现在时间大于预设时间则开售抢购
    #     if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')>buy_time:
    #         try:
    #             #找到“立即购买”，点击
    #             if driver.find_element_by_xpath(btn_buy):
    #                 driver.find_element_by_xpah(btn_buy).click()
    #                 break
    #             time.sleep(0.1)
    #         except:
    #             time.sleep(0.3)

    while True:
        try:
            #找到“立即下单”，点击，
            if driver.find_element_by_css_selector(btn_goon):
                driver.find_element_by_css_selector(btn_goon).click()
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
            if driver.find_element_by_css_selector(btn_allok):
                driver.find_element_by_css_selector(btn_allok).click()
                #下单成功，跳转至支付页面
                print("购买成功")
                break
        except:
            time.sleep(0.5)


if __name__ == "__main__":
    # url = input("请输入商品链接:")
    # mall = input("请选择商城（淘宝 1  天猫 2  小米有品 3 苏宁易购 4 输入数字即可）： ")
    # bt = input("请输入开售时间【2019-02-15（空格）12:55:50】")
    url = "https://item.jd.com/100009411156.html"
    mall = "1"
    bt = "2020-02-16 16:01:00"
    login(url, mall)
    buy(bt, mall)
