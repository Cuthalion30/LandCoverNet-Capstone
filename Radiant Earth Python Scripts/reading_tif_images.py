import rasterio as rs
from rasterio.plot import show
from matplotlib import pyplot as plt
import os
import cv2
import numpy as np
from rasterio.enums import ColorInterp

#Reading in all bands from a specified folder
folder = 'image1/'
bands = os.listdir(folder)
current_band = bands[13]
img = rs.open(folder + current_band)


# with rs.open(folder + current_band, 'r+') as src:
#     src.colorinterp = [ColorInterp.red]
#     show(src.read())

image1 = plt.imread(folder + current_band)
plt.imshow(image1)
plt.show()

# plt.imshow(img.read(1), cmap='pink')
# plt.show()

#Creating a figure visualizing all bands in a geotif
# fig = plt.figure()
# rows = 2
# columns = 7

# for i in range(0, len(bands)):
#     img = rs.open(folder + bands[i])
#     fig.add_subplot(rows, columns, i+1)
#     plt.imshow(img.read(1))
#     plt.axis('off')
#     #plt.title(bands[i])

# plt.show()
