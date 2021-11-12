import cmath as cm

#   Mathematical constants list
#   This file is going to be a comprehensive list of constants to use
#   I have to import the library cmath for a few functions because
#   I have not figured out how to do things like a square root by
#   hand and will have to do it at some point I guess. The point here
#   Is I am not a math genius and yet I love numbers so therefore I will
#   Settle utilizing some math from pythons library and recreating others
#   Mine will probably not be as fancy but they will be mine. HA HA HA
#
#   Written by: Justin Blacksher
#
# --------------------------- PI ---------------------------------------
# Pi
# There will be three levels of accuracy.
# 2 decimal points
# 4 decimal points
# 6 decimal points

PI = 3.14           # Pi to 2 Decimal points
PI_4 = 3.1415       # Pi to 4 Decimal points
PI_6 = 3.141592     # Pi to 6 Decimal points

def pi_help():      # Pi help function to print the constants
    return "PI = 3.14, PI_4 = 3.1415, PI_6 = 3.141596"

# ---------------------------------------------------------------------

# ------------------------ The Golden Mean ----------------------------
# The Golden Mean
# Pentagon, Pine Cones, and elegant buildings OH MY!
#
#
# G = (sqrt(5) - 1)/2
GOLDEN_MEAN = 0.6180339887498950

def goldenMean_help():
    return "Estimated value to 16 decimal places. Formula: G = (sqrt(5) - 1)/2"

def goldenMean():
    return (cm.sqrt(5) - 1) / 2
#
#
#
# -------------------------------------------------------------------------