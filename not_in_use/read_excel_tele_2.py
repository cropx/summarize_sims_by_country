import pandas as pd


def find_country(country):

    df = pd.read_excel('TELE2_pdf_converted_to_excel.xlsx', sheet_name='Table_1')
    titles = df.columns[:10]
    country_found = df.iloc[:, :10].isin([country])
    result = [titles.to_list()]
    for row, col in zip(*country_found.to_numpy().nonzero()):
        result.append(df.iloc[row, :10].to_list())
    if len(result) == 1:
        country = country.replace('&', 'and')
        print(country)
        country_found = df.iloc[:, :10].isin([country])
        result = [titles.to_list()]
        for row, col in zip(*country_found.to_numpy().nonzero()):
            result.append(df.iloc[row, :10].to_list())
            print(result)
    return result


# find_country('Israel')