#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@author: speedor
@file: magi.py
@version: 1.0
@time: 2020/7/24 23:21
@desc: Magi AI 机器学习搜索引擎搜索 demo
"""
import re
import requests

headers = {
    "cookie": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
}


def hex_join(arg: str) -> str:
    _0x4b082b = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19, 0xd,
                 0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c,
                 0x22, 0x25, 0xc, 0x24]
    _0x4da0dc = [''] * 40
    for _0x20a7bf in range(0, len(arg)):
        _0x385ee3 = arg[_0x20a7bf]
        for _0x217721 in range(0, len(_0x4b082b)):
            if _0x4b082b[_0x217721] == _0x20a7bf + 0x1:
                _0x4da0dc[_0x217721] = _0x385ee3
    return ''.join(_0x4da0dc)


def hex_xor(_0x4e08d8: str, _0x23a392: str) -> str:
    """
        _0x4e08d8
    :return:
    """
    _0x5a5d3b = ''
    _0xe89588 = 0x0
    while _0xe89588 < len(_0x23a392) and _0xe89588 < len(_0x4e08d8):
        _0x401af1 = int(_0x23a392[_0xe89588:_0xe89588 + 0x2], 0x10)
        _0x105f59 = int(_0x4e08d8[_0xe89588:_0xe89588 + 0x2], 0x10)
        _0x189e2c = hex(_0x401af1 ^ _0x105f59).replace("0x", "")
        if len(_0x189e2c) == 0x1:
            _0x189e2c = '\x30' + _0x189e2c
        _0x5a5d3b += _0x189e2c
        _0xe89588 += 0x2
    return _0x5a5d3b


def get_arg1_cookie_jsScript_from_first_response(url) -> dict:
    """
        get_arg1_cookie_jsScript_from_first_response
    :param url:
    :return:  {'arg1': 'xxxxx', 'acw_tc':  'xxxx'}
    """
    result = {"arg1": "", "acw_tc": ""}
    resp = requests.get(url, headers=headers, verify=False)
    try:
        arg1 = re.search("arg1='([^']+)'", resp.text).group(1)
        acw_tc = requests.utils.dict_from_cookiejar(resp.cookies)["acw_tc"]
        result["arg1"] = arg1
        result["acw_tc"] = acw_tc
    except Exception as e:
        print(e)
    return result


def create_cookie(query: str) -> str:
    """
        测试：
            arg1 = "E609CBF569B6DB613EDB0C3E3174149363F521A9"
            acw_sc__v2 = "5f1e7681965cf7c53baeafe680320df91b843110"
    :param query:
    :return:
    """
    _0x5e8b26 = "3000176000856006061501533003690027800375"
    arg1_cookie_dict = get_arg1_cookie_jsScript_from_first_response("https://magi.com/search?q=" + query)
    arg1_str = arg1_cookie_dict['arg1']
    # arg1_str = "E609CBF569B6DB613EDB0C3E3174149363F521A9"
    acw_tc_str = arg1_cookie_dict['acw_tc']
    _0x23a392 = hex_join(arg1_str)
    acw_sc__v2 = 'acw_sc__v2=' + hex_xor(_0x5e8b26, _0x23a392)
    # print(acw_sc__v2)
    cookies = "acw_tc=" + acw_tc_str + ";" + acw_sc__v2
    return cookies


if __name__ == '__main__':
    query = "电冰箱"
    headers["cookie"] = create_cookie(query)
    resp = requests.get("https://magi.com/search?q=" + query, headers=headers, verify=False)
    print(resp.text)
