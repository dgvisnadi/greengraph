from matplotlib import pyplot as plt
from greengraph_code.graph import Greengraph
import seaborn

def make_graph(start, end, steps, out=False):
    '''
    Generate a plot showing intensity of green pixels between two locations.

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
    plt.xlabel("Steps")
    plt.ylabel("Green Pixel")
    plt.title("Number of green pixel from " + start + " to " + end)

    if out:
        plt.savefig(out)
    else:
        plt.show()
