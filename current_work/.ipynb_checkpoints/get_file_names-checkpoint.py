import os
import glob as g
import rasterio as rio
import numpy as np
import earthpy.plot as ep
from matplotlib import pyplot as plt
import pandas as pd
import time

#Getting the file paths of only the bands we want - change this when running on new data
tifs_base_folder = "/ref_landcovernet_af_v1_source_landsat_8/ref_landcovernet_af_v1_source_landsat_8/*2018*"
tifs_file_list = g.glob(tifs_base_folder)
#Do the same for the labels - figure out a way to connect the labels to the images
labels_base_folder = "/ref_landcovernet_af_v1_labels/ref*"
labels_file_list = g.glob(labels_base_folder)
#Initializing pandas dataframe:
df = pd.DataFrame(columns=['tile', 'chip', 'x', 'y', 'f1', 'f2', 'labels'])

# The main loop to iterate through all files and add to csv
print("running...")
#Timing how long it takes to construct the dataframe
start_time = time.time()
for i in range(len(tifs_file_list[:1])):
    
    # Getting information about the image bands
    current_image = tifs_file_list[i]
    bands_file_list = g.glob(current_image + "/*.tif") #running this on only the current file directory
    band_1 = rio.open(bands_file_list[0])
    band_2 = rio.open(bands_file_list[1])
    f1 = band_1.read()[0]
    f2 = band_2.read()[0]

    # Getting information about the labels for the image 
    matching_list = [s for s in labels_file_list if current_image[121:129] in s]
    matching_dir = matching_list[0] #Getting the matched string out of the list
    current_image_label = rio.open(matching_dir + "/labels.tif")
    image_labels = current_image_label.read()[0]

    #Iterating through a single band to get x and y values, and adding them to the dataframe
    for x in range(len(f1)):
        for y in range(len(f1[0])):
            df = pd.concat([pd.DataFrame([[current_image[121:126], current_image[127:129], x, y, f1[x][y], f2[x][y], image_labels[x][y]]], columns=df.columns), df], ignore_index=True)
    print("image " + str(i + 1) + " successfully added to data frame")

df.to_csv("landcovernet_africa_data.csv", index=False)
print("csv download successful!")
print("--- %s seconds ---" % (time.time() - start_time))

