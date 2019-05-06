import os
import json
from datetime import date, datetime
from shutil import copyfile

import matplotlib.pyplot as plt
from .gauge import Gauge

class CreateGraphs:
    def __init__(self):
        self.datum = '{:%d-%b-%Y}'.format(date.today())

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.image_folder = os.path.join(dir_path, "../images")

        folder = os.path.join(dir_path, "../data")
        data_file_name = "{}_weights.json".format(self.datum)
        self.data_file = os.path.join(folder, data_file_name)
        
        self.first_date = 1554576328000
        
        self.weight_data = self.open_file_with_contents()
        self.mathlib_pie_chart()
        self.mathlib_pie_charts()
        self.basic_bar_chart()
        self.create_gauge()
        self.create_bmi()
        self.basic_Line_chart()
        self.basic_Line_chart('No')

    def create_gauge(self):

        g = Gauge()
        # myLabels = ['75', '76', '77', '78', '79', '80', '81']
        my_labels = list(range(75, 82, 1))

        weight = round(self.weight_data['lastval'])
        my_arrow = my_labels.index(weight)+1

        filename = os.path.join(self.image_folder, "gauge.png")
        g.gauge(labels=my_labels,
                colors=['#45ed08', '#8ded08', '#c3ed08', '#e9ed09', '#eda808', '#ed6308', '#ba1010'],
                arrow=my_arrow, title="{} Kg".format(self.weight_data['lastval']), fname=filename)

    def create_bmi(self):

        g = Gauge()
        my_labels = ['Ondergewicht', 'Gezond gewicht', 'Overgewicht', 'Obesitas']

        bmi = self.weight_data['lastval_bmi']

        print(bmi)

        if bmi < 18.5:
            my_arrow = 1
        elif 18.5 < bmi < 24.9:
            my_arrow = 2
        elif 24.9 < bmi < 29.9:
            my_arrow = 3
        elif bmi >= 30:
            my_arrow = 4
        else:
            return

        # Minder dan 18,5 = ondergewicht
        # Tussen 18,5 en 24,9 = gezond normaal gewicht
        # Tussen 25 en 29,9 = overgewicht
        # Meer dan 30 = Obesitas

        filename = os.path.join(self.image_folder, "bmi.png")
        g.gauge(labels=my_labels,
                colors=['#f2491a', '#36ce33', '#f1b119', '#f2491a'],
                arrow=my_arrow, title='BMI {}'.format(bmi), fname=filename)

    def mathlib_pie_chart(self):
        labels = 'bodyFat', 'muscleMass', 'boneMass', 'bodyWater'
        colors = ['#f9ca2f', '#e2310d', '#f4f6f7', '#2285f7']
        sizes = [self.weight_data['lastval_bodyFat'], 
                 self.weight_data['lastval_muscleMass'],
                 self.weight_data['lastval_boneMass'],
                 self.weight_data['lastval_bodyWater']]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                colors=colors, shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(self.weight_data['lastMeasurementDate'])
        filename = os.path.join(self.image_folder, "pie-chart.png")
        plt.savefig(filename)
        
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
        filename = os.path.join(self.image_folder, "pie-charts.png")
        plt.savefig(filename)

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

        filename = os.path.join(self.image_folder, "linechart_{}.png".format(month_year))
        plt.savefig(filename)

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
        filename = os.path.join(self.image_folder, "charts.png")
        plt.savefig(filename)
    
    def open_file_with_contents(self, file=None):
        if file is not None:
            self.data_file = file

        with open(self.data_file, 'r') as json_file:
            return json.load(json_file)

    def copy_graphs(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        website_graph_folder = os.path.join(dir_path, "../docs", "graphs")

        for file in os.listdir(self.image_folder):
            filename = os.fsdecode(file)
            if filename.endswith('.png'):
                src = os.path.join(self.image_folder, filename)
                dst = os.path.join(website_graph_folder, filename)

                copyfile(src, dst)
            else:
                continue


if __name__ == '__main__':
    c = CreateGraphs()
