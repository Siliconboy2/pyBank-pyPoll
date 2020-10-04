import csv
months = []
profit = []
profit_change = []

with open('/Users/northwestern/PycharmProjects/homework/PyBank/budget_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        months.append(row['Date'])
        profit.append(int(row['Profit/Losses']))
    for i in range(0, len(profit)-1):
        profit_change.append(profit[i + 1] - profit[i])
    greatest_profit_gain = max(profit_change)
    greatest_profit_loss = min(profit_change)
    greatest_profit_gain_month = profit_change.index(max(profit_change))
    greatest_profit_loss_month = profit_change.index(min(profit_change))
    average_profit_change = round(sum(profit_change) / len(profit_change), 2)




print('Financial Analysis\n----------------------------')
print(f'Total Months: {len(months)}')
print(f'Total: {sum(profit)}')
print(f'Average Change: ${average_profit_change}')
print(f'Greatest Increase in Profits: {months[greatest_profit_gain_month]} ${greatest_profit_gain}')
print(f'Greatest Decrease in Profits: {months[greatest_profit_loss_month]} ${greatest_profit_loss}')