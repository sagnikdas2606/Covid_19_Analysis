def check_missing(df):
    return df.isnull().any().any()

def fill_missing(df):
    df = df.copy()
    df["Province/State"] = df["Province/State"].fillna("All Province")
    return df.ffill()

def clean_datasets(confirmed, deaths, recovered):
    deaths = fill_missing(deaths)
    recovered = fill_missing(recovered)
    confirmed["Province/State"] = confirmed["Province/State"].fillna("All Province")
    return confirmed, deaths, recovered
