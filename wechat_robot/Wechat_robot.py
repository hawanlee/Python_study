from wxpy import *

# tuling123 api_key f83a626d7d2b4b7d9b390ea898a33742
bot = Bot()
bot.cache_path = True
bot.enable_puid('wxpy_puid.pkl')
# Bot.auto_mark_as_read = True
# myself = bot.self
# bot.self.add()
# bot.self.accept()
# bot.self.send('Can you receive?')
# bot.file_helper.send('Hello from wxpy!')
my_friend = bot.friends().search('')[0]
my_friend.send('我现在是个机器人，可以问我任何问题(虽然答案会有点傻)')
my_friend.send(':）')
tuling = Tuling(api_key='f83a626d7d2b4b7d9b390ea898a33742')


@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)


embed()
