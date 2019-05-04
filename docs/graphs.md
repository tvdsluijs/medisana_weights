---
layout: page
title: Graphs
subtitle: Data output in graphs
---

So the Data from Medisana (like in the [data link](/data)) can be easily put to nice graphs with the matplotlib library.

First load the library in your python script

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

```python
    def __init__(self):
        self.datum = '{:%d-%b-%Y}'.format(date.today())

        dir_path = os.path.dirname(os.path.realpath(__file__))
        folder = os.path.join(dir_path, "data")
        data_file_name = "{}_weights.json".format(self.datum)
        self.data_file = os.path.join(folder, data_file_name)

        with open(self.data_file, 'r') as json_file:
            self.weight_data = json.load(json_file)
```

So now you have the json data in the var weight_data.


### Pie chart current data

So lets get the current situation (last weighting) into a nice pie graph.


