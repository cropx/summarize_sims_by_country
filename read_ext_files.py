import pandas as pd
from PIL import Image


class ReadExcel:
    def __init__(self, ):
        self.try_typos = None
        self.sim = None
        self.df = None
        self.country = None

    def open_excel_files(self):
        if self.sim == "next":
            self.df = pd.read_excel('Telit Next Profile 2 - Global.xlsx', sheet_name='Telit Next Profile 2 - Global')
            print("next")
        if self.sim == "tele2":
            self.df = pd.read_excel('TELE2_pdf_converted_to_excel.xlsx', sheet_name='Table_1')
            print("tele2")

    def find_country(self):
        titles = self.df.columns[:9]
        result = [titles.to_list()]
        found = False
        while not found:
            country_found = self.df.iloc[:, :9].isin([self.country])
            for row, col in zip(*country_found.to_numpy().nonzero()):
                result.append(self.df.iloc[row, :9].to_list())
            if len(result) == 1 and self.try_typos < 5:
                print("result) == 1")
                self.look_for_country_typos()
            if len(result) > 1:
                print("result > 1")
                found = True
                return result
            if self.try_typos > 4:
                print("result > 3")
                found = True

    def look_for_country_typos(self):
        file_path = 'compare_country_table.xlsx'
        df = pd.read_excel(file_path)
        data_dict = df.to_dict(orient='list')

        for i in range(len(df)):
            row = {key: data_dict[key][i] for key in data_dict}
            if str(row["Short_option"]) in self.country:
                if self.sim == "tele2":
                    self.country = row['Tele2']
                if self.sim == "next":
                    self.country = row['Next']
                if self.sim == "hologram":
                    self.country = row['Hologram']
        self.try_typos += 1

    def get_hologram_pic(self):
        found = False
        while not found:
            try:
                im = Image.open(f'countries\{self.country}.png')
                print(im)
                found = True
                return im
            except:
                if self.try_typos > 3:
                    found = True
                self.look_for_country_typos()

    def get_data(self, country, sim):
        self.sim = sim
        self.country = country
        self.try_typos = 1
        if self.sim == "next" or self.sim == "tele2":
            self.open_excel_files()
            result = self.find_country()
            return result
        if self.sim == "hologram":
            self.try_typos = 0
            result = self.get_hologram_pic()
            return self.country, result

