import itchatmp
from itchatmp.content import TEXT

itchatmp.update_config(itchatmp.WechatConfig(
    token='myniracler123',
    appId='wx99b26a5cca5da7f8',
    appSecret='77dd28bab1cb0383d5b8b8b4f63e5728'))


@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    return msg['Content']


itchatmp.run()
