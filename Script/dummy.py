import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Constants
EXPENSE_CATEGORIES = ['Entertainment', 'Rent', 'Miscellaneous']
INCOME_CATEGORIES = ['Salary', 'Investment', 'Freelance', 'Other']

# Function to parse date input
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%d-%m-%Y')
    except ValueError:
        raise ValueError("Date format should be DD-MM-YYYY")

# Get date range from user
START_DATE = input("Enter the start date (DD-MM-YYYY): ")
END_DATE = input("Enter the end date (DD-MM-YYYY): ")

# Convert dates
START_DATE = parse_date(START_DATE)
END_DATE = parse_date(END_DATE)

# Function to generate daily expenses
def generate_daily_expenses():
    data = []
    current_date = START_DATE
    expense_descriptions = ['Concert', 'Monthly rent', 'Donation', 'Movies']
    
    while current_date <= END_DATE:
        if np.random.rand() > 0.5:  # Randomly decide if there's an expense on that day
            expense_type = np.random.choice(EXPENSE_CATEGORIES)
            amount = np.round(np.random.uniform(50, 500), 2)
            description = np.random.choice(expense_descriptions)
            data.append({
                'Date': current_date.strftime('%d-%m-%Y'),
                'Expense Type': expense_type,
                'Amount': amount,
                'Description': description
            })
        current_date += timedelta(days=1)

    return pd.DataFrame(data)

# Function to generate income
def generate_income():
    data = []
    income_descriptions = ['Bonus', 'Dividends', 'Consulting', 'Interest', 'Gift']

    current_date = START_DATE
    while current_date <= END_DATE:
        if current_date.day == 7:
            data.append({
                'Date': current_date.strftime('%d-%m-%Y'),
                'Income Type': 'Salary',
                'Amount': np.round(np.random.uniform(3000, 4000), 2),
                'Description': 'Bonus'
            })
        elif np.random.rand() > 0.7:  # Randomly decide if there's an income on that day
            income_type = np.random.choice(INCOME_CATEGORIES)
            amount = np.round(np.random.uniform(200, 5000), 2)
            description = np.random.choice(income_descriptions)
            data.append({
                'Date': current_date.strftime('%d-%m-%Y'),
                'Income Type': income_type,
                'Amount': amount,
                'Description': description
            })
        current_date += timedelta(days=1)

    return pd.DataFrame(data)

# Generate data
daily_expenses_df = generate_daily_expenses()
income_df = generate_income()

# Save to CSV
daily_expenses_df.to_csv('daily_expenses.csv', index=False)
income_df.to_csv('income.csv', index=False)

print("Dummy data for the specified period has been created and saved to CSV files.")
