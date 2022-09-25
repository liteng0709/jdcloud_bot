import json
import os


"""
调试 url
"""
DEFAULT_URL = 'https://router-app-api.jdcloud.com/v1/regions/cn-north-1/todayPointDetail?sortField=today_point&sortDirection=DESC&pageSize=15&currentPage=1'

"""
请求头
"""
DEFAULT_HEADERS = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; V1936A Build/RP1A.200720.012) (JBOX-APP; Android/3.3.3/58)",
    "Content-Type": "application/json",
    "Referer": "http://guanli.luyou.360.cn/new_index.htm",
    "Connection": "close",
    "Host": "router-app-api.jdcloud.com",
    "Accept-Encoding": "gzip",
}
"""
调试 wskey
"""
DEFAULT_WSKEY = os.environ["WSKEY"]
# DEFAULT_WSKEY = ''

"""
调试 mac_list
注意:此处为字典类型，os.environ获取的为str类型，需要进行转换
mac_list = json.loads('{"DCD87C2B1111": "Luban-1", "DCD87C4A2222": "YLuban-2"}')
"""
DEFAULT_MAC_LIST = json.loads(os.environ["DEFAULT_MAC_LIST"])
# DEFAULT_MAC_LIST = json.loads('')


"""
调试 SERVERCHAN_SECRETKEY
"""
SERVERCHAN_SECRETKEY = os.environ["SERVERCHAN_SECRETKEY"]
# SERVERCHAN_SECRETKEY = ''
