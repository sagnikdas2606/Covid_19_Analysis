import pandas as pd

def to_long(df, value_name):
    long_df = df.melt(
        id_vars = ["Province/State", "Country/Region", "Lat", "Long"],
        var_name = "Date",
        value_name = value_name
    )

    long_df["Date"] = pd.to_datetime(long_df["Date"])
    return long_df