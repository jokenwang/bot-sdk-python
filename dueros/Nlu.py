#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

from dueros.Base import Base

class Nlu(Base):
    '''

    '''

    def __init__(self, data):
        super(Nlu, self).__init__()
        self.data = data
        self.askSlot = None
        self.directive = None

    def getIntentName(self, index=0):
        '''
        获取当前的意图intent名
        :return:
        '''

        return self.data[index]['name'] if 'name' in self.data[index] else ''

    def setSlot(self, field, value, index=0):
        '''
        设置槽位信息
        desc 设置slot, 如果不存在,新增一个solt
        :param field:   槽位名
        :param value:   槽位值
        :param index:   第几组slot
        :return:
        '''

        if not field:
            return

        slots = self.data[index]['slots']

        if field in slots:
            self.data[index]['slots'][field]['value'] = value
        else:
            self.data[index]['slots'][field] = {
                'name': field,
                'value': value
            }

    def getSlot(self, field, index=0):

        '''
        获取槽位
        @desc 获取一个槽位slot的值
        :param field:
        :param index:
        :return:
        '''

        '''
            intent:[
                {
                   "slots": {
                        "{{STRING}}": {
                            "name": "{{STRING}}",
                            "value": ["{{STRING}}"],
                            "confirmationStatus": "{{STRING}}"
                        }
                    }
                },{
                .....
                } 
            ]
        '''
        if not field:
            return ''
        # #此处有坑 文档是values 但是PHP demo是value
        return self.__getSlotValueByKey(field, 'value', index)

    def getSlotConfirmationStatus(self, field, index=0):
        '''
        槽位确认状态
        :param field:
        :param index:
        :return:    NONE: 未确认；CONFIRMED: 确认；DENIED: 否认
        '''
        return self.__getSlotValueByKey(field, 'confirmationStatus', index)

    def getIntentConfirmationStatus(self, index=0):
        '''
        获取意图的确认状态
        :param index:
        :return:    NONE: 未确认；CONFIRMED: 确认；DENIED: 否认
        '''
        return self.data[index]['confirmationStatus'] if 'confirmationStatus' in self.data[index] else ''

    def __getSlotValueByKey(self, field, subField, index=0):
        '''
        :param field:
        :param subField:
        :param index:
        :return:
        '''

        if not ('slots' in self.data[index]):
            return ''
        slots = self.data[index]['slots']
        if field in slots:
            return slots[field][subField]
        else:
            return None

    def hasAsked(self):
        '''
        是否询问过用户
        :return:
        '''
        if self.directive:
            return True
        else:
            return False

    def ask(self, slot):
        '''
        询问一个特定的槽位
        :param slot:
        :return:
        '''

        if slot and slot != '':
            self.askSlot = slot
            self.directive = {
                'type': 'Dialog.ElicitSlot',
                'slotToElicit': slot,
                'updatedIntent': self.__getUpdateIntent()
            }
        else:
            return

    def toDirective(self):
        '''
        打包NLU交互协议，返回DuerOS，为第二轮用户回答提供上下文
        在Response 中被调用
        :return:
        '''
        return self.directive

    def __getUpdateIntent(self):
        '''
        构造返回的update intent 数据结构
        :return:
        '''

        if 'slots' in self.data[0]:
            return {
                'name': self.getIntentName(),
                'slots': self.data[0]['slots']
            }
        else:
            return {
                'name': self.getIntentName(),
                'slots': {}
            }

    def toUpdateIntent(self):
        '''
        bot可以修改intent中对应的值，返回给DuerOs更新
        在Response 中被调用
        :return:
        '''

        if self.data[0]:
            return {
                'intent': self.data[0]
            }
        else:
            return {
                'intent': {}
            }

    def setDelegate(self):
        '''
        设置delegate 某个槽位或确认意图
        :return:
        '''
        self.directive = {
            'type': 'Dialog.Delegate',
            'updatedIntent': self.__getUpdateIntent()
        }

    def setConfirmSlot(self, field):
        '''
        设置对一个槽位的确认
        :param field:
        :return:
        '''

        if 'slots' in self.data[0]:
            slots = self.data[0]['slots']
            if field in slots:
                self.directive = {
                    'type': 'Dialog.ConfirmSlot',
                    'slotToConfirm': field,
                    'updatedIntent': self.__getUpdateIntent()
                }

    def setConfirmIntent(self):
        '''
        设置confirm 意图。询问用户是否对意图确认，设置后需要自行返回outputSpeech
        :return:
        '''
        self.directive = {
            'type': 'Dialog.ConfirmIntent',
            'updatedIntent': self.__getUpdateIntent()
        }


if __name__ == '__main__':
    pass
