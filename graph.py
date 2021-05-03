import networkx as nx
import matplotlib.pyplot as plt
from math import exp, floor
from time import sleep

#https://www.desmos.com/calculator/dvqzqfrso2
def sigmoid(a,b,c,x):
    return a/(1+exp(-b*x-c))

G = nx.DiGraph()
  
cities = [(1,300),(2,100),(3,220)]
cities_history = [cities]
migrations = [(1,2,0.1),(1,3,0.2),(3,1,0.05)]

for migration in migrations:
    G.add_edge(migration[0], migration[1])

colors = []
for i in range(len(cities)):
    colors.append((sigmoid(1,0.015,-4,cities[i][1]),sigmoid(1,0.005,-4,cities[i][1]),0.1,1.0))

nx.draw_networkx_nodes(G, nx.planar_layout(G), node_color=colors)
nx.draw_networkx_edges(G, nx.planar_layout(G))

plt.savefig("filename.png")

def main():
    for t in range(1,10):
        newCities = updateFunction(cities_history[t-1])
        cities_history.append(newCities)

        colors = []
        for i in range(len(newCities)):
            colors.append((sigmoid(1,0.015,-4,newCities[i][1]),sigmoid(1,0.005,-4,newCities[i][1]),0.1,1.0))

        nx.draw_networkx_nodes(G, nx.planar_layout(G), node_color=colors)

        sleep(1)
        plt.savefig("filename.png")


def updateFunction(cities):
    newCities = []
    
    for i in range(len(migrations)):
        pass
    
    for i in range(len(cities)):
        newCities.append((i, cities[i][1]+100))

    return newCities

#main()

print(G.adjacency())