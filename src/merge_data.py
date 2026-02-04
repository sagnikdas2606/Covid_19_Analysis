def merge_all(confirmed_long, deaths_long, recovered_long):
    return (
        confirmed_long
        .merge(deaths_long, on=["Province/State","Country/Region","Date"], how = "left")
        .merge(recovered_long, on=["Province/State","Country/Region","Date"], how = "left")

    )