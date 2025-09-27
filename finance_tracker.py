import csv,os
import datetime


transactions = []
file_path = "financial_data.csv"


def load_transactions_from_csv(files):
    if os.path.exists(files):
        try:
            with open(files, 'r') as file:
                dict_reader = csv.DictReader(file)
                for row in dict_reader:
                    try:
                        main_dict = {"Date":row["Date"],"Amount":float(row["Amount"]),"Category":row["Category"],"Description":row["Description"],"Type":row["Type"]}
                        transactions.append(main_dict)
                    except KeyError and ValueError:
                        print("Skipping invalid row: missing or invalid data")
        except PermissionError or OSError:
            print("Error reading file: unable to access financial_data.csv")

load_transactions_from_csv(file_path)
def save_transactions_into_csv(file_path):
    header = ["Date","Amount","Category","Description","Type"]
    try:
        with open(file_path,'w',newline = '') as file:
            dict_writer = csv.DictWriter(file,fieldnames= header)
            dict_writer.writeheader()
            for row in transactions:
                dict_writer.writerow(row)
    except PermissionError or OSError:
        print("Error saving transactions to file. Please check file permissions.")

def check_user_date(user_input):
    datetime.datetime.strptime(user_input, "%Y-%m-%d")
def check_category(user_category):
    try:
        str(user_category)
    except ValueError:
        print("Please enter whether its and income or an expense")
        finance_tracker()
    user_category = user_category.lower()
    user_category.strip()
def finance_tracker():
    flag = False
    print("Please enter the following details:\n")
    Date = (input("Please enter the date in YYYY-MM-DD format \n"))
    try :
        check_user_date(Date)
    except ValueError:
        print("Please enter the date in YYYY-MM-DD format and valid date")
        finance_tracker()
    while not flag:
        Amount = float(input("Please enter your account balance \n"))
        if Amount == float(Amount) and Amount >= 0:
            flag = True
        else:
            print("wrong Input")
    flag = False
    Category = str(input("Enter a category for the amount spend (e.g., Salary,Food) \n"))
    check_category(Category)
    while not flag:
        Description = str(input("Enter description like groceries or fuel \n"))
        if Description =="":
            print("Please enter the description")
        elif type(Description) is str:
            Description.lower().strip()
            flag = True
    flag = False
    while not flag:
        Type = str(input("Enter type (income/expense):\n"))
        Type.lower().strip()
        if Type =='income' or Type == 'expense':
            flag = True
        else:
            print("please enter income or expense")
    user_finance_data  = {"Date":Date,"Amount":Amount,"Category":Category,"Description":Description,"Type":Type}
    transactions.append(user_finance_data)
    save_transactions_into_csv(file_path)
finance_tracker()


