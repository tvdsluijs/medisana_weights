import os
import json
from datetime import date, datetime

import matplotlib.pyplot as plt

class CreateGraphs:
    def __init__(self):
        self.datum = '{:%d-%b-%Y}'.format(date.today())

        dir_path = os.path.dirname(os.path.realpath(__file__))
        folder = os.path.join(dir_path, "data")
        data_file_name = "{}_weights.json".format(self.datum)
        self.data_file =  os.path.join(folder, data_file_name)
        
        self.first_date = 1554576328000
        
        self.weight_data = self.open_file_with_contents()
        self.mathlib_pie_chart()
        self.mathlib_pie_charts()
        self.basic_bar_chart()

        self.basic_Line_chart()
        self.basic_Line_chart('No')


    def mathlib_pie_chart(self):
        labels = 'bodyFat','muscleMass','boneMass','bodyWater'
        colors = ['#f9ca2f', '#e2310d', '#f4f6f7', '#2285f7']
        sizes = [self.weight_data['lastval_bodyFat'], 
                  self.weight_data['lastval_muscleMass'], 
                  self.weight_data['lastval_boneMass'], 
                  self.weight_data['lastval_bodyWater']]
        explode = (0.1, 0, 0, 0)  # only "explode" the 1nd slice (i.e. 'Fat')
        
        # fig1, ax1 = plt.subplots()
        fig1, ax1 = plt.subplots()        
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                colors=colors, shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
               
        plt.savefig('images/pie-chart.png')
        
        
    def mathlib_pie_charts(self):
        labels = 'bodyFat','muscleMass','boneMass','bodyWater'
        colors = ['#f9ca2f', '#e2310d', '#f4f6f7', '#2285f7']
        explode = (0.1, 0, 0, 0)  # only "explode" the 1nd slice (i.e. 'Fat')
        
        fig, axes = plt.subplots(2, 3, figsize=(10, 6))
        
        i = 0
        data = self.weight_data['bodyWeight']
        for w in data[-5:]:
            if w['x'] < self.first_date:
                continue
            
            sizes = [w['bodyFat'], w['muscleMass'], w['boneMass'], w['bodyWater']]
  
            ax = axes[i // 3, i % 3]
            ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                   shadow=True, startangle=90)

            ts = int(str(w['x'])[:-3])
            date = datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
            ax.set_title(date)
            i += 1
        fig.subplots_adjust(wspace=.2)
        plt.savefig('images/pie-charts.png')
        print('done')

    def basic_Line_chart(self, all=None):
        # Data for plotting
        dates = []
        values = []
        data = self.weight_data['bodyWeight']
        i = 0
        for w in data:
            if all is not None:
                if w['x'] < self.first_date:
                    continue

            ts = int(str(w['x'])[:-3])
            if i == 0:
                month_year = datetime.utcfromtimestamp(ts).strftime('%m-%Y')
                i = 1

            date = datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
            dates.append(date)
            values.append(w['y'])

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        plt.xticks(rotation=70)
        plt.subplots_adjust(hspace=0, bottom=0.3)
        ax.plot(dates, values)

        ax.set(xlabel='Dates', ylabel='Weight (kg)',
               title='About as simple as it gets, folks')

        ax.grid()
        fig.savefig("images/linechart_{}.png".format(month_year))

    def basic_bar_chart(self):
        dates = []
        values = []

        data = self.weight_data['bodyWeight']
        for w in data[-5:]:
            ts = int(str(w['x'])[:-3])
            date = datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
            dates.append(date)
            values.append(w['y'])
        
        fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
        axs[0].bar(dates, values)
        axs[1].scatter(dates, values)
        axs[2].plot(dates, values)
        fig.suptitle('Categorical Plotting')
        plt.savefig('images/charts.png')
    
    def open_file_with_contents(self, file=None):
        if file is not None:
            self.data_file = file
            
        with open(self.data_file, 'r') as json_file:
            return json.load(json_file)

if __name__ == '__main__':
    c = CreateGraphs()