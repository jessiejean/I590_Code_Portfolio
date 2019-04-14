#Assignment 9
#Question 1: Use NumPy to edit csv and save as.npy file
#Date: 10/22/2017
#Jessica Johnson



def main():
    import numpy as np
    from numpy import genfromtxt

    s=genfromtxt("Scores_all.csv", delimiter=",")
    scores=s[1:]
    scores[np.isnan(scores)] = 0
    scores = scores.astype(int)    
    np.save("scores",scores)
  
  
      
main()
