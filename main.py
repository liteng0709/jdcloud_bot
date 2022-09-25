#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @desc: 京东云路由查看积分，并推送到serve酱
# @author: xin
# @time: 2022/09/16 16:54

from urllib import response
import requests
import os
from sys import argv
import re
import time
import random
import json
import config
from utils.serverchan_push import push_to_wechat


class JDCloud_Bot(object):
    def __init__(self):
        self.session = requests.Session()
        # 添加 headers
        self.session.headers = config.DEFAULT_HEADERS

    def __json_check(self, msg):
        """
        对请求的返回的数据进行进行检查
        1.判断是否 json 形式
        """
        try:
            result = msg.json()
            # print(result)
            return True
        except Exception as e:
            print(f'Error : {e}')
            return False

    def __analysis_data(self, response):
        """
        分析response数据，获取日期和积分
        """

        # 取出响应内容中 "result" 字段的值
        result = response.json()

        # 检查数据返回是否正确
        if (result['code'] != 200):
            return '请求失败:', result

        # 从每台机器里取出当天的积分，并进行汇总
        point_infos = result['result']['pointInfos']

        sum_income = 0
        details_income = ''
        for info in point_infos:
            device_id = info['mac']
            point_income = info['todayPointIncome']

            if device_id in config.DEFAULT_MAC_LIST:
                device_name = config.DEFAULT_MAC_LIST[device_id]
            else:
                device_name = device_id

            sum_income += point_income
            # markdown语法，输入'- '即可输出列表样式
            details_income = details_income + '\n - ' + \
                device_name + ':' + str(point_income)

        # 获取今天的日期
        today_date = result['result']['todayDate']
        # print(today_date, ':', sum_income)

        # 将日期添加到字符串前面
        summary = str(today_date) + ' 获取京豆：' + str(sum_income)

        return summary, details_income

    def load_wskey_str(self, wskey):
        """
        请求通过wskey鉴权，需要将wskey添加到header中
        """
        self.session.headers['wskey'] = wskey.encode("utf-8").decode("latin1")

    def get_integral(self):
        """
        获取积分数据
        """
        response = self.session.get(config.DEFAULT_URL)
        if self.__json_check(response):
            # 解析数据
            return self.__analysis_data(response)
        else:
            return "获取失败", response.json()


def send_text(title='', content=''):

    print(title)
    print(content)

    SERVERCHAN_SECRETKEY = config.SERVERCHAN_SECRETKEY
    print('sc_key: ', SERVERCHAN_SECRETKEY)
    if isinstance(SERVERCHAN_SECRETKEY, str) and len(SERVERCHAN_SECRETKEY) > 0:
        print('检测到 SCKEY， 准备推送')
        push_to_wechat(text=title,
                       desp=str(content),
                       secretKey=SERVERCHAN_SECRETKEY)


def run():
    sb = JDCloud_Bot()
    wskey = config.DEFAULT_WSKEY
    sb.load_wskey_str(wskey)
    title, content = sb.get_integral()
    return title, content


if __name__ == "__main__":
    try:
        # 获取积分
        title, content = run()
        send_text(title, content)

    except Exception as e:
        send_text('=== ERROR ===', e)

    print('执行完毕')
