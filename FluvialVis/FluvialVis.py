import matplotlib.pyplot as plt
import numpy as np
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
    if len(filepath) > 0
        fig1.savefig(filepath+"runoff_discharge.jpeg")
        fig2.savefig(filepath+"runoff_height.jpeg")
        fig3.savefig(filepath+"sediment_volume.jpeg")
        print("outlet figures saved")
    else 
        plt.show()
    
    