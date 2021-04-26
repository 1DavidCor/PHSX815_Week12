# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:05:48 2021

@author: d338c921
"""

#Write a program that illustrates, in some way, the Central Limit Theorem (preferably with one or more figures)

#For example, the Central Limit Theorem indicates that the normalized sum (i.e. the arithmetic mean) of random variables, 
#each independently sampled from the same distribution, will asymptotically follow a Gaussian distribution. 
#Try sampling a continuous variable from a probability distribution that is *not* a Gaussian - repeat this N times and take the average. 
#Then repeat *that* again many times (so M "experiments" each with N samples) - what does this distribution of averages look like? As you increase N?

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: \n -lambda [rate parameter of exponential distribution] \n -n [Exponential disribution sample size] \n -Nexp [# of experiments] \n")
        print
        sys.exit(1)

  
    # default lambda
    lam = 0.5
    
    #default sample size:
    n = 10
    
    #default number of experiments
    Nexp = 10

    # read the user-provided values from the command line (if there)
    if '-lambda' in sys.argv:
        p = sys.argv.index('-lambda')
        lam = float(sys.argv[p+1])
    if '-n' in sys.argv:
        p = sys.argv.index('-n')
        n = int((sys.argv[p+1]))
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Nexp = int((sys.argv[p+1]))

    #repeat this Nexp times; store the averages:
    avg_arr = []
    for j in [n, 10*n, 50*n, 100*n, 500*n, 1000*n]:
        for i in range(Nexp):
            #sample from an exponential distribution:
            exp = stats.expon.rvs(scale = 1 / lam, size = j)
            avg = np.mean(exp)
            avg_arr = np.append(avg_arr, avg)
        #fit a gaussianto the data
        mu, sig = stats.norm.fit(avg_arr)
        #create histograms for different values of n; plot a gaussian fit
        plt.figure()
        plt.title("Distribution of Averages: N = " + str(j))
        plt.xlabel("Average Value")
        plt.ylabel("Probability Density")
        plt.hist(avg_arr, 100, density = True, label = "Distribution of Averages")
        #plt.hist(avg_arr, 100, weights = np.full(avg_arr.shape, 1) / j) weights give probabilities [0,1] on the y axis
        plt.plot(np.linspace(0, 4, 1000), stats.norm.pdf(np.linspace(0, 4, 1000), mu, sig), label = "mu = " + str(np.round(mu, 2)) + ", sig = " + str(np.round(sig, 2)))
        plt.legend()
        plt.show()
        
    
    
    
    
