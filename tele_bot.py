from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import json


def start(update, context):
    """Inform user about what this bot can do"""
    update.message.reply_text("Hello! How are you?\n to get India's Covid-19 report type /India \n to get Maharashtra's Covid-19 report type /Maharashtra")

def India(update, context):
	response = requests.get('https://covid-19india-api.herokuapp.com/v2.0/country_data')
	result_data = json.loads(response.text)
	res = f"""Total confirmed cases - {result_data[1]['confirmed_cases']}
			  Active cases - {result_data[1]['active_cases']}
			  Discharged/ Cured - {result_data[1]['recovered_cases']}
			  Death - {result_data[1]['death_cases']}
			  Recovery rate - {result_data[1]['recovered_rate']}%"""

	update.message.reply_text(res)		  

def Maharashtra(update, context):
	response = requests.get('https://covid-19india-api.herokuapp.com/v2.0/state_data')
	result_data = json.loads(response.text)
	all_report = ''
	for state in result_data[1]['state_data']:
		if state['state'] == 'Maharashtra':
			all_report += f"""Total confirmed cases - {state['confirmed']}
							  Active cases - {state['active']}
							  Discharged/ Cured - {state['recovered']}
							  Death - {state['deaths']}
							  Recovery rate - {state['recovered_rate']}%"""
	update.message.reply_text(all_report)
						  
def main():
    #import pdb;pdb.set_trace()
    updater = Updater('YOUR TELEGRAM TOKEN',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('India', India))
    dp.add_handler(CommandHandler('Maharashtra', Maharashtra))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
