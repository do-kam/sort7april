#Sources used: https://www.geeksforgeeks.org/python-program-for-quicksort/
# https://www.educative.io/edpresso/how-to-implement-quicksort-in-python

import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from time import time

def QuickSort(liste):
    myarray2=liste.copy()
    lenge = myarray2.shape
    lenge =(lenge[0])
    if lenge < 2:
        return (myarray2)

    pos = 0  # the partitioning element
    for i in range(1, lenge):
        if myarray2[i] <= myarray2[0]:
            pos += 1 #increment pos of smaller element
            myarray2[pos], myarray2[i] = myarray2[i], myarray2[pos]
            #temp = myarray2[i]
            #myarray2[i] = myarray2[pos]
            #myarray2[pos] = temp

    myarray2[pos], myarray2[0] = myarray2[0], myarray2[pos]  #move pivot to correct position

    #temp = myarray2[0]
    #myarray2[0] = myarray2[pos]
    #myarray2[pos] = temp
    leftside = np.array(QuickSort(myarray2[0:pos]))
    rightside = np.array(QuickSort(myarray2[pos + 1:lenge]))

    #putting them together
    wertinmitte = myarray2[pos]
    mitte = np.array([wertinmitte])
    arr = np.concatenate((leftside,mitte,rightside))
    return arr

def check_my_sort():
    # general initialization
    N_pts = 5  # number of different lentghs for which sort time is measured
    Nt = 10  # number of repetitions to measure time
    results = np.zeros([2, N_pts, 2])

    # range of lengths for built in method
    Emin = 5  # log10 of minimal sample size
    Emax = 6  # log10 of maximal sample size
    pts = np.linspace(Emin, Emax, N_pts)  # contains exponents for list lengths
    for i in range(N_pts):
        N = int(10 ** (pts[i]))  # lentgh of list
        num_list = np.zeros(N)
        print(N)
        # inititalization for timing of list with length N
        for j in range(N):
            num_list[j] = rnd.uniform(0, 100)
        # timing for built in method
        t1 = time()
        for t in range(Nt):
            sorted_num_list = np.sort(num_list, kind='mergesort')
        t2 = time()
        # write time for each list length in results
        results[0, i, 0] = N
        results[0, i, 1] = (t2 - t1) / Nt

    # range of lengths for built in method
    Emin = 2  # log10 of minimal sample size
    Emax = 3  # log10 of maximal sample size
    pts = np.linspace(Emin, Emax, N_pts)  # contains exponents for list lengths
    for i in range(N_pts):
        N = int(10 ** (pts[i]))  # lentgh of list
        num_list = np.zeros(N)
        print(N)
        # inititalization for timing of list with length N
        for j in range(N):
            num_list[j] = rnd.uniform(0, 100)
        # timing for myquicksort
        t1 = time()
        for t in range(Nt):
            sorted_num_list = QuickSort(num_list)
        t2 = time()
        # write time for each list length in results
        results[1, i, 0] = N
        results[1, i, 1] = (t2 - t1) / Nt

    print(results[0, :, :])
    print(results[1, :, :])
    x1 = np.log10(results[0, :, 0])
    y1 = np.log10(results[0, :, 1])
    x2 = np.log10(results[1, :, 0])
    y2 = np.log10(results[1, :, 1])
    k1, d1 = np.polyfit(x1, y1, 1)
    k2, d2 = np.polyfit(x2, y2, 1)

    plt.figure(0)
    plt.plot(x1, y1, 'x')
    plt.plot(x1, k1 * x1 + d1, '-')
    plt.ylabel('log(t)')
    plt.xlabel('log(N)')
    print('Slope and intercept of built-in in log-log plot are ' + str(k1)
          + ' and ' + str(d1))

    plt.figure(1)
    plt.plot(x2, y2, 'x')
    plt.plot(x2, k2 * x2 + d2, '-')
    print('Slope and intercept of myquicksort in log-log plot are ' + str(k2)
          + ' and ' + str(d2))
    plt.show()

myarray= np.array([4.2,2.1,7.5,3.9,1.1,6.8])
#myarray = np.array([4,2,7,3,1,6])

print("unsorted ", myarray)
print("sorted ", QuickSort(myarray))

print("has not changed original")
print(myarray)
check_my_sort()
