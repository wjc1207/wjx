# wjx
Some python files that can **fill in the wjx questionnaire automatically** using selenium and stealth.min.js, and its outstanding point is the **verify function** and **not relies on the IP pools**.

It utilizes the feature that Intelligent Verification can only do once at one time in the same IP. As a communication engineering student, the way of solving multi-access problem came to me immediately when I get the feature. So I use the **ALOHA and CSMA** to solve the verify problem.

I'm very glad to get stars and forks~

一些python文件，使用selenium和stealth.min.js**自动填写问卷星问卷**，其突出之处是**验证功能**，并且**不依赖IP池工作**。

它利用了智能验证在同一IP中某一时间只能执行一次的特点。作为一名通信工程专业的学生，当我get这个特点时，我立即想到了解决multi-access问题的方法。因此，我使用**ALOHA和CSMA**来解决验证问题。

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
