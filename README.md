# wjx
Some python files that can **fill in the wjx questionnaire automatically** using selenium and stealth.min.js, and its outstanding point is the **pass Intelligent verification function** and **not relies on the IP pools**.

It utilizes the feature that Intelligent Verification can only do once at one time in the same IP. As a communication engineering student, the way of solving multi-access problem came to me immediately when I get the feature. So I use the **ALOHA and CSMA** to solve the verify problem.

The ALOHA is a violent method that try to pass the intelligent verification whenever It can, if it meets a collision, It will wait a random time and try a again. It applies the low-strength workplace.

The CSMA is a better method that will listen the channel, if the channel is busy, it will wait until it's idle and immediately start to pass the intelligent verification. It has a lower collision probability and higher delay. It applies the high-strength workplace.

I'm very glad to get stars and forks~

一些python文件，使用selenium和stealth.min.js**自动填写问卷星问卷**，其突出之处是**通过智能验证功能**，并且**不依赖IP池工作**。

它利用了智能验证在同一IP中某一时间只能执行一次的特点。作为一名通信工程专业的学生，当我get这个特点时，我立即想到了解决multi-access问题的方法。因此，我使用**ALOHA和CSMA**来解决验证问题。

ALOHA是一种暴力方法，它试图在任何可能的时候通过智能验证，如果遇到冲突，它将随机等待一段时间，然后重试。它适用于低强度工作场所。

CSMA是一种更好的监听信道的方法，如果信道忙，它将等待直到空闲，并立即开始通过智能验证。它具有较低的碰撞概率和较高的延迟。它适用于高强度工作场所。

欢迎大家来star和fork~

_________________
### 使用方法
1. 下载Selenium库和threading库

    `pip install selenium`
    
    `pip install threading`

2. 前往[https://chromedriver.storage.googleapis.com/index.html](https://chromedriver.storage.googleapis.com/index.html)下载对应的ChromeDriver，大版本号对应即可。目录中的是104版本的

3. 将驱动**所在文件夹**地址添加到环境变量PATH中
_________________

参考： [白月黑羽-Selenium教程](https://www.byhy.net/tut/auto/selenium/)。
