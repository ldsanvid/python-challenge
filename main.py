import pandas as pd

file = "C:\\Users\\ldsan\\Desktop\\PythonStuff\\pythonhw\\budget.csv"

budget_df = pd.read_csv(file)

budget_df

total_months= budget_df["Date"].count()
print(total_months)

net_total= budget_df["Profit/Losses"].sum()
print(net_total)

average_change= budget_df["Profit/Losses"].mean()
print(average_change,)

max_profit_date= budget_df["Date"].max()
print(max_profit_date)

max_profit_ammount= budget_df["Profit/Losses"].max()
print(max_profit_ammount)

min_profit_date= budget_df["Date"].min()
print(min_profit_date)

min_profit_ammount= budget_df["Profit/Losses"].min()
print(min_profit_ammount)

print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
print("Monthly Average: $" + str(average_change))
print("Greatest Increase in Profit: " + str(max_profit_date) + "/ $" + str(max_profit_ammount))
print("Greatest Decrease in Profit: " + str(min_profit_date) + "/ $" + str(min_profit_ammount))