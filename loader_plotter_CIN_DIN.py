import pandas as pd

import numpy as np

import re

import networkx as nx
import matplotlib.pyplot as plt


# Check for PAN or DIN
# Function to check number and return "PAN", "DIN" or "NONE" based on check
def checkID(id):
    DIN = re.compile("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")
    PAN = re.compile("[A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][A-Z]")

    if DIN.match(id):
        return "DIN"
    elif PAN.match(id):
        return "PAN"
    else:
        return "NONE"



# Create a new dataframe from csv
df = pd.read_excel("data/TataGroup.xlsx", sheetname="DIN&CompAt3level",skiprows=0)

# Show the raw data
# print(df.head())


# Add another column IDType to the table
print("Trying a transformation")
df["IDType"] =  df["DINDPINPAN"]
df["IDType"] = df["IDType"].transform(checkID)
# print(df["IDType"])

# Break down  DIN ID and link with CIN ID
# Pick out only Directors with DIN number given
df.loc[(df["IDType"] == "DIN"), ["DINDPINPAN", "CIN", "CompanyName"]]

# Get list of CIN and Company Names
# Pick out a list of CIN and Company Names
df.loc[(df["IDType"] == "DIN"), ["CIN", "CompanyName"]]

# Get list of DINDPINPAN and Names
# Pick out a list of DINDPINPAN and Director Names
df.loc[(df["IDType"] == "DIN"), ["DINDPINPAN", "DirectorName"]]

# Create (DIN, CIN) as edges
# Create a tuple of DIN and CIN
DIN_CIN_edges = list( zip(df.DINDPINPAN, df.CIN))
print ("DIN_CIN Edges: ")
# print (DIN_CIN_edges)

## Create Label from the data column
# Create a tuple of DIN Director Names
Label_DIN_DNames = dict(list(zip(df.DINDPINPAN, df.DirectorName)))
# print(Label_DIN_DNames)
# Create a tuple of CIN Company Names
Label_CIN_CNames = dict(list(zip(df.CIN, df.CompanyName)))
# print(Label_CIN_CNames)


# Create graph instance
G = nx.Graph()

# Data node is Label_CIN_CNames and Label_DIN_DNames
# cities_data = {"a": "Mumbai", "b": "Kolkata", "c": "Chennai"}

# edge_list = [("a", "b"), ("b","c"), ("d","e"), ("c","f"), ("f", "e")]

G.add_edges_from(DIN_CIN_edges)

# Relabel nodes according to their labels
H = nx.relabel_nodes(G, Label_CIN_CNames)
H = nx.relabel_nodes(H, Label_DIN_DNames)


print("Nodes of the graph", H.nodes())
print("Edges of the graph", H.edges())

print("Node type", type(H.nodes()))
print("Edges type", type(H.edges()))

# Plot it
nx.draw_networkx(H)
# plt.savefig("simple_path.png") # save as png
plt.show() # display



