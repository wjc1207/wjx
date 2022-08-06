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
probability = [[0.9732,0,0,0.268],[0.0465,0.9535],[0.7311,0.9496,0.3277,0.6639,0.8824,0.6134],[0.9244,0.8067,0.7731,0.5798,0.8067],
[0.7984,0.0233,0.155,0.0233],[0.8837,0.093,0.0233],[0.2248,0.5271,0.2481],[0.0155,0.9845],[0.7953,0.2047],[0.9606,0.9134,0.9291],[0.2283,0.7717]]

channelState = [True]

def autoFill(probability):
    wd = tools.getWebDriver()
    try:
        wd.get("https://www.wjx.cn/vm/ervZaoV.aspx")
    except TimeoutError:
        wd.quit()
        return 0
    wd.maximize_window()
    #第一道题
    autofillques.autoFillSingleChoiceQues(wd,1,probability)
    #第二道题分情况选择
    if random.random() < probability[1][0]: #无
        wd.find_element(By.ID, "div2").find_elements(By.CLASS_NAME,"ui-radio")[0].click()
        time.sleep(random.random()*5)
        wd.find_element(By.ID, "divNext").click()
        time.sleep(random.random()*5)
    else: #有
        wd.find_element(By.ID, "div2").find_elements(By.CLASS_NAME,"ui-radio")[1].click()
        time.sleep(random.random()*5)
        wd.find_element(By.ID, "divNext").click()
        time.sleep(random.random()*5)
        autofillques.autoFillMultiChoiceQues(wd,3,probability)
        autofillques.autoFillMultiChoiceQues(wd,4,probability)
        wd.find_element(By.ID, "divNext").click()
        time.sleep(random.random()*5)
    #题目五
    autofillques.autoFillSingleChoiceQues(wd,5,probability)
    #题目六
    autofillques.autoFillSingleChoiceQues(wd,6,probability)
    #题目七
    autofillques.autoFillSingleChoiceQues(wd,7,probability)
    #题目八分情况选择
    if random.random() < probability[7][0]:
        wd.find_element(By.ID, "div8").find_elements(By.CLASS_NAME,"ui-radio")[0].click() #不会
        time.sleep(random.random()*5)
        wd.find_element(By.ID, "divNext").click()
        time.sleep(random.random()*5)
    else:
        wd.find_element(By.ID, "div8").find_elements(By.CLASS_NAME,"ui-radio")[1].click() #会
        time.sleep(random.random()*5)
        wd.find_element(By.ID, "divNext").click()
        time.sleep(random.random()*5)
        #题目九
        autofillques.autoFillSingleChoiceQues(wd,9,probability)
        #题目十
        autofillques.autoFillMultiChoiceQues(wd,10,probability)
        #题目十一
        autofillques.autoFillSingleChoiceQues(wd,11,probability)
        wd.find_element(By.ID, "divNext").click()
    time.sleep(random.random()*5)
    wd.find_element(By.ID, "ctlNext").click() #提交问卷
    time.sleep(3)
    #验证按钮和滑动条
    try:
        successMsg = wd.find_element(By.ID, "divdsc")
    except Exception:
        verify.verifyByCSMA(wd,channelState)

    time.sleep(4) #休息4秒
    wd.quit()

def multiAutoFill(num):
    for i in range(num):
        autoFill(probability)

for i in range(16):
    task = threading.Thread(target=multiAutoFill,args=(100,))
    task.start()
    time.sleep(4)
