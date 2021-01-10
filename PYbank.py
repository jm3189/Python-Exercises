#!/usr/bin/env python
# coding: utf-8

# In[21]:


import csv
import os

load = os.path.join ("budget_data.csv")
output = os.path.join("budget_analysis.txt")

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 10000000000000]
total_net = 0

with open(load) as financial_data:
    reader = csv.reader(financial_data)
    
    header = next(reader)
    #print(header)
    
    first_row = next(reader)
    #print(first_row)
    total_months = total_months + 1
    total_net = total_net + int(first_row [1])
    prev_net = int(first_row[1])
    
    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        #print(total_net)
        net_change  = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        net_monthly_avg = sum(net_change_list) / len(net_change_list)
        
        output_summary = (
            f"\nFinancial Analysis\n"
            f"======================\n"
            f"Total Months: {total_months}\n"
            f"Average Change: ${net_monthly_avg:.2f}\n"
            f"Greatest Increase In Profits {greatest_increase[0]}, (${greatest_increase[1]})\n"
            f"Greatest Decrease In Profits {greatest_decrease[0]}, (${greatest_decrease[1]})\n")
    #print(output_summary)
    with open(output, "w") as txt_file:
        txt_file.write(output_summary)
        

