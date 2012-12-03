#!/usr/bin/env python
# coding: utf-8

from __future__ import division

import igraph
import random


__author__ = "Laszlo Daniel Fogas, Tamas Endrodi and Arpad Horvath"

def price_newman(m, a, n):
    """Returns a graph based on the Price model

    Parameters:
    m -- number of starting vertices
    a -- initial attractivity
    n -- number of vertices in the end of the generation

    It uses the algorithm descibed in the book
    Mark Newman:
    Networks, An Introduction,
    Oxford University Press, 2010
    pp. 495-498

    """

    # Initialize an empty, directed graph
    g = igraph.Graph(directed=True)

    # add starting vertices
    g.add_vertices(m)

    prob_propotional = m/(m+a)

    g.add_vertex()
    edges = [(m, i) for i in range(m)]
    g.add_edges(edges)
    vertices_with_inedge = range(m)

    while g.vcount() < n:
        # add vertex
        g.add_vertex()
        N = g.vcount()

        target_set = set()
        while len(target_set) < m:
            if random.random() < prob_propotional:
                while True:
                    target = random.choice(vertices_with_inedge)
                    if target not in target_set:
                        break
            else:
                while True:
                    target = random.randint(0, N-2)
                    if target not in target_set:
                        break
            target_set.add(target)
        vertices_with_inedge.extend(list(target_set))
        g.add_edges([(N-1, target) for target in target_set])

    # Return the graph
    return g

# TODO not ready
def price_orig(m, a, n):
    """Returns a graph based on the Price model

    Parameters:
    m -- starting vertices
    a -- initial attractivity
    n -- size of the network

    It uses the definition of the Price model.

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

price = price_newman
