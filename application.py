from flask import Flask, request
from flask import render_template
import StartGophish
import GetGophishInformation
import Automation
import Report
import sys
import os


sys.path.append("/opt/python/current/app/Gophish_html")

application = Flask(__name__)


# Start Page
@application.route('/', methods=["POST", "GET"])
def home():
    StartGophish.open_web_browser()
    StartGophish.open_program()
    return render_template('main_menu.html', groups=GetGophishInformation.get_grp_info(),
                           campaigns=GetGophishInformation.get_campaign_info(),
                           templates=GetGophishInformation.get_email_info(),
                           senders=GetGophishInformation.get_sender_info())


# Redirect to new group campaign launched
@application.route('/new-group-campaign-launched', methods=["POST", "GET"])
def newGroupCampLaunched():
    if request.method == "POST":
        user_file = request.form.get('fileupload')
        user_template = request.form.get('emailTemplates')
        user_sender = request.form.get('senders')
        group_string, grp_id, exists = Automation.populate_users(user_file)
        if exists:
            return render_template('groupPreExists.html')
        else:
            Automation.launch_campaign(group_string, user_template, user_sender)
    return render_template('newUserGroupCampaign.html')


# Redirect to Pre-Existing group campaign launch
@application.route('/pre-existing-campaign-launched', methods=["POST", "GET"])
def preExistCampLaunched():
    if request.method == "POST":
        user_group = request.form.get('groups')
        user_template = request.form.get('emailTemplates')
        user_sender = request.form.get('senders')
        Automation.launch_campaign(user_group, user_template, user_sender)
    return render_template('preExistCampLaunched.html')


# Redirect to Get Results launch
@application.route('/retrieve-results', methods=["POST", "GET"])
def retrieveResults():
    if request.method == "POST":
        user_campaign = request.form.get('campaigns')
        Report.get_report(user_campaign)
    return render_template('getResults.html')


if __name__ == '__main__':
    application.run(host="0.0.0.0")
