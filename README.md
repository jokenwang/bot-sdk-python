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

### 暂未实现
* 拦截器
* 监控器
* 会话
* ~~指令处理~~


### 免责声明

* 此SDK非官网提供，纯属个人学习研究，如因使用此SDK导致的任何损失，本人概不负责


