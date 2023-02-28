# Run command 'python3'
import rasterio
from matplotlib import pyplot as plt
from rasterio.plot import show
import earthpy as ep
from matplotlib.colors import ListedColormap

path = '/Users/nate/Documents/github/Capstone-Project/ref_landcovernet_af_v1_labels/ref_landcovernet_af_v1_labels_'
name = '/labels.tif'

color_key = ['#0000ff', '#888888', '#d1a46d', '#f5f5ff', '#d64c2b', '#186818', '#00ff00']

for x in range(10,29):
    sat = '28QDE_' + str(x)
    path_sat = path + sat + name
    img = rasterio.open(path_sat)
    ep.plot_bands(img, cmap = ListedColormap(color_key))
    plt.show()