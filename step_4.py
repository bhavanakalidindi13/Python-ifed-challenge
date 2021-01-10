import time
import pandas as pd
import numpy as np


def f1(subset_elements,all_elements):
    """
    Uses for loop to get common elements from the given two lists.

    Parameters:
    subset_elements (list):
        contains list of elements of subset_elemets.txt
    all_elements (list):
        contains list of elements of all_elements.txt

    """

    start = time.time()
    verified_elements = []

    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


def f2(subset_elements,all_elements):
    """
    Uses numpy.intersect1d() function to get common elements from the given two lists.

        Parameters:
        subset_elements (list):
            contains list of elements of subset_elemets.txt
        all_elements (list):
            contains list of elements of all_elements.txt

    """

    start = time.time()
    verified_elements = np.intersect1d(subset_elements, all_elements)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


def f3(subset_elements,all_elements):
    """
    Uses set().intersecton() data structure function to get common elements from the given two lists.

        Parameters:
        subset_elements (list):
            contains list of elements of subset_elemets.txt
        all_elements (list):
            contains list of elements of all_elements.txt

    """

    start = time.time()
    verified_elements = set(all_elements).intersection(subset_elements)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


def main():
    """
    Reads data from subset_elemets.txt and all_elements.txt and stores in subset_elements and all_elements resp.

    """

    with open('subset_elemets.txt') as f:
        subset_elements = f.read().split('\n')

    with open('all_elements.txt') as f:
        all_elements = f.read().split('\n')

    f1(subset_elements,all_elements)
    f2(subset_elements,all_elements)
    f3(subset_elements,all_elements)


if __name__ == "__main__":
    main()
