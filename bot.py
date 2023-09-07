from config import load_config

config = load_config(path=None)

print('bot_token = ', config.tg_bot.token)
print('admin_ids = ', config.tg_bot.admin_ids)
print('\n')
print('db_name = ', config.db.database)
print('db_host = ', config.db.db_host)
print('db_user = ', config.db.db_user)
print('db_password = ', config.db.db_password)