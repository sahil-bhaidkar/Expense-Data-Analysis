import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Constants
INCOME_CATEGORIES = ['Salary', 'Investments', 'Freelance']
EXPENSE_CATEGORIES = ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Rent', 'Miscellaneous']

# Get date range from user
START_DATE = input("Enter the start date (YYYY-MM-DD): ")
END_DATE = input("Enter the end date (YYYY-MM-DD): ")

# Generate date ranges
NUM_DAYS = (datetime.strptime(END_DATE, '%Y-%m-%d') - datetime.strptime(START_DATE, '%Y-%m-%d')).days + 1
MONTHS = pd.date_range(START_DATE, END_DATE, freq='MS').strftime("%Y-%m").tolist()

# Helper functions
def generate_daily_expenses():
    dates = pd.date_range(START_DATE, END_DATE, freq='D')
    data = []

    for date in dates:
        daily_expenses = {category: np.random.randint(50, 500) for category in EXPENSE_CATEGORIES}
        daily_expenses['Date'] = date
        daily_expenses['Total'] = sum(daily_expenses.values())
        data.append(daily_expenses)

    return pd.DataFrame(data)

def generate_monthly_income():
    data = []

    for month in MONTHS:
        monthly_income = {category: np.random.randint(15000, 30000) for category in INCOME_CATEGORIES}
        monthly_income['Month'] = month
        monthly_income['Total'] = sum(monthly_income.values())
        data.append(monthly_income)

    return pd.DataFrame(data)

def generate_investments():
    dates = pd.date_range(START_DATE, END_DATE, freq='D')
    data = []

    for date in dates:
        sip_investment = 500  # Fixed SIP amount
        gold_investment = 20  # Fixed daily gold investment
        data.append({'Date': date, 'SIP': sip_investment, 'Gold': gold_investment, 'Total Investment': sip_investment + gold_investment})

    return pd.DataFrame(data)

# Generate data
daily_expenses_df = generate_daily_expenses()
monthly_income_df = generate_monthly_income()
investments_df = generate_investments()

# Save to CSV
daily_expenses_df.to_csv('daily_expenses.csv', index=False)
monthly_income_df.to_csv('monthly_income.csv', index=False)
investments_df.to_csv('investments.csv', index=False)

print("Dummy data has been created and saved to CSV files.")
