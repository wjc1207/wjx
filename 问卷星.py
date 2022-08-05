from logging import NullHandler
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
    with open('实用小工具\stealth.min.js', 'r') as f:
        js = f.read()
    wd.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
    wd.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
    """})

    return wd

def autoFillSingleChoiceQues(wd,quesIndex,probability):
    low_limit = 0
    high_limit = probability[quesIndex-1][0]
    random_num = random.random()
    for i in range(len(probability[quesIndex-1])):
        if random_num > low_limit and random_num < high_limit:
            wd.find_element(By.ID, "div" + str(quesIndex)).find_elements(By.CLASS_NAME,"ui-radio")[i].click() #填写答案
            break
        low_limit += probability[quesIndex-1][i]
        high_limit += probability[quesIndex-1][i+1]
    time.sleep(random.random()*5)

def autoFillMultiChoiceQues(wd,quesIndex,probability):
    choices = wd.find_element(By.ID, "div" + str(quesIndex)).find_elements(By.CLASS_NAME,"ui-checkbox")
    for i in range(len(probability[quesIndex-1])): 
        if random.random() < probability[quesIndex-1][i]: 
            choices[i].click() #填写答案
            time.sleep(random.random())
    time.sleep(random.random()*5)

def verify(wd):
    #点击对话框里的确认
    try:
        wd.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/button").click()
    except Exception:
        pass
    time.sleep(random.random()*5)
    action = ActionChains(wd)
    #验证按钮和滑动条
    tag = 0
    while (True):
        try:
            verifiButtton = wd.find_element(By.ID, "rectMask")
        except Exception:
            verifiButtton = None
        if verifiButtton != None:
            action.move_to_element(verifiButtton).perform()
            action.move_by_offset((random.random()-0.5)*2*100,(random.random()-0.5)*2*15).perform()
            action.click().perform()
        try:
            verifiSlide = wd.find_element(By.ID,"nc_1_n1z")
            break
        except Exception:
            verifiSlide = None
            try:
                stopButton = wd.find_element(By.ID,"SM_POP_CLOSE_1")
            except Exception:
                stopButton = None
            if stopButton != None:
                action.move_to_element(stopButton).perform()
                action.click().perform()
        time.sleep(1)
        tag += 1
        if tag > 10:
            break

    if verifiSlide != None:
        action.move_to_element(verifiSlide).perform()
        action.drag_and_drop_by_offset(verifiSlide,300,0).perform()

#问卷概率 每个问题的每个选项被选中的概率
probability = [[0.9732,0,0,0.268],[0.0465,0.9535],[0.7073,0.9187,0.2358,0.6341,0.8211,0.5203],[0.9431,0.6911,0.8211,0.5122,0.7724],
[0.7984,0.0233,0.155,0.0233],[0.8837,0.093,0.0233],[0.2248,0.5271,0.2481],[0.0155,0.9845],[0.7953,0.2047],[0.9606,0.9134,0.9291],[0.2283,0.7717]]

def autoFill(probability):
    wd = getWebDriver()
    try:
        wd.get("https://www.wjx.cn/vm/ervZaoV.aspx")
    except TimeoutError:
        wd.quit()
        return 0
    wd.maximize_window()
    #第一道题
    autoFillSingleChoiceQues(wd,1,probability)
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
        autoFillMultiChoiceQues(wd,3,probability)
        autoFillMultiChoiceQues(wd,4,probability)
        wd.find_element(By.ID, "divNext").click()
        time.sleep(random.random()*5)
    #题目五
    autoFillSingleChoiceQues(wd,5,probability)
    #题目六
    autoFillSingleChoiceQues(wd,6,probability)
    #题目七
    autoFillSingleChoiceQues(wd,7,probability)
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
        autoFillSingleChoiceQues(wd,9,probability)
        #题目十
        autoFillMultiChoiceQues(wd,10,probability)
        #题目十一
        autoFillSingleChoiceQues(wd,11,probability)
        wd.find_element(By.ID, "divNext").click()
    time.sleep(random.random()*5)
    wd.find_element(By.ID, "ctlNext").click()
    time.sleep(1)
    #验证按钮和滑动条
    verify(wd)

    time.sleep(random.randint(10,20)) #错开时间
    wd.quit()

def multiAutoFill(num):
    for i in range(num):
        autoFill(probability)

task1 = threading.Thread(target=multiAutoFill,args=(100,))
task2 = threading.Thread(target=multiAutoFill,args=(100,))
task3 = threading.Thread(target=multiAutoFill,args=(100,))
task4 = threading.Thread(target=multiAutoFill,args=(100,))
task5 = threading.Thread(target=multiAutoFill,args=(100,))
task1.start()
time.sleep(random.randint(8,16))
task2.start()
time.sleep(random.randint(8,16))
task3.start()
time.sleep(random.randint(8,16))
task4.start()
time.sleep(random.randint(8,16))
task5.start()