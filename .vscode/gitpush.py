#!/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import os
import filecmp
import subprocess
import platform
import webbrowser
import configparser
import pathlib


if __name__ == "__main__":

    print("gitpush.py version: 1.1")

    execResult = os.system("git config credential.helper \"\" && git add . && git commit -m \"提交作业\"")

    if execResult == 256 or  execResult == 1:
        print("\n-------- 本次提交没有任何变更，即使推送成功，也不代表远程一定有提交记录 --------")
        print("-------- 请对项目中的文件进行修改后再进行提交-----------------------------------")
    elif  execResult != 0:
        print("\n-------- 提交作业失败! 错误码: {0}--------".format(execResult))
        exit(execResult)
    print("\n-------------------------------------------------------------------------------")
    print("请在 VSCode 顶部弹出的命令面板中输入 Git 远程库的用户名和密码。通常为 CodeCode 平台的用户名和密码。")
    print("-------------------------------------------------------------------------------")

    execResult = os.system("git push")
    if execResult == 0:
        print("\n-------- 提交作业成功！ --------")
        strGitconfigPath = ""
        if platform.system().lower() == 'windows':
            strGitconfigPath = ".\\.git\\config" 
        else:
            strGitconfigPath = "./.git/config"
        gitConfigPath = pathlib.Path(strGitconfigPath)
        
        # 判断是否存在.git/config文件
        if gitConfigPath.exists() and gitConfigPath.is_file():
            #  实例化configParser对象
            config = configparser.ConfigParser()
            config.read(strGitconfigPath, encoding='UTF-8')
            webURL = config.get('remote \"origin\"', 'url').replace(".git", "")
            webInfo = "正在使用浏览器打开 Git 远程库页面，或者点击 " + webURL

            ciPath = pathlib.Path(".gitlab-ci.yml")
            if ciPath.exists() and ciPath.is_file():
                webURL = config.get('remote \"origin\"', 'url').replace(".git", "/pipelines")
                webInfo = "正在使用浏览器打开流水线页面，或者点击 " + webURL
        
            print(webInfo)
            webbrowser.open(webURL)
    else:
        print("\n--- 提交作业失败! 想解决失败问题？ 使用浏览器访问下面链接即可。 ---")
        print("https://www.codecode.net/engintime/codecode/publicmanual/blob/master/GitFAQ.md")
        exit(execResult)
    