
import matplotlib.pyplot as plt
import numpy as np


#Create histogram
plt.hist(df.variable, bins=10)
#Can drop NA values from histogram (or any other graph
plt.hist(df.variable.drop().values, bins = 20
#Take log value of variable
plt.hist(np.log10(df.variable), bins = 20)

# Create Line Graph: set the linewidth (lw), color and transparency (alpha) of the line
    df.plot(df.x, df.y, lw = 2, color = 'choose color', alpha = 1)
    # Label the axes and provide a title
    df.set_title(title)
    df.set_xlabel(x_label)
    df.set_ylabel(y_label)
    
# Create ScatterPlot: set the linewidth (lw), color and transparency (alpha) of the line  
   df.scatter(df.x, df.y, s = 10, color = 'choose color', alpha = 1)
    # Label the axes and provide a title
    df.set_title(title)
    df.set_xlabel(x_label)
    df.set_ylabel(y_label)
 
# Create BarPlot
    df.bar(df.x, df.y, color = 'choose color', align = 'center')
