# encoding: latin2
"""
Test distance functions 
"""
__author__ = "Juan C. Duque"
__credits__ = "Copyright (c) 2009-11 Juan C. Duque"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "RiSE Group"
__email__ = "contacto@rise-group.org"

from clusterpy.core.toolboxes.cluster.componentsAlg.distanceFunctions import square_double

def test_square_double_of_many_items_list():
    """ Test square_double function
    Squares each element of a list and then returns the sum
    of all the squared elements.
    """
    input_list = [-4, -3, 0, 1, 2, 3, 0.5]
    expected_ans = float(39.25)
    output = square_double(input_list)
    assert expected_ans == output

def test_distance_area_2_area_euclidean_squared():
    assert False

def test_hamming_distance():
    assert False

def test_distance_area_2_area_hausdorff():
    assert False