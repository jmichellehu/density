import numpy as np

# Bulk density model based on climate classes of seasonal snow
# Sturm's model parameters by snow class - Table 4 in Sturm et al., 2010
# Ephemeral snow lacked sufficient systematic measurements, was excluded
# rho_max is the maximum bulk density of the season
# rho_init is the initial seasonal bulk density
# k1 is the densification parameter for snow_depth
# k2 is the densification parameter for DOY
def get_sturm_density():
    snow_classes = ["Alpine", "Maritime", "Prairie", "Tundra", "Taiga"]
    rho_maxes = [0.5975, 0.5979, 0.5940, 0.3630, 0.2170]
    rho_inits = [0.2237, 0.2578, 0.2332, 0.2425, 0.2170]
    k1s = [0.0012, 0.0010, 0.0016, 0.0029, 0.0000]
    k2s = [0.0038, 0.0038, 0.0031, 0.0049, 0.0000]

    # Will need to extract day of year, pre-existing snow depth, and climate class based on image metadata (location, date of collection, etc.)
    DOY_i = -92          # specify the day of year of interest (-92 = Oct 1; +181 = June 30)
    h_i = 1.4           # ith observation of snow_depth in meters

    climate_class = 0   # values range 0-4 based on snow class

    snow_class = snow_classes[climate_class]
    rho_max = rho_maxes[climate_class]
    rho_init = rho_inits[climate_class]
    k1 = k1s[climate_class]
    k2 = k2s[climate_class]

    # t = snow deposition history
    # rho_b = function of h_s, t, and initial snow layer density
    rho_b_model = (rho_max - rho_init) * (1-np.exp(-k1 * h_i - k2 * DOY_i)) + rho_init
    # print(rho_b_model)
    return rho_b_model

    # Basic SWE calculation using snow_depth and bulk_density
    # h_s = 1             # snow_depth in meters
    # rho_w = 1           # density_of_water in grams/cubic cm
    # rho_b = 0.3         # bulk_density in grams/cubic cm

    # swe = h_s * rho_b_model / rho_w
    # print("SWE from basic calculations using bulk density based on snow class is "
    # + str(format(swe, '.2f')) + " meters in the " + snow_class + " snow class.")
