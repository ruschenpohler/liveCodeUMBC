#!/usr/bin/env python
# coding: utf-8

# # Miscellaneous Tools
# 
# A set of tools used in our exercise.

# ## Import Things

# In[1]:


import numpy as np

import matplotlib.pyplot as plt


# ## plotSeries

# In[2]:


def plotSeries(y,x=None,xMin=None,xMax=None,xVert=None,yTitle='',xTitle='',
               title='',labels=None,reverseLabels=False,savePath='',dpi=300,
               useOffset=False, style='sci'):
    '''
    Plot a series of y-values (or multiple series) against a common x variable.
    
    Parameters
    ----------
    y: np.array
        Array of y-axis values. Maximum number of series to plot is 39.
    x: np.array
        Common array of x-values
    xMin: float
        Minimum x-value to plot
    xMax: float
        Maximum x-value to plot
    xVert: float
        Float or array of vertical lines to plot
    yTitle: string
        Title for y-axis
    xTitle: string
        Title for x-axis
    title: string
        Title for entire figure
    labels: list of strings
        Labels for legend for each series of data in the plot
    savePath : string
        Where the file is saved
    dpi : integer
        Quality of png image
    useOffset : boolean
        Turns on or off axis offset
    style : string
        When 'plain', turns off scientific notation, 'sci' keeps it on.
    
    Returns
    -------
    None
    '''
    # make series at least 2D
    y = np.atleast_2d(y)
    
    if x is None:
        x = np.arange(y[0].size,step=1) + 1
    else:
        x = np.atleast_1d(x)
    
    if xMin is None:
        xMin = x.min()
    
    if xMax is None:
        xMax = x.max()
    
    assert y.shape[0] <= 39, 'Will only plot a maximum of 39 series'
    assert x.size == y[0].size, 'x and y[i] must have same number of points'
    
    for i,yi in enumerate(y):
        lineColor = 'C' + str(np.mod(i,10))
        if i/10 == 0:
            lineStyle = '-'
        elif i/10 == 1:
            lineStyle = '--'
        elif i/10 == 2:
            lineStyle = ':'
        elif i/10 == 3:
            lineStyle = '-.'
        
        try:
            labeli = labels[i]
        except:
            labeli = None
        
        plt.plot(x[(x >= xMin) & (x <= xMax)],yi[(x >= xMin) & (x <= xMax)],
                   lineColor,linestyle=lineStyle,label=labeli)
        
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.title(title)
    
    if labels is not None:
        handles, labels = plt.gca().get_legend_handles_labels()
        if reverseLabels:
            handles.reverse()
            labels.reverse()
        plt.legend(handles,labels,loc='center left', bbox_to_anchor=(1,0.5))
        
    plt.grid()
    
    if xVert is not None:
        xVert = np.atleast_1d(xVert) # make float iterable
        for xc in xVert:
            plt.axvline(x=xc,color='red',linestyle=':')
    
    if x[(x >= xMin) & (x <= xMax)].size < 6:
        # Make small number of ticks into integers
        plt.xticks(x[(x >= xMin) & (x <= xMax)])
        
    if savePath != '':
        plt.savefig(savePath + '.png', bbox_inches='tight', dpi=dpi)
        
    plt.ticklabel_format(useOffset=useOffset, style=style)
    plt.show()
    return None


# In[3]:




# In[ ]:




