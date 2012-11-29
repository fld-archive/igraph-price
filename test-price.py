#!/usr/bin/env python
# coding: utf-8

from __future__ import division
from __future__ import print_function

import price

""" Create a graph, and print out its properties
"""
p = price.price(3,0.5,10)

# Summary
print()
print("Starting vertices: ", 3)
print("Probability: ", 0.5)
print("All vertices: ", 10)
print()

print("vcount: ", p.vcount())
print("ecount: ", p.ecount())

print("directed: ", p.is_directed())

print("indegree: ", sorted(p.indegree()))

# Plot the graph
p.vs["label"] = range(p.vcount())
p.vs["color"] = "yellow"
plot(p)
