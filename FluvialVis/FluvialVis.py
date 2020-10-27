import matplotlib.pyplot as plt
import numpy as np
from landlab.plot import graph, plot_network_and_parcels
from landlab.plot.imshow import imshow_grid, imshow_grid_at_node


def plot_discharge(hydrograph_time, discharge):
    fig=plt.figure()
    plt.plot(hydrograph_time, discharge_at_outlet, "b-", label="at outlet")
    plt.ylabel("Discharge (cms)")
    plt.xlabel("Time (seconds)")
    plt.legend(loc="upper right")
    return fig
def plot_depth(hydrograph_time, height_at_outlet):
    fig=plt.figure()
    plt.plot(hydrograph_time, height_at_outlet, "b-", label="at outlet")
    plt.ylabel("Water depth (m)")
    plt.xlabel("Time (seconds)")
    plt.legend(loc="upper right")
    return fig

def plot_sed_volume(parcels):
    parcel_vol_on_grid = parcels.dataset["volume"].values
    #if s
    parcel_vol_on_grid[parcels.dataset["element_id"].values==-2]=0
    sum_parcel_vol_on_grid = np.sum(parcel_vol_on_grid, axis=0)
    fig=plt.figure(4)
    plt.plot(np.asarray(parcels.time_coordinates), 
             sum_parcel_vol_on_grid[0]-sum_parcel_vol_on_grid,'b-'
            )
    plt.ylabel('Total volume of parcels that left catchment $[m^3]$')
    plt.xlabel('Time (seconds)')
    return fig

def plot_outlet_conditions(hydrograph_time, discharge, height_at_outlet, parcels, filepath = ""):
    fig1 = plot_discharge(hydorgraph_time, discharge)
    fig2 = plot_depth(hydrograph_time, height_at_outlet)
    fig3 = plot_sed_volume(parcels)
    if len(filepath) > 0:
        fig1.savefig(filepath+"runoff_discharge.jpeg")
        fig2.savefig(filepath+"runoff_height.jpeg")
        fig3.savefig(filepath+"sediment_volume.jpeg")
        print("outlet figures saved")
    else: 
        plt.show()
    
def plot_network(network_grid):
    ## Plot nodes
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    graph.plot_nodes(network_grid)
    plt.title("Nodes")

    ## Plot nodes + links
    plt.subplot(1,2,2)
    graph.plot_nodes(network_grid,with_id=False,markersize=4)
    graph.plot_links(network_grid)
    plt.title("Links")
    plt.show()
def plot_topography(network_grid, new_network_grid):
# Plot topography
    plt.figure(figsize=(12,8))
    graph.plot_nodes(network_grid,with_id=False,markersize=4)
    graph.plot_links(new_network_grid,with_id=False)
    imshow_grid(rmg, 'topographic__elevation',\
                plot_name="Basin topography",\
                color_for_closed=None,\
                colorbar_label="$z$ [m]")
    plr.show()
    
def plot_storm(rmg, h):
    plt.figure(figsize=(14,8))
    plt.subplot(1,2,1)
    imshow_grid(rmg, 'topographic__elevation',\
                plot_name="Basin topography",\
                color_for_closed=None,\
                colorbar_label="$z$ [m]",\
                output=None,shrink=0.5)
    plt.subplot(1,2,2)
    imshow_grid(rmg, h,\
                plot_name="Rain distribution",\
                color_for_closed=None,\
                colorbar_label="Initial rain $h$ [m]",\
                cmap="winter",output=None,shrink=0.5)
    plt.show()
def plot_initial_floodplain(zFP, nX, nY, grid):
    # Plot 2D domain topography
    plt.figure(figsize=(14,8))
    plt.subplot(1,2,1)
    ls = plt.LightSource(azdeg=315, altdeg=45)
    plt.imshow(ls.hillshade(np.reshape(zFP,[nX,nY]), vert_exag=10), cmap='gray')

    #Plot 2D domain hydraulic cond.
    plt.subplot(1,2,2)
    imshow_grid(grid,'hydraulic_conductivity', plot_name="Hydraulic Conductivity", cmap="winter")
    fig.show()
def plot_overland_flow(rmg, cmap, outlet_nearest_raster_cell,elapsed_time,filepath = ""):  
    #Plot overland flow 
    fig=plt.figure()
    imshow_grid(rmg,'topographic__elevation',colorbar_label='Elevation (m)')
    imshow_grid(rmg,'surface_water__depth',limits=(0,2),cmap=cmap,colorbar_label='Water depth (m)')
    plt.title(f'Time = {round(elapsed_time,1)} s')
    plt.plot(rmg.node_x[outlet_nearest_raster_cell], rmg.node_y[outlet_nearest_raster_cell], "yo")
    if len(filepath) > 0:
        fig.savefig(filepath + "flow/" + str(elapsed_time).zfill(5) + ".png")
    else: 
        plt.show()
def plot_floodplain(grid, zFP, nX, nY, WaterMap, elapsed_time, filepath = ""):
    fig = plt.figure(figsize=(14, 8))
    plt.imshow(ls.hillshade(np.reshape(z,[nX,nY]), vert_exag=10), cmap='gray',origin="lower")
    imshow_grid(grid,'surface_water__depth',
          limits=(0,1),cmap=WaterMap,                    
          colorbar_label="Water depth (m)",                    
          plot_name="Time = %i" %elapsed_time)
    if len(filepath) > 0:
        fig.savefig(filepath + "floodplain/" + str(elapsed_time).zfill(5) + ".png")
    else: 
        plt.show()
def plot_parcels(new_grid, parcels, elapsed_time, outlet_nearest_raster_cell, filepath = ""):
    #Plot sediment parcels locationss
    fig = plt.figure(figsize = (14,8))
    plt.subplot(plt.subplot(1,2,1))
    plot_network_and_parcels(
            new_grid, parcels, 
            parcel_time_index=len(parcels.time_coordinates)-1)
    plt.plot(rmg.node_x[outlet_nearest_raster_cell], rmg.node_y[outlet_nearest_raster_cell], "yo")
    plt.title(f'Time = {round(elapsed_time,1)} s')

    plt.subplot(plt.subplot(1,2,2))
   
        #grain size
    parcel_D = parcels.dataset.D.values
    parcel_D_off_grid=parcel_D[parcels.dataset["element_id"].values==-2] 

    # the histogram of the data
    plt.hist(parcel_D_off_grid*1000, histtype='bar')
    plt.xlabel('grain size (mm)')
    plt.ylabel('Count')
    plt.title('Histogram of grain sizes that left grid')
    plt.text(0.011, 700, r'original distribution $\mu=2 mm$')
    plt.xlim(0, 20)
    plt.ylim(0, 4000)
    plt.grid(True)
    plt.show()
    if len(filepath) > 0:
        fig.savefig(filepath + "parcels/" +str(elapsed_time).zfill(5) + ".png")
    else: 
        plt.show()
