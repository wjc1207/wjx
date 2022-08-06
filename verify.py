from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import threading

lock = threading.Lock()

def verifyByALOHA(wd):
    #点击对话框里的确认
    try:
        wd.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/button").click() #按“确定”按钮
    except Exception:
        pass
    time.sleep(random.random()*5)
    action = ActionChains(wd)
    #验证按钮和滑动条
    tag = 0
    while (True):
        try:
            verifiButtton = wd.find_element(By.ID, "rectMask")
            action.move_to_element(verifiButtton).perform()
            action.move_by_offset((random.random()-0.5)*2*100,(random.random()-0.5)*2*15).perform()
            action.click().perform()
        except Exception:
            verifiButtton = None

        try:
            verifiSlide = wd.find_element(By.ID,"nc_1_n1z")
            action.move_to_element(verifiSlide).perform()
            action.drag_and_drop_by_offset(verifiSlide,300,0).perform()
            break
        except Exception:
            verifiSlide = None
            try:
                stopButton = wd.find_element(By.ID,"SM_POP_CLOSE_1")
                action.move_to_element(stopButton).perform()
                action.click().perform()
            except Exception:
                stopButton = None
        
        try:
            successMsg = wd.find_element(By.ID, "divdsc")
            break
        except Exception:
            pass
        time.sleep(1)
        tag += 1
        if tag > 5:
            time.sleep(random.randint(1,30))
            break
        
def verifyByCSMA(wd,channelState):
    lock.acquire()
    while(True):
        if channelState[0]:
            channelState[0] = False
            break
        else:
            time.sleep(1)
    lock.release()
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
            action.move_to_element(verifiButtton).perform()
            action.move_by_offset((random.random()-0.5)*2*100,(random.random()-0.5)*2*15).perform()
            action.click().perform()
        except Exception:
            verifiButtton = None

        try:
            verifiSlide = wd.find_element(By.ID,"nc_1_n1z")
            action.move_to_element(verifiSlide).perform()
            action.drag_and_drop_by_offset(verifiSlide,300,0).perform()
            break
        except Exception:
            verifiSlide = None
            try:
                stopButton = wd.find_element(By.ID,"SM_POP_CLOSE_1")
                action.move_to_element(stopButton).perform()
                action.click().perform()
            except Exception:
                stopButton = None
        
        try:
            successMsg = wd.find_element(By.ID, "divdsc")
            break
        except Exception:
            pass
        time.sleep(1)
        tag += 1
        if tag > 5:
            time.sleep(random.randint(1,30))
            break
    
    channelState[0] = True
    