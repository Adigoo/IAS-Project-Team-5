import sys

from imageio import imread
from scipy.linalg import norm
import pickle
from scipy import sum, average

def main():
    # read images as 2D arrays (convert to grayscale for simplicity)
    arr = imread("frame0001.jpg").astype(float)
    if len(arr) == 3:
        img1 =  average(arr, -1)  # average over the last axis (color channels)
    else:
        img1 = arr

    arr = imread("frame0100.jpg").astype(float)
    if len(arr) == 3:
        img2 =  average(arr, -1)  # average over the last axis (color channels)
    else:
        img2 = arr

    
    rng = img1.max()-img1.min()
    amin = img1.min()
    img1 = (img1-amin)*255/rng

    rng = img2.max()-img2.min()
    amin = img2.min()
    img2 = (img2-amin)*255/rng

    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    n_m,n_0 = m_norm, z_norm


    # print("Manhattan norm:", n_m, "/ per pixel:", n_m/img1.size)
    # print("Zero norm:", n_0, "/ per pixel:", n_0*1.0/img1.size)

    if n_m/img1.size > 2:
      return 1
    return 0

with open ("model.pkl","wb") as handle:
    pickle.dump(main,handle)