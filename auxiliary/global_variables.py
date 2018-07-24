from model import *

global network
global opt
global mesh_ref
global mesh_ref_LR
# load template at high and low resolution
mesh_ref = trimesh.load("/home/thibault/Downloads/MPI-FAUST/training/ref/reg_color_ref_HR.ply", process=False)
mesh_ref_LR = trimesh.load("/home/thibault/Downloads/MPI-FAUST/training/ref/reg_color_ref.ply", process=False)
red_LR = np.load("./data/red_LR.npy")
green_LR = np.load("./data/green_LR.npy")
blue_LR = np.load("./data/blue_LR.npy")
red_HR = np.load("./data/red_HR.npy")
green_HR = np.load("./data/green_HR.npy")
blue_HR = np.load("./data/blue_HR.npy")
