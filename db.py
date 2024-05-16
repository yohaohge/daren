import datetime
import os.path
from collections import defaultdict
import pickle

ph_creators = defaultdict(dict)
if os.path.exists("ini/ph_creator.pickle"):
    with open("ini/ph_creator.pickle", "rb") as f:
        ph_creators = pickle.load(f)
print(ph_creators)

vn_creators = defaultdict(dict)
if os.path.exists("ini/vn_creator.pickle"):
    with open("ini/vn_creator.pickle", "rb") as f:
        vn_creators = pickle.load(f)

my_creators = defaultdict(dict)
if os.path.exists("ini/my_creator.pickle"):
    with open("ini/my_creator.pickle", "rb") as f:
        my_creators = pickle.load(f)

th_creators = defaultdict(dict)
if os.path.exists("ini/th_creators.pickle"):
    with open("ini/th_creator.pickle", "rb") as f:
        th_creators = pickle.load(f)

sg_creators = defaultdict(dict)
if os.path.exists("ini/sg_creator.pickle"):
    with open("ini/sg_creator.pickle", "rb") as f:
        sg_creators = pickle.load(f)

nation_map = {
    "PH": ph_creators,
    "VN": vn_creators,
    "MY": my_creators,
    "TH": th_creators,
    "SG": sg_creators
}

file_map = {
    "PH": "ini/ph_creator.pickle",
    "VN": "ini/vn_creator.pickle",
    "MY": "ini/my_creator.pickle",
    "TH": "ini/th_creator.pickle",
    "SG": "ini/sg_creator.pickle"
}


def save(nation):
    file = nation_map[nation]
    if not file:
        print("错误的国家")
        return
    obj = nation_map[nation]

    with open(file_map[nation], "wb") as f:
        pickle.dump(obj, f)


def get_file_name(nation):
    if nation_map not in nation_map:
        return {}
    return nation_map[nation]


def get_obj_by_nation(nation):
    if nation not in nation_map:
        return {}
    return nation_map[nation]


def add_creator(name: str, category: str, fans: int, views: int, gmp: str, nation: str):
    creators = get_obj_by_nation(nation)
    if name in creators:
        print("已经收集过该达人了", name)
        return

    creators[name] = {
        "name": name,
        "category": category,
        "fans": fans,
        "views": views,
        "gmp": gmp,
        "nation": nation,
    }
    nation_map[nation] = creators
    save(nation)


def get_creator(nation: str):
    return get_obj_by_nation(nation)


class UserData:
    nation_creator_map = defaultdict(dict)


user_data_manager = defaultdict(UserData)


def load_from_file(current_user: str):
    user_data = UserData()

    user_file_prefix = "user_data/%s" % current_user
    if not os.path.exists("user_data/%s" % current_user):
        os.mkdir("user_data/%s" % current_user)

    nation_file_map = {
        "PH": "ph_user.pickle",
        "VN": "vn_user.pickle",
        "MY": "my_user.pickle",
        "TH": "th_user.pickle",
        "SG": "sg_user.pickle"
    }

    for key in nation_file_map:
        file_path = user_file_prefix + "/" + nation_file_map[key]
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                user_data.nation_creator_map[key] = pickle.load(f)
        else:
            user_data.nation_creator_map[key] = {}
    user_data_manager[current_user] = user_data


def save_user_data(current_user: str, nation: str):
    nation_file_map = {
        "PH": "ph_user.pickle",
        "VN": "vn_user.pickle",
        "MY": "my_user.pickle",
        "TH": "th_user.pickle",
        "SG": "sg_user.pickle"
    }
    user_file_prefix = "user_data/%s" % current_user
    file_path = user_file_prefix + "/" + nation_file_map[nation]

    with open(file_path, "wb") as f:
        pickle.dump(user_data_manager[current_user].nation_creator_map[nation], f)


def update_invite(name, nation, current_user):
    if current_user not in user_data_manager:
        load_from_file(current_user)

    user_data = user_data_manager[name]
    if name not in user_data.nation_creator_map[nation]:
        user_data.nation_creator_map[nation][name] = {
            "last_invite_time": datetime.datetime.now().strftime("%Y%m%d"),
            "last_msg_time": "",
        }
    else:
        user_data.nation_creator_map[nation][name]["last_invite_time"] = datetime.datetime.now().strftime("%Y%m%d")
    save_user_data(current_user, nation)

def update_send_msg(name, nation, current_user):
    if current_user not in user_data_manager:
        load_from_file(current_user)

    user_data = user_data_manager[name]
    if name not in user_data.nation_creator_map[nation]:
        user_data.nation_creator_map[nation][name] = {
            "last_msg_time": datetime.datetime.now().strftime("%Y%m%d"),
            "last_invite_time": ""
        }
    else:
        user_data.nation_creator_map[nation][name]["last_msg_time"] = datetime.datetime.now().strftime("%Y%m%d")

    save_user_data(current_user, nation)