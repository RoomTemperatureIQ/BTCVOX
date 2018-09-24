import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import pandas as pd
import os

# current layer index start with the first layer 
idx = 0

folder = "26OCT18"
files = sorted(os.listdir(str(folder)))
name = folder + "/" + files[0]
df = pd.read_csv(name, sep='\t',index_col=0)
data = df.values
axis =  df.index.values

# figure axis setup 
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.15)

ax.set_title("Recorded Values")
ax.set_xlabel("Moves")
ax.set_ylabel("Strike Price")

plt.setp(ax,xticks=[0,1,2,3], xticklabels=["Calls_B","Calls_A", "Puts_B", "Puts_A"], yticklabels=axis)
# display initial image 
im_h = ax.imshow(data, cmap='hot', interpolation='nearest')

# setup a slider axis and the Slider
ax_depth = plt.axes([0.23, 0.02, 0.56, 0.04])
slider_depth = Slider(ax_depth, 'time', 0, len(files), valinit=idx)

# update the figure with a change on the slider 
def update_depth(val):
    idx = int(round(slider_depth.val))
    folder = "26OCT18"
    files = sorted(os.listdir(str(folder)))
    name = folder + "/" + files[int(idx)]
    #im_h.set_data(data[:, :, idx])
    df = pd.read_csv(name, sep='\t',index_col=0)
    im_h.set_data(df.values)

slider_depth.on_changed(update_depth)

plt.xticks(np.array([0,1]),["Calls", "Puts"])
plt.show()
