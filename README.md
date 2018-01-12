# bot-sdk
Dueros Bot Python版SDK，鉴于官网只提供了PHP和Node的SDK，不能满足大家的需求，
于是硬着头皮试着搞一搞Python版本的SDK。这里不得不吐槽下百度的文档(实在挺烂的)。
另外Python自学了1周，代码还比较烂（勿喷），希望大家不断来完善。

### SDK结构介绍

* Bot.py 为SDK的入口，用于接收请求并返回结果
* Nlu.py 负责对数据的加工，如槽位、意图信息等
* Request.py Bot接收到的数据全部交给Request进行处理，Request再委托Nlu、Session
对数据做处理
* Response.py Bot数据处理完后交由Response封装返回结果
* Session.py 处理会话信息(暂未实现)
* card 目录处理展示卡片相关
* directive 生成指令相关比如：浏览器指令、音频指令
* tests 目录存放本地测试代码
* samples 搭建有Python Wsgi 的Demo,通过执行sh start.sh

### Bot-Python-SDK使用说明

* 实现自己的Bot逻辑需要继承Bot.py类

```
from sdk.Bot import Bot

class BotTest(Bot):
    def __init__(self, data):
        super(BotTest, self).__init__(data)
        self.addLaunchHandler(launchHandlerFunc)
        self.addIntentHandler('自己的意图标识英文名', 自定义func)
```

* 创建自己的Handler函数,回调函数返回的是dict类型数据，可以包含多个字段card，directives，outputSpeech，reprompt

```
def lanuchHandlerFunc():
    return {
        'card': TextCard('欢迎使用家居控制!请告诉我您要查找什么智能设备，比如查找我的空调'),
        'outputSpeech': '<speak>欢迎使用家居控制!请告诉我您要查找什么智能设备，比如查找我的空调</speak>'
    }
```

* 搭建服务 详见samples


### 更新记录

===========================================

2018-01-12

* Bot.py添加错误回调，用户可以调用setCallBack方法设置错误回调方法
* 优化samples demo
* 添加个税demo数据


2018-01-06

* 完成拦截器
* 完成会话
* 完成指令处理

===========================================

### 暂未实现
* ~~拦截器~~
* ~~监控器~~
* ~~会话~~
* ~~指令处理~~


### 免责声明

* 此SDK非官网提供，纯属个人学习研究，如因使用此SDK导致的任何损失，本人概不负责


