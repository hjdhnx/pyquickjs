#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : test_module.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/3/31

from pyquickjs import Context

if __name__ == '__main__':
    module_js = """
    function add(a,b){
    return a+b
    }
    globalThis.add = add;
    module.exports = {
    add
    }
    """
    ctx = Context()
    ctx.module(module_js)
    ret = ctx.eval('add(1,2)')
    print('ret:', ret)
