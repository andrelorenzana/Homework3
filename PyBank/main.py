import csv
import os

def main():

    with open('budget_data.csv', 'r', newline = '', encoding='utf-8') as csvfile:
        financial_data = list(csv.reader(csvfile, delimiter= ","))

        months, net_change, max_change, min_change = 0, 0, 0, 0
        changes = []
        max_change_month, min_change_month = '', ''




        for i in range(1,len(financial_data)):
            months = months + 1
            current_profit = int(financial_data[i][1])
            net_change = net_change + current_profit

            if len(changes) > 0:
                changes.append(current_profit-int(financial_data[i-1][1]))
            else:
                changes.append(current_profit)

            max_change = max(changes)
            min_change = min(changes)

            if max_change < max(changes):
                max_change = max(changes)
                max_change_month = financial_data[i][0]

            if min_change > min(changes):
                min_change = min(changes)
                min_change_month = financial_data[i][0]

    average_change = sum(changes)/months

    analysis_string = """----------------------------\nFinancial Analysis\n----------------------------\n
Total Months: {}\n
Total: ${}\n
Average Change: ${}\n
Greatest Increase in Profits: {} (${})\n
Greatest Decrease in Profits: {} (${})\n""".format(months, net_change, average_change,
        max_change_month, max_change, min_change_month, min_change)

    with open('financial_analysis_output.txt', 'w', newline = '', encoding='utf-8') as output_file:
        output_file.write(analysis_string)



if __name__ == '__main__':
    main()
