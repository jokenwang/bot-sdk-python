# bot-sdk 变更记录
1、fix DPL显示BUG
2、fix DPL点击问题
***
1、新增DPL支持
***
1、可以将技能数据上送到第三方统计平台
2、**Bot内属性改为私有，会影响到以前代码(如果技能使用了Bot内的属性)**
***
1、方便使用SDK授权功能，SDK会自己完成授权
***
* Bot.py 新增功能  
1、新增获取SessionEndedRequest结束原因回调   
2、新增获取设备ID, 添加屏幕选择事件回调、屏幕点击回调   
3、方便快速开发，新增了各种通用意图的回调设置      
4、新增权限事件回调

***
* 更新Permission
* directives指令排序方式
* 增加设备VideoPlayer分辨率
* 增加UI CONTROL支持

***
* Request新增获取apiAccessToken方法
* Bot 新增添加权限回调方法
* 修复权限bug

***
* 优化日志功能
* 优化数据统计功能

***
* 增加Display.PushStack指令
* 增加expectResponse
* 增加Record.RecordSpeech指令
* 增加Permission.AskForPermissionsConsent指令

*** 
* 增加列表标签Tag
* 增加BodyTemplate6
* 增加ListTemplate3
* 增加ListTemplate4
* 增加RenderVideoPlayerInfo
* 增加RenderAudioPlayerInfo