#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : test_module.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/3/31
import os
import sys

from pyquickjs import Context

base_path = os.path.dirname(__file__)


def _(p):
    return os.path.join(base_path, p)


def moduleloader(number):
    print(f"module_ name: {number}")
    _str = ''
    with open(_(number), encoding='utf-8') as f:
        _str = f.read()
    #print(_str)
    return _str


def handleLog(*args):
    print(*args)


if __name__ == '__main__':
    module_js = """
    function addd(a,b){
    return a+b
    }
    export default {
    addd
    }
    """
    mod_test = '''import { fib } from "./fib_module.js";
    import q from "./1.js";
    import cheerio from './cheerio.min.js';
    import './crypto-js.js';
    import 模板 from './模板.js'
    import {gbkTool} from './gbk.js'

    console.log("Hello World 你好");

    console.log(typeof(q.add));

    console.log("fib(10)=", fib(10));'''
    ctx = Context()
    ctx.moduleloader(moduleloader)
    #print(ctx.getmoduleloader('1.js'))
    ctx.add_callable("log", handleLog)
    ctx.eval("const console = {log};")
    print("work dir:", os.getcwd())
    ctx.module(module_js, "11.js")
    ctx.module('import qq from "./drpy2.js";\nconsole.log(typeof(qq.addd));', "2.js")
    ctx.eval('console.log(1+1)')
    ctx.module(mod_test)
