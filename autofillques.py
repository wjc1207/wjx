from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import threading


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