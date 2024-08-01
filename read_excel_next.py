import pandas as pd


def find_country(country):
    df = pd.read_excel('Telit Next Profile 2 - Global.xlsx', sheet_name='Telit Next Profile 2 - Global')
    titles = df.columns[:9]
    country_found = df.iloc[:, :9].isin([country])
    result = [titles.to_list()]
    for row, col in zip(*country_found.to_numpy().nonzero()):
        result.append(df.iloc[row, :9].to_list())
    print(result)
    return result
