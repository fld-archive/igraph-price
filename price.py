#!/usr/bin/env python
# coding: utf-8

from __future__ import division

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

	# add starting vertices
	g.add_vertices(m)
	
	
	while g.vcount() < n:
		# add vertex
		g.add_vertices(1)

		# generate edgelist
		el = range(g.vcount()-1)
		
		# calculate connection attractivity for each vertex
		cp = []
		li = [i + a for i in g.indegree()]
		sm = sum(li)
		for i in range(g.vcount()):
			cp.append(li[i] / sm)

		# walk through the vertices
		for i in el:
			# add edge, if a random number is greater than attractivity of the vertex
			if random.random() > cp[i]:
				g.add_edge(g.vcount() - 1, i)


	# Return the graph
	return g
