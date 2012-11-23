#!/usr/bin/env python
# coding: utf-8

from __future__ import division
from __future__ import print_function

from igraph import *
from random import *

__author__ = "Laszlo Daniel Fogas, Tamas Endrodi"

"""Returns a graph based on the Price model

m -- number of starting vertices
a -- probability of connection
n -- number of vertices to add to the graph

"""
def price(m, a, n):
	# Initialize an empty, directed graph
	g = Graph(directed=True)

	# add starting vertices
	[g.add_vertex(i) for i in xrange(m)]

	j = m

	# 
	while(j < n):
		ind = g.indegree()
		g.add_vertex(j)
		if(j/(j+a) > random()):
			g.add_edge(j,m)
		j += 1 

	return g





# Tesztelés
p = price(3, 1, 10)
print(p.vcount())
print(p.ecount())
print(p.is_directed())
plot(p)
