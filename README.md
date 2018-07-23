# bot-sdk



### SDK结构介绍
* Bot.py为SDK的入口，用于接收DuerOS请求并返回结果
* Nlu.py负责对请求关键信息的提取，如槽位、意图信息等
* Request.py技能接收到DuerOS的数据全部交给Request进行处理，Request再委托Nlu、Session对数据做处理
* Response.py技能数据处理完后交由Response封装结果返回DuerOS
* Session.py处理会话信息
* Certificate.py封装DuerOS和技能通信认证
* card目录处理展示卡片相关
* directive目录生成指令相关比如：浏览器指令、音频指令
* tests 目录存放本地测试代码
* samples 示例demo，其中包括guess_num、audio_play、personal_income_tax
### 安装、使用BOT SDK进行开发

1、 通过pip进行安装   

```
pip install dueros-bot
```
  
2、 下载源码安装
    
* 通过GitHub获取最新源码
```
git clone https://github.com/jokenwang/bot-sdk-python.git
```

* 通过Pypi获取最新发布版本源码
    
    * dueros-bot-1.1.0 (大版本更新) [Pypi地址](https://pypi.org/project/dueros-bot-python2/1.1.0)
    * dueros-bot-0.2.4 [Pypi地址](https://pypi.python.org/pypi/dueros-bot/0.2.4)
    * dueros-bot-0.2.3 [Pypi地址](https://pypi.python.org/pypi/dueros-bot/0.2.3)
    * dueros-bot-0.2.2 [Pypi地址](https://pypi.python.org/pypi/dueros-bot/0.2.2)

下载bot-sdk代码后，可以使用如下命令安装:
```python
python setup.py install
```

3、sh start.sh 运行，如出现问题请参考[常见问题](#常见问题)

4、运行tests目录下的 
```bash
sh postData.sh json/xxx.json
```

将xxx.json文件内容发送模拟数据到服务器

5、开发教程

为了开始使用BOT SDK，你需要先新建一个python文件，比如文件名是Bot.py,该文件需要继承sdk/Bot.py。下一步，我们处理意图，Bot-sdk提供个函数来handle这些意图,例如继承sdk/Bot.py中的add_intent_handler函数，添加一个意图处理函数，比如，为新建闹钟，创建一个handler，在构造函数中添加：

```python
self.add_intent_handler('remind', self.create_remind)
def create_remind(self):
    remind_time = self.get_slots('remindTime')
    if remind_time:
        card = new TextCard('创建中')
        return {
            'card': card,
        }
```
第一个参数代表意图名称，第二个参数代表意图命中后的回调函数，这里add_handler可以用来建立intent和handler的映射，第一个参数意图名称是条件，如果满足则执行对应的回调函数(第二个参数)。 其中回调函数中，self指向当前的Bot，get_slots继承自父类Bot，通过slot名字来获取对应的槽位值。回调函数返回值是一个字典，可以包含多个字段，比如：card、directives、outputSpeech、reprompt等,下面会一一给出示例。
### card展示卡片
* 文本卡片:TextCard
```python
card = TextCard('content')
or 
card = TextCard()
//设置链接
card.set_anchor('http://www.baidu.com');
//设置cueWords
card.add_cue_Words('hint1');
```
* 标准卡片 StandardCard
```python
card = StandardCard()
card.set_title('title');
card.set_content('content');
card.set_image('http://www...');
card.set_anchor('http://www.baidu.com');
```
* 列表卡片ListCard
```python
card = new ListCard();
item = new ListCardItem();
item.set_title('title')
item.set_content('content')
item.set_url('http://www')
item.set_image('http://www.png');
card.add_item(item);
```
* 图片卡片ImageCard
```python
card = ImageCard();
card.add_item('http://src.image', 'http://thumbnail.image');
```

### 文本展现模板
* BodyTemplate1
```python

bodyTemplate = BodyTemplate1()
bodyTemplate.set_token('token')
#设置模版背景图片
bodyTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版标题
bodyTemplate.set_title('托尔斯泰的格言')
#设置模版plain类型的文本
bodyTemplate.set_plaintext_content('拖尔斯泰-理想的书籍是智慧的钥匙') 
#定义RenderTemplate指令
directive = RenderTemplate(bodyTemplate)
return {
    'directives': [directive],
    'outputSpeech': '这是BodyTemplate1模板'
}
```
### 上图下文模版
* BodyTemplate2
```python
bodyTemplate = BodyTemplate2()
#设置模版token
bodyTemplate.set_token('token')
#设置模版展示图片
bodyTemplate.set_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版背景图片
bodyTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版标题
bodyTemplate.set_title('托尔斯泰的格言')
#设置模版plain类型的文本结构
bodyTemplate.set_plain_content('拖尔斯泰-理想的书籍是智慧的钥匙') 
#定义RenderTemplate指令
directive = RenderTemplate(bodyTemplate)
return {
    'directives':[directive],
    'outputSpeech': '这是BodyTemplate2模板'
}

```

### 左图右文模版
* BodyTemplate3
```python
bodyTemplate = BodyTemplate3()
#设置模版token
bodyTemplate.set_token('token')
#设置模版展示图片
bodyTemplate.set_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版背景图片
bodyTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版标题
bodyTemplate.set_title('托尔斯泰的格言')
#设置模版plain类型的文本结构
bodyTemplate.set_plain_content('拖尔斯泰-理想的书籍是智慧的钥匙')  
#定义RenderTemplate指令
directive = RenderTemplate(bodyTemplate)
return {
    'directives': [directive],
    'outputSpeech' : '这是BodyTemplate3模板'
}
```

### 右图左文
* BodyTemplate4
```python
bodyTemplate = BodyTemplate4()
bodyTemplate.set_token('token')
#设置模版展示图片
bodyTemplate.set_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版背景图片
bodyTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版标题
bodyTemplate.set_title('托尔斯泰的格言')
#设置模版plain类型的文本结构
bodyTemplate.set_plain_content('拖尔斯泰-理想的书籍是智慧的钥匙') 
#定义RenderTemplate指令
directive = RenderTemplate(bodyTemplate)
return {
    'directives': [directive],
    'outputSpeech': '这是BodyTemplate4模板'
}
```

### 图片模板
* BodyTemplate5
```python
bodyTemplate = BodyTemplate5()
#设置模版token
bodyTemplate.set_token('token')
#模版图片数组添加一张图片
bodyTemplate.add_images('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版背景图片
bodyTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版标题
bodyTemplate.set_title('托尔斯泰的格言')
#定义RenderTemplate指令
directive = RenderTemplate(bodyTemplate)
return {
    'directives': [directive],
    'outputSpeech': '这是BodyTemplate5模板'
}
```

### 横向列表模板
* ListTemplate1
```python
listTemplate = ListTemplate1()
#设置模板token
listTemplate.set_token('token')
#设置模板背景图
listTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版标题
listTemplate.set_title('托尔斯泰的格言')

#设置模版列表数组listItems其中一项，即列表的一个元素
listTemplateItem = ListTemplateItem()
listTemplateItem.set_token('token')
listTemplateItem.set_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
listTemplateItem.set_plain_primary_Text('一级标题')
listTemplateItem.set_plain_secondary_text('二级标题')

#把listTemplateItem添加到模版listItems
listTemplate.add_item(listTemplateItem)
#定义RenderTemplate指令
directive = RenderTemplate(listTemplate)
return {
    'directives': [directive],
    'outputSpeech': '这是ListTemplate1模板'
}
```

### 纵向列表模板
* ListTemplate2
```python
listTemplate = ListTemplate2()
#设置模板token
listTemplate.set_token('token')
#设置模板背景图
listTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
#设置模版标题
listTemplate.set_title('托尔斯泰的格言')

#设置模版列表数组listItems其中一项，即列表的一个元素
listTemplateItem = ListTemplateItem()
listTemplateItem.set_token('token')
listTemplateItem.set_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
listTemplateItem.set_plain_primary_text('一级标题')
listTemplateItem.set_plain_secondary_text('二级标题')

#把listTemplateItem添加到模版listItems
listTemplate.add_item(listTemplateItem)
#定义RenderTemplate指令
directive = RenderTemplate(listTemplate)
return {
    'directives': [directive],
    'outputSpeech': '这是ListTemplate1模板'
}
```


### directive指令
* 播放指令 AudioPlayer.Play
```python
directives = []
directive = Play('http://www.music', Play::REPLACE_ALL)
directives.append(directive)
return {
    'directives': directives,
    'outputSpeech': '正在为你播放歌曲',
}
```
* 停止端上的播放音频 AudioPlayer.Stop
```python
directives = []
directive = Stop()
directives.append(directive)
return {
    'directives': directives,
    'outputSpeech': '已停止播放',
}
```
设置好handler之后，就可以实例化刚刚定义的Bot，在webserver中接受DuerOS来的请求。例如samples中的文件。
### 返回speech
* outputSpeech
上面例子，除了返回card之外，还可以返回outputSpeech，让客户端播报tts：
```python
return {
    'outputSpeech': '请问你要干啥呢',
    'outputSpeech': '<speak>请问你要干啥呢</speak>'
}
```
* reprompt
当客户端响应用户后，用户可能会一段时间不说话，如果你返回了reprompt，客户端会提示用户输入
```python
return {
    'reprompt': '请问你要干啥呢',
    #或者ssml
    'reprompt': '<speak>请问你要干啥呢</speak>'
}
```
### Lanuch & SessionEnd
* bot开始服务
当bot被@（通过bot唤醒名打开时），DuerOS会发送LanuchRequest给bot，此时，bot可以返回欢迎语或者操作提示：
```python
def launch_request(self):
    return {
        'outputSpeech': r'欢迎进入'
    }

self.add_launch_handler(self.launch_request)
```
* bot 结束服务
当用户表达退出bot时，DuerOS会发送SessionEndedRequest：
```python
def end_request(self):
    ```
    清空状态，结束会话
    ```
self.add_session_ended_handler(self.end_request)
```
### 使多轮对话管理更加简单
往往用户一次表达的需求，信息不一定完整，比如：'给我创建一个闹钟'，由于query中没有提醒的时间，一个好的bot实现会问用户：'我应该什么时候提醒你呢？'，这时用户说明天上午8点，这样bot就能获取设置时间，可以为用户创建一个闹钟。比如，你可以这样来实现：
```python
def get_remind_slot(self):
    remind_time = self.get_slots('remind_time');
    if remind_time:
        return 返回设置闹钟指令
    self.nlu.ask('remind_time')
    return {
        'outputSpeech': r'要几点的闹钟呢?'
    }
self.add_launch_handler(self.get_remind_slot)
```
### 监听events
```python
def deal_alert_event(self):
    card = TextCard('闹钟创建成功')
    return {
        'card': card,
    }
self.add_event_listener('Alerts.SetAlertSucceeded', self.deal_alert_event)
```
Bot-sdk会根据通过addIntentHandler添加handler的顺序来遍历所有的检查条件，寻找条件满足的handler来执行回调，并且当回调函数返回值不是None时结束遍历，将这个不为None的值返回。

NLU会维护slot的值，merge每次对话解析出的slot，你可以不用自己来处理，DuerOS每次请求Bot时会将merge的slot都下发。session内的数据完全由你来维护，你可以用来存储一些状态，比如打车Bot会用来存储当前的订单状态。你可以通过如下接口来使用slot和session：
```python
get_slot('slot name')
set_slot('slot name', 'slot value'); #如果没有找到对应的slot，会自动新增一个slot
#session
get_session_attribute('key')
set_session_attribute('key', 'value')
#or
set_session_attribute('key.key1', 'value')
get_session_attribute('key.key1')
#清空session
clear_session()
```
你的Bot可以订阅端上触发的事件，通过接口addEventListener实现，比如端上设置闹钟成功后，会下发SetAlertSucceeded的事件，Bot通过注册事件处理函数，进行相关的操作。

### NLU交互协议
在DuerOS Bot Platform平台，可以通过nlu工具，添加了针对槽位询问的配置，包括：
1、是否必选，对应询问的默认话术
2、是否需要用户确认槽位内容，以及对应的话术
3、是否需要用户在执行动作前，对所有的槽位确认一遍，以及对应的话术
针对填槽多轮，Bot发起对用户收集、确认槽位（如果针对特定槽位有设置确认选项，就进行确认）、确认意图(如果有设置确认选项)的询问，bot-sdk提供了方便的快捷函数支持：
注意：一次返回的对话directive，只有一个，如果多次设置，只有最后一次的生效

* ask
多轮对话的bot，会通过询问用户来收集完成任务所需要的槽位信息，询问用户的特点总结为3点，ask：问一个特定的槽位。比如，打车服务收到用户的打车意图的时候，发现没有提供目的地，就可以ask destination(目的地的槽位名)：
```python
#命中打车意图rent_car.book，但是没有提供目的地
def RentCar(self):
    destination = self.get_slots('destination')
    if not destination:
        self.nlu.ask('destination')
        card = TextCard('打车去哪呢')
        return {
            'card': card,
        }
self.add_intent_handler('rent_car.book', self.RentCar)
```
* delegate
将处理交给DuerOS的对话管理模块DM（Dialog Management）,按事先配置的顺序，包括对缺失槽位的询问，槽位值的确认（如果设置了槽位需要确认，以及确认的话术）,整个意图的确认（如果设置了意图需要确认，以及确认的话术。比如可以将收集的槽位依次列出，等待用户确认）
```python
return self.nlu.set_delegate()
```
* confirm slot
主动发起对一个槽位的确认，此时还需同时返回询问的outputSpeach。主动发起的确认，DM不会使用默认配置的话术。
```python
self.nlu.set_confirm_slot('money')
return {
    'outputSpeech': '你确认充话费：10000000000',
    }
```
* confirm intent
主动发起对一个意图的确认，此时还需同时返回询问的outputSpeach。主动发起的确认，DM不会使用默认配置的话术。一般当槽位填槽完毕，在进行下一步操作之前，一次性的询问各个槽位，是否符合用户预期。
```python
money = self.get_slots('money')
phone = self.get_slots('phone')
if money and phone:
    self.nlu.set_confirm_intent()
    return {
        'outputSpeech': '你确认充话费：' + money + '，充值手机：' + phone,
    }
```
### 插件

可以使用如下命令安装:你还可以写插件(拦截器Intercept),干预对话流程、干预返回结果。比如，用户没有通过百度帐号登录，bot直接让用户去登录，不响应意图，可以使用LoginIntercept:
```python
loginIntercept = LoginIntercept()
self.addIntercept(loginIntercept)
```
开发自己的拦截器，继承Intercept,通过重载preprocess，能够在处理通过addHandler、addEventListener添加的回调之前，定义一些逻辑。通过重载postprocess能够对回调函数的返回值，进行统一的处理：
```python
class YourIntercept(Intercept):
    def preprocess(self, bot):
        '''
        bot: 你的bot实例化对象
        '''

    def postprocess(self, bot, result):
        '''
        maybe format result 
        '''
        return result
```
intercept可以定义多个，执行顺序，以调用addIntercept的顺序来执行

### <span id = "question">常见问题</span>
* 运行sh start.sh 出现 ImportError: No module named OpenSSL
执行下面命令
```
sudo pip install pyOpenSSL
```

* ImportError: No module named Crypto.PublicKey
执行下面命令
```
sudo pip install pycrypto
```

* ImportError: No module named requests
执行下面命令
```
sudo pip install requests
```
或者在根目录执行下面命令解决全部问题
```
pip install -r requirements.txt
```

# 完成过程记录

2018-01-12
* Bot.py添加错误回调，用户可以调用setCallBack方法设置错误回调方法
* 优化samples demo
* 添加个税demo数据


2018-01-06


* 完成拦截器
* 完成会话
* 完成指令处理

===========================================

### 鸣谢
[@gongqingliang821](https://github.com/gongqingliang821)

### 免责声明

* 此SDK非官网提供，纯属个人学习研究，如因使用此SDK导致的任何损失，本人概不负责


