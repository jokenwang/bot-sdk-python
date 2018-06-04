#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/6/1

"""
    desc:pass
"""
import requests

from dueros.Bot import Bot
from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.Display.Hint import Hint
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.template.BodyTemplate2 import BodyTemplate2
from dueros.directive.Display.template.ListTemplate1 import ListTemplate1
from dueros.directive.Display.template.ListTemplateItem import ListTemplateItem
from dueros.directive.Display.template.ListTemplate2 import ListTemplate2
from dueros.directive.Display.template.BodyTemplate3 import BodyTemplate3

class Bot(Bot):

    def __init__(self, data):
        super(Bot, self).__init__(data)
        self.addLaunchHandler(self.launchRequest)
        self.addIntentHandler('com.jack.dbp.express.help', self.help)
        self.addIntentHandler('com.jack.dbp.express.company', self.queryCompanies)
        self.addIntentHandler('com.jack.dbp.express.which', self.confirmCompany)
        self.addIntentHandler('com.jack.dbp.express.expressno', self.queryExpress)
        self.addEventListener('Display.ElementSelected', self.handleCompanyClick)

        pass

    def launchRequest(self):
        self.waitAnswer()
        template = self.__getHomeCard()
        speech = '欢迎使用快递查询,快递查询方便进行快递查询,您可以对我说帮助来获取帮助信息,对我说退出关闭技能'
        reprompt = '没有听懂，可以直接对我说帮助'
        hint = Hint('查询支持的快递公司')
        return {
            'outputSpeech': speech,
            'reprompt': reprompt,
            'directives': [hint, template]
        }

    def queryCompanies(self):
        self.waitAnswer()
        companies = [{'id':'1','name':'顺丰', 'logo':'http://zfs1.fiiimg.com/zfs1/fw/13/343/19738520131209103002_960x720.jpg'},
                     {'id':'2','name':'中通', 'logo':'https://cdn.kuaidi100.com/images/sz/p-2.png?version=20180521'},
                     {'id':'3','name':'EMS', 'logo':'http://h.hiphotos.baidu.com/exp/w=500/sign=ce660b919d22720e7bcee2fa4bca0a3a/b3119313b07eca80a2a99714942397dda0448391.jpg'}]
        listTemplate2 = ListTemplate2()
        listTemplate2.setToken('adfasdf')
        for company in companies:
            listTemplateItem = ListTemplateItem()
            listTemplateItem.setPlainPrimaryText(company['name'])
            listTemplateItem.setImage(company['logo'])
            listTemplateItem.setToken(company['id'])
            listTemplate2.addItem(listTemplateItem)

        listTemplate2.setBackGroundImage('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1527835685180&di=5db741cde07e06be10e607c92d2bb2b0&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Ffc1f4134970a304e3c1907c7dac8a786c9175cd7.jpg')
        template = RenderTemplate(listTemplate2)
        speech = '请问您要查询哪家快递公司的快递,例如:查询顺丰快递'
        reprompt = '没有听懂，可以直接对我说帮助'
        hint = Hint('查询顺丰快递')
        return {
            'outputSpeech': speech,
            'reprompt': reprompt,
            'directives': [hint, template]
        }

    def confirmCompany(self):
        self.waitAnswer()
        expressName = self.getSlots('expressName')
        if expressName:
            speech = '请您告诉我快递单号,例如:快递单号为123123123'
            reprompt = '没有听懂，可以直接对我说帮助'
            bodyTemplate2 = BodyTemplate2()
            bodyTemplate2.setImage('http://zfs1.fiiimg.com/zfs1/fw/13/343/19738520131209103002_960x720.jpg')
            bodyTemplate2.setBackGroundImage('http://zfs1.fiiimg.com/zfs1/fw/13/343/19738520131209103002_960x720.jpg')
            bodyTemplate2.setPlainContent('顺丰快递')
            template = RenderTemplate(bodyTemplate2)
            hint = Hint(reprompt)
            return {
                'outputSpeech': speech,
                'reprompt': reprompt,
                'directives':[hint, template]
            }
        else:
            pass
        pass

    def handleCompanyClick(self, event):

        print(event)
        pass

    def queryExpress(self):

        self.waitAnswer()
        expressNo = self.getSlots('expressNo')
        if expressNo:
            expressName = self.getSlots('expressName')
            result = self.__queryExpress('shunfeng', expressNo)
            status = result['status']
            notify = ''
            # directive = ''
            if '0' == status:
                notify = '物流单暂无结果'
                pass
            elif '2' == status:
                # 接口出现异常
                notify = '查询异常'
                pass
            else:
                datas = self.__buildResultCard(result)
                notify = datas[0]
                directive = datas[1]
            template = RenderTemplate(directive)
            hint = Hint('帮助')
            return {
                'outputSpeech': notify,
                'reprompt': notify,
                'directives': [hint,template]
            }

        else:
            pass
        pass

    def __buildResultCard(self, result):
        state = result['state']
        notify = ''
        if '0' == state:
            notify = '在途'
            #，即货物处于运输过程中'
            pass
        elif '1' == state:
            notify = '已揽件'
            #，货物已由快递公司揽收并且产生了第一条跟踪信息
            pass
        elif '2' == state:
            notify = '疑难'
            #，货物寄送过程出了问题
            pass
        elif '3' == state:
            notify = '收件人已签收'
            #，收件人已签收
            pass
        elif '4' == state:
            notify = '退签'
            #，即货物由于用户拒签、超区等原因退回，而且发件人已经签收
            pass
        elif '5' == state:
            notify = '快递正在进行同城派件'
            #，即快递正在进行同城派件
            pass
        elif '6' == state:
            notify = '货物正处于退回发件人的途中'
            #，货物正处于退回发件人的途中
            pass
        datas = result['data']
        listTemplate2 = ListTemplate2()
        listTemplate2.setToken('adfasdf')
        for express in datas:
            print(express)
            item = ListTemplateItem()
            text = '在%s, %s' % (express['ftime'], express['context'])
            item.setPlainPrimaryText(text)
            item.setToken(express['ftime'])
            listTemplate2.addItem(item)
        listTemplate2.setBackGroundImage('http://zfs1.fiiimg.com/zfs1/fw/13/343/19738520131209103002_960x720.jpg')
        return (notify, listTemplate2)


    def __queryExpress(self, expressCompany, expressNo):
        data = {'type': expressCompany, 'postid': expressNo}
        print(data)
        response = requests.request('GET', 'http://www.kuaidi100.com/query', params=data)
        result = response.json()
        return result

    def help(self):
        self.waitAnswer()
        template = self.__getHomeCard()
        speech = '欢迎使用快递查询,快递查询方便进行快递查询,您可以对我说帮助来获取帮助信息,对我说退出关闭技能'
        reprompt = '没有听懂，可以直接对我想要使用的服务，例如'
        hint = Hint('视频')
        return {
            'outputSpeech': speech,
            'reprompt': reprompt,
            'directives': [hint, template]
        }

    def __getHomeCard(self):

        token = {'page':'home'}
        IMAGE_AUDIO = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1527835685180&di=5db741cde07e06be10e607c92d2bb2b0&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Ffc1f4134970a304e3c1907c7dac8a786c9175cd7.jpg'

        bodyTemplate = BodyTemplate3()
        bodyTemplate.setTitle('快递查询')
        bodyTemplate.setToken(self.getToken(token))

        bodyTemplate.setBackGroundImage(IMAGE_AUDIO)
        bodyTemplate.setImage(IMAGE_AUDIO)
        bodyTemplate.setPlainContent('欢迎使用快递查询,快递查询方便进行快递查询,您可以对我说帮助来获取帮助信息,对我说退出关闭技能')
        directive = RenderTemplate(bodyTemplate)
        return directive

    def __getHelpCard(self):
        token = {'page': 'home'}
        IMAGE_AUDIO = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1527835685180&di=5db741cde07e06be10e607c92d2bb2b0&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Ffc1f4134970a304e3c1907c7dac8a786c9175cd7.jpg'

        bodyTemplate = BodyTemplate3()
        bodyTemplate.setTitle('快递查询')
        bodyTemplate.setToken(self.getToken(token))

        bodyTemplate.setBackGroundImage(IMAGE_AUDIO)
        bodyTemplate.setImage(IMAGE_AUDIO)
        bodyTemplate.setPlainContent('欢迎使用快递查询,快递查询方便进行快递查询,您可以对我说帮助来获取帮助信息,对我说退出关闭技能')
        directive = RenderTemplate(bodyTemplate)
        return directive



    pass


if __name__ == '__main__':
    pass