import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
import time


##### This function is used for the subset function()
def one_filter(data, argument, return_dict):
    return_data = {argument[0] : []}
    row = data.shape[0]
    for i in range(0, row):
        if argument[1] == True:
            return_data[argument[0]].append((data[argument[0]][i], i))
        if argument[1] != True:
            if data[argument[0]][i] == argument[1]:
                return_data[argument[0]].append((data[argument[0]][i], i))
    if return_dict == False:
        return return_data
    if return_dict == True:
        return pd.DataFrame.from_dict(return_data)

# Used to filter with tuples For example (the_data, ('Name_of_column', 'Name_of_what_you_want_to_filter_by'), ('Another Column', True))
# use true value to return all data in column.
# this applies a multifilter into one line of code

def subset(data, *args): 
    final_num = []
    first_instance = True
    final_dataset = {}
    subset = data
    for a in args:
        final_dataset.update({a[0] : []})
    for a in args:
        diff = []
        check = []
        for i in range(1, len(a)):
            subset = one_filter(data, (a[0], a[i]), False)
            for s in subset[a[0]]:
                diff.append(s[1])
        if first_instance == False:
            for d in diff:
                if d not in final_num:
                    pass
                if d in final_num:
                    check.append(d)               
        if first_instance == True:
            for d in diff:
                check.append(d)
            first_instance = False
        final_num = check
    for num in final_num:
        for a in args:
            final_dataset[a[0]].append(data[a[0]][num])
    return pd.DataFrame.from_dict(final_dataset)
    
    
 

def remove_nan(nlist):
    check = 0
    if nlist == dict(nlist):
        nlist = {k: [x for x in v if not isinstance(x, float) or not math.isnan(x)] \
                 for k, v in nlist.items() }
        
    if nlist == list(nlist):
        for i in range(len(nlist)):
            if nlist[i] != str(nlist[i]):
                if math.isnan(nlist[i]) == True:
                    nlist.remove(nlist[i])
    return nlist
    


def dataset_size(data, cat):
    row = data.shape[0]
    new_data = {'nan' : 0}
    for i in range(0, row):
        check = False
        
        if data[cat][i] != str(data[cat][i]):
            if math.isnan(data[cat][i]) == True:
                new_data['nan'] = new_data['nan'] + 1
                check = True
                
        if data[cat][i] not in new_data.keys() and check == False:
            new_data.update({data[cat][i] : 1})
            
        if data[cat][i] in new_data.keys() and check == False:
            new_data[data[cat][i]] = new_data[data[cat][i]] + 1
            
    return new_data


def dtype_sets(data, catone, cattwo):
    row = data.shape[0]
    new_data = {}
    for i in range(0, row):

        if data[catone][i] not in new_data.keys():
            new_data.update({data[catone][i] : []})

        new_data[data[catone][i]].append(data[cattwo][i])

    return new_data
        
                          

def data_list(data, cat):
    row = data.shape[0]
    new_data = []
    nan_values = 0
    for i in range(0, row):
        if math.isnan(data[cat][i]) != True:
            new_data.append(data[cat][i])
        if math.isnan(data[cat][i]) == True:
            nan_values += 1
    return new_data, nan_values


        
def data_hist(values, grange, width):
    plt.hist(values, rwidth=width, bins = list(grange))
    plt.show()


def data_bar(values, typeof):   
    new_values = list(values.keys())
    y = np.arange(len(new_values))
    top = []
    
    for v in values:
        graphing = []
        for i in values[v]:
            graphing.append(i)

        if typeof == 'Total':
            top.append(sum(graphing))
            
        if typeof == 'Average':
            top.append((sum(graphing) / float(len(graphing))))
            
            
    plt.bar(y, top, align = 'center', alpha = 0.5)
    plt.xticks(y, new_values)
    plt.ylabel(typeof)

    plt.show()
