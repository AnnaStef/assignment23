import pandas as pd
import matplotlib.pyplot as plt
gold=pd.read_csv("gold rate.csv")
goldprice1980=pd.read_csv("gold rate 1980.csv")

#graph1
#Plotting the line Graph for Gold rate at United States,United Kingdom and Canada for the year 2021.
def linegraph():
     plt.plot()
     plt.plot(gold["Date"],gold["United States(USD)"],label="gold rate in US",color='green')
     plt.plot(gold["Date"],gold["United Kingdom(GBP)"],label="gold rate in United Kingdom",color='red')
     plt.plot(gold["Date"],gold["Canada(CAD)"],label="gold rate in Canada",color='black')
     plt.plot(gold["Date"],gold["Australia(AUD)"],label="gold rate in Australia",color='violet')
     plt.xticks(rotation=45)
     plt.savefig('linegraph1.png')
     plt.title('GOLD RATE IN 2020')
     plt.xlabel('Date')
     plt.ylabel('Gold Rate')
     plt.legend(loc="upper left",framealpha=0)
     plt.show()


#2nd graph
#Plotting the pie Graph for Gold rate at United States,United Kingdom and Canada for the year 2021.
def pie():
     plt.figure(figsize=(10,15))
     plt.subplot(2,2,1)
     plt.pie(gold["United States(USD)"],labels=gold["Date"],autopct="%2.1f%%")
     plt.title("American gold price")
     plt.subplot(2,2,2)
     plt.pie(gold["United Kingdom(GBP)"],labels=gold["Date"],autopct="%2.1f%%")
     plt.title("UK gold price")
     plt.subplot(2,2,3)
     plt.pie(gold["Canada(CAD)"],labels=gold["Date"],autopct="%2.1f%%")
     plt.title("Canada gold price")
     plt.subplot(2,2,4)
     plt.pie(gold["Australia(AUD)"],labels=gold["Date"],autopct="%2.1f%%")
     plt.title("Australian gold price")
     plt.savefig('piechart.png')
     plt.show()


#3rd graph
#Plotting the bar Graph for Gold rate at United Kingdom for the year 1980 and 2020.
#def bar():
     plt.bar(goldprice1980['Date'],goldprice1980['United Kingdom(GBP)'],label="gold rate in UK in 1980",color="green")
     plt.xticks(rotation=90)
     plt.xlabel('Date')
     plt.ylabel('Gold Rate in UK in 1980')
     plt.bar(gold['Date'],gold['United Kingdom(GBP)'],label="gold rate in UK in 2020",color="red")
     plt.legend()
     plt.xticks(rotation=90)
     plt.xlabel('Date')
     plt.ylabel('Gold Rate in uk in 2020')
     plt.savefig('bargraph.png')
     plt.legend()
     plt.show()

linegraph()
pie()
bar()
