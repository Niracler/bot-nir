# coding=utf8
import time
import threading
from tuling import get_response  # 图灵机器人,https://github.com/Niracler/myChat/blob/master/tuling.py
import itchat
from itchat.content import *
from informatiom import info  # 关于信息的类,https://github.com/Niracler/myChat/blob/master/informatiom.py


# 当接到文字消息的时候的动作
@itchat.msg_register('Text')
def text_reply(msg):
    # help，以及code
    if u'/help' == msg['Text'] or u'help' == msg['Text']:
        msg.user.send(u'Bot:' + info.help)
        return

    # 关于图灵机的启动与关闭
    if u'/tuling' == msg['Text']:
        msg.user.send(u'Bot:M醬,出来吧')
        info.tulingBot = True
        return
    elif u'/killTuling' == msg['Text']:
        msg.user.send(u'Bot:M醬,可以走了')
        info.tulingBot = False
        return
    elif info.tulingBot == True:
        msg.user.send(('M醬:' + get_response(msg['Text'])) or u'bot：M醬不在')
        return

    # 自定义回复内容
    if msg['Text'] in info.items.keys():
        msg.user.send('Bot:' + info.items[msg['Text']])
        return

    # 调试模式
    if u'/test' in msg['Text']:
        test, from_str, to_str = map(str, msg['Text'].split())
        info.items[from_str] = to_str  # 这已经是互异的了
        msg.user.send(u'Bot:指令录入成功')
        return

    # 时间模式,只对自己有用
    if u'/time' in msg['Text'] and msg['ToUserName'] == 'filehelper':
        time0, info.time = map(str, msg['Text'].split())
        msg.user.send(u'Bot:成功设定时间')
        msg.user.send(u'Bot:' + info.time)

    # 状态模式,只对自己有用
    if u'/status' in msg['Text'] and msg['ToUserName'] == 'filehelper':
        test, info.status = map(str, msg['Text'].split())
        msg.user.send('Bot:成功设定状态')
        msg.user.send('Bot:' + info.time)

    # 状态中,向对方表示自己的状态
    if ((time.time() - info.last_time) > int(info.time)):
        info.last_time = time.time()
        return 'Bot:' + info.status

        # 记录最后通话时间
    info.last_time = time.time()


# 对于文件之类的操作
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return ('@%s@%s' % (typeSymbol, msg.fileName))


# 添加朋友时的动作
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(info.help, msg['RecommendInfo']['UserName'])


# 在组内回复的动作
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    # 关于图灵机的启动与关闭
    if u'/tuling' == msg['Text']:
        msg.user.send(u'Bot:M醬,出来吧')
        info.tulingBot_Group = True
        return
    elif u'/killTuling' == msg['Text']:
        msg.user.send(u'Bot:M醬,可以走了')
        info.tulingBot_Group = False
        return
    elif info.tulingBot_Group == True:
        msg.user.send(('M醬:' + get_response(msg['Text'])) or u'bot：M醬不在')
        return


def main():
    # 微信机器人启动
    # itchat.auto_login(True)
    itchat.auto_login(True, enableCmdQR=2)
    itchat.run()


if __name__ == '__main__':
    main()

wechat_bot = threading.Thread(target=main)
# wechat_bot.setDaemon(True)# 将其设置为后台进程
