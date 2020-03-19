#import
import operator
import emails
import reports
import os

#process data
#outside loop
max_sales = {"total_sales": 0}
total_sales = {}

#inside loop
  if item["total_sales"] > max_sales["total_sales"]:
    max_sales = item
  key = item["car"]["car_year"]
  if not key in total_sales:
    total_sales[key] = 0
  total_sales[key] += item["total_sales"]
  
#outside loop
sorted_total_sales = sorted(total_sales.items(), key=operator.itemgetter(1), reverse=True)
max_year_sales = next(iter(sorted_total_sales))

summary = [
    "The {} had the most sales: {}".format(format_car(max_sales["car"]), max_sales["total_sales"]),
    "The most popular year was {} with {} sales.".format(max_year_sales[0], max_year_sales[1])
    ]

#main
#fix path
data = load_data("../car_sales.json")
#generate pdf
body = ""
title = "Sales summary for last month"
for line in summary:
    body = body + line + "<br/>"
table_data = cars_dict_to_table(data)
reports.generate("/tmp/cars.pdf", title, body, table_data)
#generate EmailMessage
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
message = emails.generate(sender, receiver, title, body, "/tmp/cars.pdf")
emails.send(message)


