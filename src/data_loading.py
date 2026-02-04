import pandas as pd

def load_datasets():
    confirmed = pd.read_csv("C:/Users/SAGNIK/Downloads/Covid_19_Analysis/Covid_19_Analysis/data/covid_19_confirmed.csv")
    deaths = pd.read_csv("C:/Users/SAGNIK/Downloads/Covid_19_Analysis/Covid_19_Analysis/data/covid_19_deaths.csv")
    recovered = pd.read_csv("C:/Users/SAGNIK/Downloads/Covid_19_Analysis/Covid_19_Analysis/data/covid_19_recovered.csv")

    return confirmed, deaths, recovered

def inspect_dataframes(*dfs):
    for df in dfs:
        print(df.info())