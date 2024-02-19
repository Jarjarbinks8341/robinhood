import robin_stocks.robinhood as robin
import pyotp
import json
import sys
import datetime
import sqlite3

def getCred():
	with open('./userinfo/cred.json', 'r') as f:
		data = json.load(f)
	return data

def getConfig():
	with open('./userinfo/config.json', 'r') as f:
		data = json.load(f)
	return data

def quote(ticker):
	r = robin.get_latest_price(ticker)
	return str(r[0])

def buy(ticker, ammount):
	r = robin.order_buy_market(ticker, ammount)
	return r

def sell(ticker, ammount):
	r = robin.order_sell_market(ticker, ammount)
	return r

def deposit(ammount):
	bank_accounts = robin.get_linked_bank_accounts()
	account_names = robin.filter_data(bank_accounts, 'bank_account_nickname')
	ach_relationship = bank_accounts[0]['url']
	deposit   = robin.deposit_funds_to_robinhood_account(ach_relationship, 500)
	return deposit

def withdraw(ammount):
	bank_accounts = robin.get_linked_bank_accounts()
	account_names = robin.filter_data(bank_accounts, 'bank_account_nickname')
	ach_relationship = bank_accounts[0]['url']
	withdrawl = robin.withdrawl_funds_to_bank_account(ach_relationship, 10)
	return withdrawl

def showHoldings():
	my_stocks = robin.build_holdings()
	for key,value in my_stocks.items():
		print(key,value)

def checkHoliday(today):
    holiday_2024 = {"2024-01-01", "2024-01-15", "2024-02-19", "2024-03-29", "2024-05-27", "2024-06-19", "2024-07-04", "2024-09-02", "2024-11-28", "2024-12-25"}
    holiday_2025 = {"2025-01-01", "2025-01-20", "2025-02-17", "2025-04-18", "2025-05-26", "2025-06-19", "2025-07-04", "2025-09-01", "2025-11-27", "2025-12-25"}
    holiday_2026 = {"2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25", "2026-06-19", "2026-07-03", "2026-09-07", "2026-11-26", "2026-12-25"}
    weekday_number = today.weekday()
    if weekday_number == 5 or weekday_number == 6:
        return False
    current_year = today.year
    if current_year == "2024": 
        if today in holiday_2024:
            return True
    elif current_year == "2025":
        if today in holiday_2025:
            return True
    elif current_year == "2026":
        if today in holiday_2026:
            return True
    else:
        return False

def get_current_year_and_week(today):
    # Get the current date
    # Get ISO year and ISO week number
    iso_year, iso_week, _ = today.isocalendar()
    # Create a string representing the year and week
    year_week_string = f"{iso_year}_W{iso_week:02d}"
    return year_week_string



# read credential infomation
cred = getCred()
code = cred['Code']

# read config metadata
config = getConfig()

# load config
budget = config['Budget']
stocks = config['Stocks']

totp = pyotp.TOTP(cred['Key']).now()
login = robin.login(cred['Email'], cred['Password'], mfa_code=totp)

print(quote('AAPL'))
print(budget)
print(stocks)

today = datetime.date.today()
weekday_number = today.weekday()
print(today)
print(checkHoliday(today))

year_week_string = get_current_year_and_week(today)
print("Current Year and Week:", year_week_string)
