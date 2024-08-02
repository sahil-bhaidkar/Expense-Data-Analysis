import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Constants
EXPENSE_CATEGORIES = ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Rent', 'Miscellaneous']
INCOME_CATEGORIES = ['Salary', 'Investments', 'Freelance']

# Function to parse date input
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%d %m %Y')
    except ValueError:
        raise ValueError("Date format should be DD MM YYYY")

# Get date range from user
START_DATE = input("Enter the start date (DD MM YYYY): ")
END_DATE = input("Enter the end date (DD MM YYYY): ")

# Convert dates
START_DATE = parse_date(START_DATE)
END_DATE = parse_date(END_DATE)

# Generate daily periods
def generate_daily_expenses():
    data = []

    current_date = START_DATE
    while current_date <= END_DATE:
        daily_expenses = {category: np.random.randint(50, 500) for category in EXPENSE_CATEGORIES}
        daily_expenses['Date'] = current_date.strftime('%d %m %Y')
        daily_expenses['Total Expenses'] = sum(daily_expenses[cat] for cat in EXPENSE_CATEGORIES)
        data.append(daily_expenses)
        current_date += timedelta(days=1)

    return pd.DataFrame(data)

def generate_monthly_income():
    # This will create monthly income data for each month within the range
    months = pd.date_range(START_DATE, END_DATE, freq='MS').strftime("%Y-%m").tolist()
    data = []

    for month in months:
        monthly_income = {category: np.random.randint(15000, 30000) for category in INCOME_CATEGORIES}
        monthly_income['Month'] = month
        monthly_income['Total Income'] = sum(monthly_income[cat] for cat in INCOME_CATEGORIES)
        data.append(monthly_income)

    return pd.DataFrame(data)

def generate_investments():
    # This will create investment data for each month within the range
    months = pd.date_range(START_DATE, END_DATE, freq='MS').strftime("%Y-%m").tolist()
    data = []

    for month in months:
        sip_investment = np.random.randint(3000, 7000)
        gold_investment = np.random.randint(200, 500)
        data.append({'Month': month, 'SIP': sip_investment, 'Gold': gold_investment, 'Total Investment': sip_investment + gold_investment})

    return pd.DataFrame(data)

# Generate data
daily_expenses_df = generate_daily_expenses()
monthly_income_df = generate_monthly_income()
investments_df = generate_investments()

# Save to CSV
daily_expenses_df.to_csv('daily_expenses.csv', index=False)
monthly_income_df.to_csv('monthly_income.csv', index=False)
investments_df.to_csv('investments.csv', index=False)

print("Dummy data for the specified period has been created and saved to CSV files.")
