# import os
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# print(os.getcwd())
from forecastTemp.scripts import main
import pandas as pd
# import forecast-temp/scripts/etl

from matplotlib import pyplot as plt
from datetime import datetime

a = 100  # number of rows
b = 8  # number of columns
c = 1  # initialize plot counter

input_data_path = "../data/weather.csv"
if __name__ == "__main__":
	start_test_date = "2020-02-01"
	end_test_date = "2020-02-29"
	date_format = "%Y-%m-%d"
	start = datetime.strptime(start_test_date, date_format)
	end = datetime.strptime(end_test_date, date_format)
	# fig, axes = plt.subplots(a, b)
	delta = end - start
	print(delta.days)
	a = 6  # number of rows
	b = 6  # number of columns
	c = 1  # initialize plot counter
	fig = plt.figure(figsize=(20,15))
	daterange = pd.date_range(start, end)
	# custom_xlim = (0, 100)
	custom_ylim = (-5, 20)
	for i in daterange:
		date = str(i.date())
		print(date)
		result, y_test, predictions, humidity = main.main(date, input_data_path)
		print(result)
		# plt.savefig('../visualisation/av{}.png'.format(date))
		# plt.subplot(a, b, c)
		ax = fig.add_subplot(a, b, c)
		ax2 = ax.twinx()
		# plt.title('{}'.format(date))
		ax.title.set_text('{}'.format(date))
		# plt.xlabel(date)
		ax2.plot(humidity.values,  color = 'g', label = 'humidity')
		ax.plot(y_test.values,  color = 'b', label = 'temp_actual')
		ax.plot(predictions,  color = 'r', label = 'temp_predicted')
		# print(humidity)
		plt.savefig('../visualisation/av{}.png'.format(date))
		plt.setp(ax,  ylim=custom_ylim)
		c = c + 1
	fig.tight_layout()
	fig.savefig('../visualisation.png')
