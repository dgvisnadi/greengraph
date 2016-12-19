#!/usr/bin/env python
from argparse import ArgumentParser
from mkgraph import make_graph

def load_image():
    parser = ArgumentParser(description = 'Visualize amount of green pixels between two locations')
    parser.add_argument('--from', help='Start Location')
    parser.add_argument('--to', help='End Location')
    parser.add_argument('--steps', help='Steps between the two locations')
    parser.add_argument('--out', help='Save as: (i.e. image.png)')
    arguments = parser.parse_args()

    make_graph(arguments.start, arguments.end, arguments.steps, arguments.out)

