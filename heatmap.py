import numpy as np
np.random.seed(0)
import seaborn as sns
sns.set()
# uniform_data = np.random.rand(10, 12)
# ax = sns.heatmap(uniform_data)
# data = [[][]

# for file in os.listdir(folder):
#   with open(folder + "/" + file, "r") as file:
#      reader = csv.reader(file, delimiter='\t')

#     for row in reader:
#        line = map(float, row)
#       data.append(line)

import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Heatmap(z=[[1, 20, 30],
                      [20, 1, 60],
                      [30, 60, 1]])
data = [trace]
py.plot(data, filename='basic-heatmap')
