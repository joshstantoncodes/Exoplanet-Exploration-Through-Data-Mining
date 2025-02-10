"""  Exoplanet Exploration through Data Mining
    The NASA Exoplanet Archive file consists of 38,090 entries across 92 columns covering the planets'
    mass relative to Earth and Jupiter, Insolation Flux, the Orbital Periods, among other properties.
    In total, 38,090 rows by 92 columns results in just over 3.5 million points of data, which need to
    be cleaned and tailored to answer the questions:

    • Are there any patterns in exoplanet discovery over time?
    • Do certain facilities have a propensity for discovering certain exoplanet types more than
    others?
    • Is there a relationship between planet size and gravity?
    • Does the number of stars relative to an exoplanet have any effect on its orbital?
    • Have specific discovery methods been more successful than others, or has a specific discovery
    method identified more planets than others?
    and likely more

    Author: Josh Stanton
    Date: February 09, 2025
"""

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import sklearn



# Using the absolute file path of the Exoplanet Archive
file_path = r"C:\Users\joshs\Documents\GitHub\Exoplanet-Exploration-Through-Data-Mining\NASA Exoplanet Archive.csv"
exoplanets = pd.read_csv(file_path)

print(exoplanets.columns)