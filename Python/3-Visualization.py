
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
    
#Create density plot: shows density plots for all numeric variables in dataset
    df.plot(kind = 'density', subplots=True, layout = (3,3), sharex=False)
         
# Create ScatterPlot: set the linewidth (lw), color and transparency (alpha) of the line  
   df.scatter(df.x, df.y, s = 10, color = 'choose color', alpha = 1)
    # Label the axes and provide a title
    df.set_title(title)
    df.set_xlabel(x_label)
    df.set_ylabel(y_label)
 
# Create BarPlot
    df.bar(df.x, df.y, color = 'choose color', align = 'center')
         
#Create Boxplot
     data.plot(kind = 'box', subplots = True, layout = (3,3), sharex = False, sharey = False)
  
#Create correlation plot: choose coolwarm as color scheme
    df.corr()
    corr.style.background_gradient(cmap='coolwarm')
         
#Create scatterplot matrix: creates scatterplots and a central histogram of all numeric variables in dataset
    import matplotlib.pyplot as plt
    import pandas
    from pandas.plotting import scatter_matrix
    
    scatter_matrix(df)
    plt.show()
         
   #Source: https://machinelearningmastery.com/visualize-machine-learning-data-python-pandas/
