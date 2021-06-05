# Principles of Programming Languages and Compiler Design (CEID - University of Patras)
# Python Project 2021
# Christos-Panagiotis Balatsouras, StudentID: 1054335

# import python libraries
import requests
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import numpy as np
import warnings


# Global Variables
files_downloaded = 0
Country_1 = "Greece"
Country_2 = "Sweden"
Years = [2016, 2017, 2018, 2019]


class Dataset:
    def __init__(self, country1, country2, years):
        self.first_country = country1
        self.second_country = country2
        self.data1 = []
        self.data2 = []


def download(files_downloaded_count):  # download data in .xlsx format from the WEB
    # URLs
    url_nights_spent_residents = "https://ec.europa.eu/eurostat/databrowser-backend/api/query/1.0/LIVE/xlsx/en/download/cbe1232e-1456-4561-8e1d-8f15188c9a57"
    url_nights_spent_non_residents = "https://ec.europa.eu/eurostat/databrowser-backend/api/query/1.0/LIVE/xlsx/en/download/e0bb6a45-b0bc-4537-9175-611c32cfc97b"
    url_arrivals_residents = "https://ec.europa.eu/eurostat/databrowser-backend/api/query/1.0/LIVE/xlsx/en/download/af97e98f-35dc-45aa-bfe6-e70ae267cd1e"
    url_arrivals_non_residents = "https://ec.europa.eu/eurostat/databrowser-backend/api/query/1.0/LIVE/xlsx/en/download/67cc5b33-2c00-4767-bbd8-74224b7b78e5"

    # Download process
    print("Downloading: Nights spent at tourist accommodation establishments by residents, from URL: ", url_nights_spent_residents)
    req_nights_spent_residents = requests.get(url_nights_spent_residents, allow_redirects=True)
    open('nights_spent_by_residents.xlsx', 'wb').write(req_nights_spent_residents.content)
    print("File Downloaded Successfully")
    files_downloaded_count += 1

    print("Downloading: Nights spent at tourist accommodation establishments by non-residents, from URL: ", url_nights_spent_non_residents)
    req_nights_spent_non_residents = requests.get(url_nights_spent_non_residents, allow_redirects=True)
    open('nights_spent_by_non_residents.xlsx', 'wb').write(req_nights_spent_non_residents.content)
    print("File Downloaded Successfully")
    files_downloaded_count += 1

    print("Downloading: Arrivals of residents at tourist accommodation establishments, from URL: ", url_arrivals_residents)
    req_arrivals_residents = requests.get(url_arrivals_residents, allow_redirects=True)
    open('arrivals_by_residents.xlsx', 'wb').write(req_arrivals_residents.content)
    print("File Downloaded Successfully")
    files_downloaded_count += 1

    print("Downloading: Arrivals of non-residents at tourist accommodation establishments, from URL: ", url_arrivals_non_residents)
    req_arrivals_non_residents = requests.get(url_arrivals_non_residents, allow_redirects=True)
    open('arrivals_by_non_residents.xlsx', 'wb').write(req_arrivals_non_residents.content)
    print("File Downloaded Successfully")
    files_downloaded_count += 1

    print("\nDownload Completed Successfully!\nDownloaded ", files_downloaded_count, "files.\n")


def read_excel_data(file_name):  # Extract Useful Information from Excel Files
    dataset = Dataset(Country_1, Country_2, Years)
    year_columns = []
    row1 = None
    row2 = None

    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        wb = load_workbook(file_name)
    sheet_1 = wb['Sheet 1']
    for row in sheet_1.iter_rows(min_row=10, max_col=25, max_row=53):
        for cell in row:
            if cell.value == Country_1:
                row1 = cell.row
    for row in sheet_1.iter_rows(min_row=10, max_col=25, max_row=53):
        for cell in row:
            if cell.value == Country_2:
                row2 = cell.row
    for row in sheet_1.iter_rows(min_row=10, max_col=25, max_row=10):
        for cell in row:
            for item in Years:
                if cell.value == str(item):
                    col = cell.column
                    year_columns.append(col)

    numofyears = len(year_columns)
    # print(row1)
    # print(row2)
    # print(year_columns)

    for row in sheet_1.iter_rows(min_col=year_columns[0], min_row=row1, max_col=year_columns[numofyears-1], max_row=row1):
        for cell in row:
            if isinstance(cell.value, float):
                dataset.data1.append(int(cell.value))
    # print(dataset.data1)

    for row in sheet_1.iter_rows(min_col=year_columns[0], min_row=row2, max_col=year_columns[numofyears-1], max_row=row2):
        for cell in row:
            if isinstance(cell.value, float):
                dataset.data2.append(int(cell.value))
    # print(dataset.data2)

    return dataset


def plot(country1, country2, years, data1, data2, xlabel, ylabel, title):
    x_pos = np.arange(len(years))
    width = 0.25  # bar width

    fig, ax = plt.subplots()
    r1 = ax.bar(x_pos - width / 2, data1, width, label=country1, color='b')
    r2 = ax.bar(x_pos + width / 2, data2, width, label=country2, color='g')

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.set_xticks(x_pos)
    ax.set_yticks(np.arange(0, 100000000, 10000000))
    ax.set_xticklabels(years)
    ax.legend()

    fig.tight_layout()
    plt.show()

def main():
    # download(files_downloaded)
    Nights_spent_residents = read_excel_data('nights_spent_by_residents.xlsx')
    Nights_spent_non_residents = read_excel_data('nights_spent_by_non_residents.xlsx')
    Arrivals_residents = read_excel_data('arrivals_by_residents.xlsx')
    Arrivals_non_residents = read_excel_data('arrivals_by_non_residents.xlsx')

    plot(Nights_spent_residents.first_country, Nights_spent_residents.second_country, Years,
         Nights_spent_residents.data1, Nights_spent_residents.data2, "Year", "Million Nights Spent",
         "Nights spent at tourist accommodation establishments by residents")
    plot(Nights_spent_non_residents.first_country, Nights_spent_non_residents.second_country, Years,
         Nights_spent_non_residents.data1, Nights_spent_non_residents.data2, "Year", "Million Nights Spent",
         "Nights spent at tourist accommodation establishments by non-residents")
    plot(Arrivals_residents.first_country, Arrivals_residents.second_country, Years,
         Arrivals_residents.data1, Arrivals_residents.data2, "Year", "Million Arrivals",
         "Arrivals of residents at tourist accommodation establishments")
    plot(Arrivals_non_residents.first_country, Arrivals_non_residents.second_country, Years,
         Arrivals_non_residents.data1, Arrivals_non_residents.data2, "Year", "Million Arrivals",
         "Arrivals of non-residents at tourist accommodation establishments")


main()
