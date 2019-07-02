from gophish import *
import urllib3

# Gain access to GoPhish
api_key = 'c21434defd36f0158cb2803b2947cfec1bb0dd52296d9e645c41ecbbf4bdc27c'
urllib3.disable_warnings()
api = Gophish(api_key, host='https://127.0.0.1:3333/', verify=False)


def get_grp_info():
    # Get group name and size
    active_groups = []
    for group in api.groups.get():
        active_groups.append(group.name)
        # print('{} has {} users'.format(group.name, len(group.targets)))
    return active_groups


def get_email_info():
    # Iterate through Email Templates
    active_templates = []
    for i in api.templates.get():
        active_templates.append(i.name)
    return active_templates


def get_sender_info():
    # Iterate through Senders
    active_senders = []
    for i in api.smtp.get():
        active_senders.append(i.name)
    return active_senders


def get_campaign_info():
    # Iterate through Current Campaigns
    active_campaigns = []
    for i in api.campaigns.get():
        campaigns_name_and_id = []
        campaigns_name_and_id.append(i.name)
        campaigns_name_and_id.append(i.id)
        active_campaigns.append(campaigns_name_and_id)
    return active_campaigns

    # TODO ask if Phishbowl is only landing page
