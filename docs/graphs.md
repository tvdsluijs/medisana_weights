---
layout: page
title: Graphs
subtitle: Data output in graphs
---

So the data from Medisana (like in the [data link]({{ site.baseurl }}/data)) can be easily put to nice graphs with the matplotlib library.

{: .box-error}
**Error:** Looking at my data can cause instant weightloss.

> Just kidding

First load the library in your python script.

```python
import matplotlib.pyplot as plt
```

and load some other stuff for processing and layout reasons (like showing dates)

```python
import os
import json
from datetime import date, datetime
```

And then you can start using it!

### loading the json file

You can easily grab the last json file by

{% highlight python linenos %}
    def __init__(self):
        self.datum = '{:%d-%b-%Y}'.format(date.today())

        dir_path = os.path.dirname(os.path.realpath(__file__))
        folder = os.path.join(dir_path, "data")
        data_file_name = "{}_weights.json".format(self.datum)
        self.data_file = os.path.join(folder, data_file_name)

        with open(self.data_file, 'r') as json_file:
            self.weight_data = json.load(json_file)
{% endhighlight %}

So now you have the json data in the var weight_data.


### Pie chart current data

So lets get the current situation (last weighting) into a nice pie graph.
![Pie Chart](graphs/pie-chart.png)

Its actually very easy to create this pie chart.

Just put the labels in, then get the sizes from the self.weight_data variable put it together with a nice title. And voila!

{% highlight python linenos %}
    def mathlib_pie_chart(self):
        labels = 'bodyFat','muscleMass','boneMass','bodyWater'
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
        plt.savefig('images/pie-chart.png')
{% endhighlight %}


![Pie Charts](graphs/pie-charts.png)
![Line Chart](graphs/linechart_04-2019.png)
![Line Chart](graphs/gauge.png)
