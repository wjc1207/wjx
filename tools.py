from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import threading

def getWebDriver():
    # 启动chrome浏览器
    options = webdriver.ChromeOptions()

    # 处理SSL证书错误问题
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
        
    # 忽略无用的日志
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)

    wd = webdriver.Chrome(options=options)
    with open('wjx-main\stealth.min.js', 'r') as f:
        js = f.read()
    wd.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
    wd.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
    """})

    return wd