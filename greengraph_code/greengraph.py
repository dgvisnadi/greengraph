from matplotlib import pyplot as plt
from graph import Greengraph
from map  import Map

def greengraph(start, end, steps, out=False):
    ''' Generate a plot showing intensiity of green pixels between two locations.

    Parameters
    ---------
    start: str
        Start location name, such as London or Paris

    end: str
        End location name, such as Milan or Madrid

    steps: int
        Number of images between start location and end location

    out: str
        Save as, i.e Desktop/graph.png

    Returns
    ---------
    image

    '''


    mygraph=Greengraph(start, end)
    data=mygraph.green_between(steps)
    plt.plot(data)
    if out:
        plt.savefig(out)
    else:
        show()
