#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : test_module.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/3/31
import os
import sys

from pyquickjs import Context

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
    import "./crypto-js.js";
    console.log("Hello World 你好");

    console.log(typeof(q.add));

    console.log("fib(10)=", fib(10));'''
    ctx = Context()
    print("work dir:", os.getcwd())
    ctx.eval('let a=1+3')
    print(ctx.eval('a'))

    ctx.module(module_js, "11.js")
    ctx.module(mod_test,"")
    ctx.module('''import qq from "11.js";\nconsole.log(typeof(qq.addd));''',"2.js")
