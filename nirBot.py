import time
from informatiom import info
from tuling import get_response


def get_nir_response(message):
    # help，以及code
    if u'/help' == message or u'help' == message:
        return (u'Bot:' + info.help)

    # 关于图灵机的启动与关闭
    if u'/tuling' == message:
        info.tulingBot = True
        return (u'M醬:你好,我是M醬')
    elif u'/killTuling' == message:
        info.tulingBot = False
        return (u'M醬:我这就走')
    elif info.tulingBot == True:
        return ('M醬:' + get_response(message)) or u'bot：M醬不在'

    # 自定义回复内容
    if message in info.items.keys():
        return ('Bot:' + info.items[message])

    # 调试模式
    if u'/test' in message:
        test, from_str, to_str = map(str, message.split())
        info.items[from_str] = to_str  # 这已经是互异的了
        return (u'Bot:指令录入成功')

    # 时间模式,只对自己有用
    if u'/time' in message:
        time0, info.time = map(str, message.split())
        return (u'Bot:成功设定时间 ' + info.time)

    # 状态模式,只对自己有用
    if u'/status' in message:
        test, info.status = map(str, message.split())
        return ('Bot:成功设定状态 ' + info.time)

    # 状态中,向对方表示自己的状态
    if ((time.time() - info.last_time) > int(info.time)):
        info.last_time = time.time()
        return 'Bot:' + info.status

    # 记录最后通话时间
    info.last_time = time.time()

    # 对作业的操作
    if '/add' in message:
        course_name = message.split()[1]

        homework = ''
        for row in message.split('\n')[1:]:
            homework = homework + '\n' + row

        info.homework[course_name] = homework
        return (course_name + homework)

    if '/del' in message:
        info.homework.pop(str(message.split()[1]))
        return "Bot:成功删除"

    if '/homework' == message:
        homework = ""
        cow = ""
        for cow in info.homework:
            homework = homework + cow
            homework = homework + info.homework[cow]
            homework += "\n\n"

        return homework
