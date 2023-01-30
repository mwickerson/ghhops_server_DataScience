"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm

import math
import re
import urllib.request
import collections
from collections import Counter
from collections import OrderedDict
import os
from os import path
import random

import numpy as np
import numpy.linalg

# import matplotlib
# import matplotlib.pyplot as plt

import pandas as pd
import io

# import scipy
# import seaborn
import sklearn

#from lxml import objectify

# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

"""
import json
import sklearn as skl
import sklearn.linear_model as linm
import sklearn.cluster as cluster
import sklearn.neighbors as nb
import sklearn.neural_network as MLP
import sklearn.tree
import sklearn.svm
import sklearn.ensemble
"""

"""
███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗        
████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝        
██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗          
██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝          
██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗        
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝        
                                                                
██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
██║     █████╗  ███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
███████╗███████╗██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""

#Working with Real Data
#Manipulating data streams
#working with flat and unstructured files
#Interacting with relational databases
#using NoSQL as a data source
#interacting with web-based data sources

#uploading, streaming, and Sampling data
#columns are called features and rows are called observations

#uploading small amounts of data into memory
#use colors.txt file
#use @hops.component to open the txt file

@hops.component(
    "/ReadText",
    name="Read Text File",
    description="Reads a text file and returns a list of strings",
    icon="read_text_file.png",
    inputs=[
        hs.HopsString('file', 'File', 'File path')
    ],
    outputs=[
        hs.HopsString('strings', 'Strings', 'List of strings')
    ]
)
def read_text_file(file):
    with open(file, 'r') as open_file:
        readOut = open_file.read()
        #create a data frame with the readOut data by using the pandas library
        df = pd.read_csv(io.StringIO(readOut), sep=" ", header=None)
        #create a list of the data frame
        listOut = df.values.tolist()
        #return the first element in each list index
        listOut = [x[0] for x in listOut]
        #return the list
        return (listOut[0:10])

@hops.component(
    "/colorsNumber",
    name="Read Text File",
    description="Reads a text file and returns a list of strings",
    inputs=[
        hs.HopsString('file', 'File', 'File path')
    ],
    outputs=[
        hs.HopsString('colors', 'Colors', 'List of colors'),
        hs.HopsString('numbers', 'Numbers', 'List of numbers')
    ]
)
def read_text_file(file):
    with open(file, 'r') as open_file:
        readOut = open_file.read()
        #create a data frame with the readOut data by using the pandas library
        df = pd.read_csv(io.StringIO(readOut), sep=" ", header=None)
        #create a list of the data frame
        listOut = df.values.tolist()
        #return the first element in each list index
        listOut = [x[0] for x in listOut]
        #eliminate the brackets from the list
        listOut = [x.replace('[', '') for x in listOut]
        #remove the first element in the list
        listOut.pop(0)

        #return the first thru last element in each list index up until the / character minus two characters
        colorsOut = [x[0:-2] for x in listOut]
        

        #return the last 
        numOut = [y[-1] for y in listOut]


        #return colorsOut and numOut
        return (colorsOut, numOut)




if __name__ == "__main__":
    app.run(debug=True)
