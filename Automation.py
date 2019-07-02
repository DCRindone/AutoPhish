from gophish import *
from gophish.models import *
from datetime import datetime as dt
import datetime
import urllib3
import Report
from pathlib import Path


# Gain access to GoPhish
api_key = 'c21434defd36f0158cb2803b2947cfec1bb0dd52296d9e645c41ecbbf4bdc27c'
urllib3.disable_warnings()
api = Gophish(api_key, host='https://127.0.0.1:3333/', verify=False)


# Read in file:
def populate_users(file):
    # Creates Group Name
    group_name_list = []
    for char in file:
        if char != '.':
            group_name_list.append(char)
        else:
            break
    group_name_string = "".join(group_name_list)

    # Check to make sure group does not already exist
    exists = False
    for group in api.groups.get():
        if group.name == group_name_string:
            print("group name already exists")
            exists = True

    # Open File/Removes Header/Generate users
    home = str(Path.home())
    targets = []
    file_path = (r'{}\Desktop\GoPhish\New Groups\{}').format(home, file)
    f = open(file_path, 'r')
    lines = f.readlines()[1:]
    for line in lines:
        fields = line.strip().split(",")
        first, last, email_ad, pos = fields
        print(first, last, email_ad, pos)
        targets.append(User(first_name=first, last_name=last, email=email_ad, position=pos))
    f.close()

    # posts group to Gophish
    grp_id = 1
    for group in api.groups.get():
        if group.id == grp_id:
            grp_id += 1
    group = Group(name=group_name_string, targets=targets, id=grp_id)
    try:
        api.groups.post(group)
        return group_name_string, grp_id, exists
    except:
        print("error, Group pre-exists")
        return group_name_string, grp_id, exists


def campaign_time(group_id):
    x = 0
    group = api.groups.get(group_id=group_id)
    for target in group.targets:
        x += 1
    cam_time = int(x/2)
    return cam_time


def get_group_camp_len(group_name):
    for group in api.groups.get():
        if group.name == group_name:
            return campaign_time(group.id)


def launch_campaign(group_name, email_name, sender_name):
    # Gather info to create Campaign
    campaign_time = get_group_camp_len(group_name)
    groups = [Group(name=group_name)]
    page = Page(name='Google')
    template = Template(name=email_name)
    smtp = SMTP(name=sender_name)
    launch = dt.now(tzlocal())
    send_by = launch + datetime.timedelta(days=campaign_time)
    # url = 'https://127.0.0.1:3333'     # url = 'http://phishing_server'    # url = 'https://127.0.0.1:3333'

    # String for titling launch
    temp_date_launch = str(launch)
    temp_date_list = temp_date_launch.split(" ")
    launch_date = temp_date_list[0]

    # launch Campaign
    campaign = Campaign(name=str(group_name + " " + launch_date), launch_date=launch, send_by_date=send_by,
                        groups=groups, page=page, template=template, smtp=smtp)
    api.campaigns.post(campaign)
    return True


def main():
    user_in = input("Enter campaign ID")
    Report.get_report(user_in)


if __name__ == '__main__':
    main()
