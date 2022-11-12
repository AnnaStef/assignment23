import pandas as pd # This command imports the pandas library as pd
import matplotlib.pyplot as plt # This command imports the matplotlib.pyplot library as plt
gold=pd.read_csv("gold rate.csv") # read_csv() command reads the csv file
goldprice1980=pd.read_csv("gold rate 1980.csv") # read_csv() command reads the csv file

#graph1
#Plotting the line Graph for Gold rate at United States,United Kingdom and Canada for the year 2021.
def linegraph():
     plt.figure() # figure() command Creates a figure
     plt.plot(gold["Date"],gold["United States(USD)"],label="gold rate in US",color='green') # we are plotting the linegraph of United States(USD) defining the labels and colors
     plt.plot(gold["Date"],gold["United Kingdom(GBP)"],label="gold rate in United Kingdom",color='red')  #we are plotting the linegraph of United States(USD) defining the labels and colors
     plt.plot(gold["Date"],gold["Canada(CAD)"],label="gold rate in Canada",color='black')  #we are plotting the linegraph of United States(USD) defining the labels and colors
     plt.plot(gold["Date"],gold["Australia(AUD)"],label="gold rate in Australia",color='violet') #  we are plotting the linegraph of United States(USD) defining the labels and colors
     plt.xticks(rotation=45) # xticks command rotates the X-Axis labels to 90 degrees
     plt.savefig('linegraph1.png') # savefig() command saves the graph
     plt.title('GOLD RATE IN 2020') # title() command gives the title of the graph
     plt.xlabel('Date') # xlabel() command defines the X-Axis name of the graph
     plt.ylabel('Gold Rate') # ylabel() command defines the Y-Axis name of the graph
     plt.legend(loc="upper left",framealpha=0) # legend() command shows the index values on the graph
     plt.show() # show() command shows the plotted graph


#2nd graph
#Plotting the pie Graph for Gold rate at United States,United Kingdom and Canada for the year 2021.
def pie():
     plt.figure(figsize=(10,15)) # figure() command Creates a figure
     plt.subplot(2,2,1) # subplot() command creates the subplot
     plt.pie(gold["United States(USD)"],labels=gold["Date"],autopct="%2.1f%%") # we are plotting the pie chart defining th labels and the piechart size
     plt.title("American gold price") # title() command gives the title of the graph
     plt.subplot(2,2,2) # subplot() command creates the subplot
     plt.pie(gold["United Kingdom(GBP)"],labels=gold["Date"],autopct="%2.1f%%")  # we are plotting the pie chart defining th labels and the piechart size
     plt.title("UK gold price") # title() command gives the title of the graph
     plt.subplot(2,2,3) # subplot() command creates the subplot
     plt.pie(gold["Canada(CAD)"],labels=gold["Date"],autopct="%2.1f%%")  # we are plotting the pie chart defining th labels and the piechart size
     plt.title("Canada gold price") # xticks command rotates the X-Axis labels to 90 degrees
     plt.subplot(2,2,4) # subplot() command creates the subplot
     plt.pie(gold["Australia(AUD)"],labels=gold["Date"],autopct="%2.1f%%")  # we are plotting the pie chart defining th labels and the piechart size
     plt.title("Australian gold price") # title() command gives the title of the graph
     plt.savefig('piechart.png') # savefig() command saves the graph
     plt.show() # show() command shows the plotted graph


#3rd graph
#Plotting the bar Graph for Gold rate at United Kingdom for the year 1980 and 2020.
def bar():
     plt.bar(goldprice1980['Date'],goldprice1980['United Kingdom(GBP)'],label="gold rate in UK in 1980",color="green") # we are plotting the barplot defining the label and color
     plt.xticks(rotation=90) # xticks command rotates the X-Axis labels to 90 degrees
     plt.xlabel('Date') # xlabel() command defines the X-Axis name of the graph
     plt.ylabel('Gold Rate in UK in 1980') # ylabel() command defines the Y-Axis name of the graph
     plt.bar(gold['Date'],gold['United Kingdom(GBP)'],label="gold rate in UK in 2020",color="red") # we are plotting the barplot defining the label and color
     plt.legend()  # legend() command shows the index values on the graph
     plt.xticks(rotation=90) # xticks command rotates the X-Axis labels to 90 degrees
     plt.xlabel('Date') # xlabel() command defines the X-Axis name of the graph
     plt.ylabel('Gold Rate in uk in 2020')  # ylabel() command defines the Y-Axis name of the graph
     plt.savefig('bargraph.png') # savefig() command saves the graph
     plt.legend() # legend() command shows the index values on the graph
     plt.show() # show() command shows the plotted graph

linegraph() # calling the linegraph function
pie() # calling the pie function
bar() # calling the bar function
