#!/usr/bin/env python
# coding: utf-8

from __future__ import division
from __future__ import print_function

import igraph
import random


__author__ = "Laszlo Daniel Fogas, Tamas Endrodi"

def price(m, a, n):
	"""Returns a graph based on the Price model

	Parameters:
	m -- starting vertices
	a -- initial attractivity
	n -- size of the network
	"""

	# Initialize an empty, directed graph
	g = igraph.Graph(directed=True)

	# add starting vertex
	g.add_vertices(m)
	
	
	while g.vcount() < n:
		# add vertex
		g.add_vertices(1)

		# generate edgelist
		el = range(g.vcount()-1)
		
		# calculate connection probability for each vertex
		cp = []
		li = [i + a for i in g.indegree()]
		sm = sum(li)
		for i in range(g.vcount()):
			cp.append( (g.indegree(i) + a) / sm )

		# walk through the vertices, and add m edges
		for i in el:
			if random.random() > cp[i]:
				g.add_edge(g.vcount() - 1, i)


	# Return the graph
	return g
