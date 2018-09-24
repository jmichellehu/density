import numpy as np

# Bulk density model based on climate classes of seasonal snow
DOY_i = -92          # specify the day of year of interest (-92 = Oct 1; +181 = June 30)
h_i = 1.4           # ith observation of snow_depth in meters

# Determine model parameters based on climate snow class
# Ephemeral snow lacked sufficient systematic measurements, was excluded
# rho_max is the maximum bulk density of the season
# rho_init is the initial seasonal bulk density
# k1 is the densification parameter for snow_depth
# k2 is the densification parameter for DOY
climate_class = 3   # values range 1-5 based on snow class

if climate_class == 1:
    # Alpine (1)
    snow_class = "Alpine"
    rho_max = 0.5975
    rho_init = 0.2237
    k1 = 0.0012
    k2 = 0.0038
elif climate_class == 2:
    # Maritime (2)
    snow_class = "Maritime"
    rho_max = 0.5979
    rho_init = 0.2578
    k1 = 0.0010
    k2 = 0.0038
elif climate_class == 3:
    # Prairie (3)
    snow_class = "Prairie"
    rho_max = 0.5940
    rho_init = 0.2332
    k1 = 0.0016
    k2 = 0.0031
elif climate_class == 4:
    # Tundra (4)
    snow_class = "Tundra"
    rho_max = 0.3630
    rho_init = 0.2425
    k1 = 0.0029
    k2 = 0.0049
elif climate_class == 5:
    # Taiga (5)
    snow_class = "Taiga"
    rho_max = 0.2170
    rho_init = 0.2170
    k1 = 0.0000
    k2 = 0.0000
else:
    # display error
    print("Incorrect climate class value.")

# t = snow deposition history
# rho_b = function of h_s, t, and initial snow layer density
rho_b_model = (rho_max - rho_init) * (1-np.exp(-k1 * h_i - k2 * DOY_i)) + rho_init

print(rho_b_model)

# Basic SWE calculation using snow_depth and bulk_density
h_s = 1             # snow_depth in meters
rho_w = 1           # density_of_water in grams/cubic cm
# rho_b = 0.3         # bulk_density in grams/cubic cm

swe = h_s * rho_b_model / rho_w
print("SWE from basic calculations using bulk density is "
+ str(format(swe, '.2f')) + " meters in the " + snow_class + " snow class.")
