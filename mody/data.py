from mody.yad import Bot
from mody.Redis import db

bot_id = Bot.me.id

def add_user(user_id: int):
    if is_user(user_id):
        return
    db.sadd(f"botusers{bot_id}", user_id)

def is_user(user_id: int) -> bool:
    try:
        users = get_users()
        return user_id in users
    except:
        return False

def del_user(user_id: int) -> bool:
    if not is_user(user_id):
        return False
    db.srem(f"botusers{bot_id}", user_id)
    return True

def get_users() -> list:
    try:
        users = []
        for user_id in db.smembers(f"botusers{bot_id}"):
            users.append(int(user_id))
        return users
    except:
        return []

def get_users_backup() -> str:
    text = ''
    for user in db.smembers(f"botusers{bot_id}"):
        text += user + '\n'
    with open('users.txt', 'w+') as f:
        f.write(text)
    return 'users.txt'

def add_admin(user_id: int):
    if is_admin(user_id):
        return
    db.sadd(f"bot_admins{bot_id}", user_id)

def is_admin(user_id: int) -> bool:
    try:
        admins = get_admins()
        return user_id in admins
    except:
        return False

def del_admin(user_id: int) -> bool:
    if not is_admin(user_id):
        return False
    db.srem(f"bot_admins{bot_id}", user_id)
    return True

def get_admins() -> list:
    try:
        admins = []
        for admin_id in db.smembers(f"bot_admins{bot_id}"):
            admins.append(int(admin_id))
        return admins
    except:
        return []

def get_admins_backup() -> str:
    text = ''
    for admin in db.smembers(f"bot_admins{bot_id}"):
        text += admin + '\n'
    with open('admins.txt', 'w+') as f:
        f.write(text)
    return 'admins.txt'

def add_group(chat_id: int):
    if is_group(chat_id):
        return
    db.sadd(f"botgroups{bot_id}", chat_id)

def is_group(chat_id: int) -> bool:
    try:
        groups = get_groups()
        return chat_id in groups
    except:
        return False

def del_group(chat_id: int) -> bool:
    if not is_group(chat_id):
        return False
    db.srem(f"botgroups{bot_id}", chat_id)
    return True

def get_groups() -> list:
    try:
        groups = []
        for group_id in db.smembers(f"botgroups{bot_id}"):
            groups.append(int(group_id))
        return groups
    except:
        return []

def get_groups_backup() -> str:
    text = ''
    for group in db.smembers(f"botgroups{bot_id}"):
        text += group + '\n'
    with open('groups.txt', 'w+') as f:
        f.write(text)
    return 'groups.txt'

def check(id):
    if is_admin(id):
        return True
    if id == int(db.get(f"bot_owner{bot_id}")):
        return True
    else:
        return False