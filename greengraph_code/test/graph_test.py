from greengraph_code.graph import Greengraph
from nose.tools import assert_equal


def Greengraph_test(start, end):
    def Greengraph_init_test(start, end):
        greengraph_result = Greengraph(start, end)
        assert_equal(start, greengraph_result.start)
        assert_equal(end, greengraph_result.end)
        return 'Test completed. All good.'

    # def geolocate_test():

    # def location_sequence_test():

    # def green_between_test():
