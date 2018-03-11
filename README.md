# bot-sdk
Dueros Bot Python版SDK，鉴于官网只提供了PHP和Node的SDK，不能满足大家的需求，
于是硬着头皮试着搞一搞Python版本的SDK。这里不得不吐槽下百度的文档(实在挺烂的)。
另外Python自学了1周，代码还比较烂（勿喷），希望大家不断来完善。



### SDK结构介绍

* 封装了DuerOS的request和response,其中Request.py中用来处理DuerOS发送给Bot的请求数据，其中包含Request再委托Nlu、Session
对请求数据做处理；Response.py Bot数据处理完后交由Response封装返回给DuerOS
* Bot.py 为SDK的入口，用于接收DuerOs请求并返回结果
* Nlu.py 负责对请求关键信息的提取，如槽位、意图信息等
* Request.py Bot接收到的数据全部交给Request进行处理，Request再委托Nlu、Session 对数据做处理
* Response.py Bot数据处理完后交由Response封装返回结果
* Session.py 处理会话信息
* card 目录处理展示卡片相关
* directive 生成指令相关比如：浏览器指令、音频指令
* tests 目录存放本地测试代码
* samples 搭建有Python Wsgi 的Demo,通过执行sh start.sh

### 安装、使用BOT SDK进行开发

下载bot-sdk代码后，可以使用如下命令安装:
```javascript
bot-sdk:python setup.py install。
```
为了开始使用BOT SDK，你需要先新建一个python文件，比如文件名是Bot.py,该文件需要继承sdk/Bot.py。下一步，我们处理意图，Bot-sdk提供个函数来handle这些意图，
为了开始使用BOT SDK，你需要先新建一个python文件，比如文件名是Bot.py,该文件需要继承sdk/Bot.py。下一步，我们处理意图，Bot-sdk提供个函数来handle这些意图,例如继承sdk/Bot.py中的addIntentHandler函数，添加一个意图处理函数，比如，为新建闹钟，创建一个handler，在构造函数中添加：
```javascript
self.addIntentHandler('remind', self.createRemind)，其中需要自定义createRemind处理函数：例如定义一个函数
def createRemind(self):
	remindTime = self.getSlots('remindTime')
	if($remindTime) {
		card = new TextCard('创建中')
		 return {
            'card':card,
        }
	}
```
第一个参数代表意图名称，第二个参数代表意图命中后的回调函数，这里addHandler可以用来建立intent和handler的映射，第一个参数是意图名称,
是条件，如果满足则执行对应的回调函数(第二个参数)。 其中回调函数中，self指向当前的Bot，getSlots继承自父类Bot，通过slot名字来获取对应的值。回调函数返回值是一个字典，可以包含多个字段，比如：card，directives，outputSpeech，reprompt等
示例如下：

* 可以搭建服务 详见samples
### card展示卡片
* 文本卡片:TextCard
```
card = TextCard('content')
or 
card = TextCard()
//设置链接
card.setAnchor('http://www.baidu.com');
//设置cueWords
card.addCueWords('hint1');
```
* 标准卡片 StandardCard
```
card = StandardCard()
card.setTitle('title');
card.setContent('content');
card.setImage('http://www...');
card.setAnchor('http://www.baidu.com');
```
* 列表卡片ListCard
```
card = new ListCard();
item = new ListCardItem();
item.setTitle('title')
item.setContent('content')
item.setUrl('http://www')
item.setImage('http://www.png');
card.addItem(item);
```
* 图片卡片ImageCard
```
card = ImageCard();
card.addItem('http://src.image', 'http://thumbnail.image');
```
### directive返回指令
* 播放指令 AudioPlayer.Play
```
directives = []
directive = Play('http://www.music', Play::REPLACE_ALL)
directives.append(directive)
return {
    'directives':directives,
    'outputSpeech':'正在为你播放歌曲',
}
```
* 停止端上的播放音频 AudioPlayer.Stop
```
directives = []
directive = Stop()
directives.append(directive)
return {
    'directives':directives,
    'outputSpeech':'已停止播放',
}
```
设置好handler之后，就可以实例化刚刚定义的Bot，在webserver中接受DuerOS来的请求。例如samples中的文件。
###返回speech
* outputSpeech
上面例子，除了返回card之外，还可以返回outputSpeech，让客户端播报tts：
```
return {
    'outputSpeech':'请问你要干啥呢',
    'outputSpeech':'<speak>请问你要干啥呢</speak>'
}
```
* reprompt
当客户端响应用户后，用户可能会一段时间不说话，如果你返回了reprompt，客户端会提示用户输入
```
return {
    'reprompt':'请问你要干啥呢',
    //或者ssml
    'reprompt':'<speak>请问你要干啥呢</speak>'
}
```
###Lanuch & SessionEnd
* bot开始服务
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


