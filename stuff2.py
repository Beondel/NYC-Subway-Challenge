import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from mpl_toolkits import mplot3d

class Node:
    def __init__(self,lon,lat,id,neighbors,name):
        self.lon = lon
        self.lat = lat
        self.id = id
        self.neighbors = neighbors
        self.name = name

def seconds(time):
    h, m, s = map(int, time.split(':'))
    return h * 60**2 + m * 60 + s

filename = "google_transit/stop_times.txt"
f = open(filename, 'r')

full_list = []

for line in f:
    trip_id = line.split(',')[0].split('-')

    full_list.append(line)

full_list = full_list[1:]

full_list[1]


full_list[0].split(",")
name_list = []
time_list = []
current_trip_id = ""

timed_graph = {}
graph = {}

last_trip = ""
last_name = ""
last_time = ""
for item in full_list:
    split_list = item.split(",")

    trip = split_list[0]
    name = split_list[3]
    time = seconds(split_list[1])
    
    if name not in graph:
        graph[name] = []
    if (name, time) not in timed_graph:
        timed_graph[(name, time)] = []

    if trip == last_trip:
        timed_graph[(last_name, last_time)].append((name, time))
        graph[last_name].append(name)

    last_name = name
    last_time = time

print(f"{len(timed_graph) = }")
print(f"{len(graph) = }")
print(' '.join(sorted(list(graph))))


filename = "google_transit/transfers.txt"
f = open(filename, 'r')

trans_graph = {}

graph_size = 0
count = 0
for line in f:
    count += 1
    if count == 1:
        continue
    info = line.split(',')
    stats = []
    stats.append(info[0] + 'N')
    stats.append(info[0] + 'S')
    stats.append(info[1] + 'N')
    stats.append(info[1] + 'S')
    stats = list(set(stats))
    time = int(info[3])

    for item1 in stats:
        for item2 in stats:
            if item1 == item2:
                continue
            if item1 not in trans_graph:
                trans_graph[item1] = {}
            if item2 not in trans_graph[item1]:
                trans_graph[item1][item2] = 60**3
                trans_graph[item1][item2] = min(trans_graph[item1][item2], time)
            graph_size += 1

for stat in trans_graph:
    neighs = trans_graph[stat]
    if len(neighs) > 1:
        print(f"{stat} : {len(neighs)}")
print(len(trans_graph))
