#!/usr/bin/env python
from argparse import ArgumentParser
from greengraph_code.mkgraph import make_graph
from greengraph_code.test.graph_test import Greengraph_test

def load_image():
    parser = ArgumentParser(description = 'Visualize amount of green pixels between two locations')
    parser.add_argument('--from', help='Start Location', dest='start', type=str)
    parser.add_argument('--to', help='End Location', dest='end', type=str)
    parser.add_argument('--steps', help='Steps between the two locations', dest='steps', type=int)
    parser.add_argument('--out', help='Save as: (i.e. image.png)', dest='out', type=str)
    arguments = parser.parse_args()

    make_graph(arguments.start, arguments.end, arguments.steps, arguments.out)

if __name__ == "__main__":
    load_image()





def test_package():
    parser = ArgumentParser(description = 'Test Greengraph package')
    parser.add_argument('--teststart', help='Test - Start Location', dest='teststart', type=str)
    parser.add_argument('--testend', help='Test - End Location', dest='testend', type=str)
    arguments = parser.parse_args()

    Greengraph_test(arguments.teststart, arguments.testend)

if __name__ == "__main__":
    test_package()
