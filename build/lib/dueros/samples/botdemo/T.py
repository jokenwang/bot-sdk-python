#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/31

"""
    desc:pass
"""
import json
import base64


class T:

    def __loadData(self):
        with open("./data.json", 'r', encoding='utf-8') as load_f:
            return load_f.read()

    def getPlayList(self, type):
        list = json.loads(self.__loadData())
        func = lambda list, element: list[element] if element in list and list[element] else ''

        if type == "video":
            return func(list,"video")

        if type =="audio":
            return func(list, "audio")
        return list

    pass

    def getDetailBy(self, datatype, element, value):

        if 'video' == datatype:
            videoList = self.getPlayList(datatype)
            if videoList and type(videoList) == list:
                for video in videoList:
                    temp = ''
                    if element in video:
                        temp = video[element]
                    if temp == value:
                        return video

        if 'audio' == datatype:
            audioList = self.getPlayList(datatype)
            if audioList and type(audioList) == list:
                for audio in audioList:
                    temp = ''
                    if element in audio:
                        temp = audio[element]
                    if temp == value:
                        return audio

        return False


if __name__ == '__main__':

    t = T()
    print(t.getPlayList('videow'))
    # video = t.getDetailBy('video','title','告白气球')
    # print(video)
    audio ={}
    func = lambda audio, element: audio[element] if element in audio and audio[element] else ''
    # print(func({'id':'aaa', 'name':'asdfasd'},'name'))

    tt = "'id':'aaa', 'name':'adfads'"
    ta = json.JSONEncoder.encode(tt)
    print(ta)
    jjj = base64.encodebytes(bytes(str(ta), 'utf8'))

    print(str(jjj))
    print(base64.decodebytes(jjj))
    pass