#!/usr/bin/env python
# coding: utf-8

from __future__ import division
from __future__ import print_function

import igraph
import price

# Define variables
sv = 3		# starting vertices
at = .8 	# attractivity
ns = 10		# network size

""" Create a graph, and print out its properties
"""
p = price.price(sv, at, ns)

# Summary
print()
print("Starting vertices: ", sv)
print("Attractivity: ", at)
print("Network size: ", ns)
print()

print("vcount: ", p.vcount())
print("ecount: ", p.ecount())

print("directed: ", p.is_directed())

print("indegree: ", p.indegree())
print("outdegree:", p.outdegree())


# Plot the graph
p.vs["label"] = range(p.vcount())
p.vs["color"] = "yellow"
igraph.plot(p)
