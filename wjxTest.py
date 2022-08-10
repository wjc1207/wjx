from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import threading
import tools
import autofillques
import verify

#问卷概率 每个问题的每个选项被选中的概率
probability = [[0.5,0.5],[0.2,0.9,0.6]]

channelState = [True]

def autoFill(probability):
    wd = tools.getWebDriver()
    try:
        wd.get("https://www.wjx.cn/vm/ro7P32N.aspx")
    except TimeoutError:
        wd.quit()
        return 0
    wd.maximize_window()
    #第一道题
    autofillques.autoFillSingleChoiceQues(wd,1,probability)
    autofillques.autoFillMultiChoiceQues(wd,2,probability)
    wd.find_element(By.ID, "ctlNext").click() #提交问卷
    time.sleep(3)
    #验证按钮和滑动条
    try:
        successMsg = wd.find_element(By.ID, "divdsc")
    except Exception:
        verify.verifyByCSMA(wd,channelState=channelState)

    time.sleep(4) #休息4秒
    wd.quit()

def multiAutoFill(num):
    for i in range(num):
        autoFill(probability)

for i in range(3):
    task = threading.Thread(target=multiAutoFill,args=(10,))
    task.start()
    time.sleep(4)