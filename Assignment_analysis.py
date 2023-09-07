#   Importing Packages
import pandas as pd

#   Reading Data
data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

# Subsetting data
new_df = data[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

#   Viewing new data
print(new_df)
