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
    m -- number of starting vertices
    a -- initial attractivity
    n -- number of vertices in the end of the generation

    """
	# Initialize an empty, directed graph
	g = igraph.Graph(directed=True)

	# add starting vertices
    g.add_vertices(m)

	j = m

	while len(g.indegree()) < n:
		ind = g.indegree()
		g.add_vertex(j)
		for i in xrange(j):
			if ind[i] + a/j > random.random():
				g.add_edge(j,i)
		j += 1

	return g

