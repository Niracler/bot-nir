# coding=utf8
import json
import threading
from time import sleep, time


class Information():
    # 构造函数,关于基本配置,文件读档
    def __init__(self, last_time):
        # 数据成员
        self.items = {}  # 一个自定义规则的字典
        self.status = '本人离线中，可能要等一段时间再能回复\n'
        self.statusFlag = True
        self.tulingBot = False
        self.tulingBot_Group = False
        self.tulingBot_Telegram = False
        self.last_time = last_time
        self.time = '1000'
        self.help = '关于各种命令\n' \
                    + '/help: 该帮助文档\n' \
                    + '/phone：获取本人电话号码\n' \
                    + '/test：调教Bot\n' \
                    + '/tuling:呼叫图灵机器人 \n' \
                    + '/killTuling:赶走图灵机器人\n\n' \
                    + '项目主页：github.com/Niracler/nirBot\n'

        # 从文件中，读取自定义规则
        try:
            with open('keyWord.json') as f:
                self.items = json.load(f)
        except:
            self.items = {}


info = Information(time())


def wait():
    while (True):
        sleep(int(info.time))
        with open('keyWord.json', 'w') as f: f.write(json.dumps(info.items))


t = threading.Thread(target=wait)  # 多线程计算时间五分钟
t.setDaemon(True)  # 后台进程,定时操作
t.start()
