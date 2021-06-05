# Principles of Programming Languages and Compiler Design (CEID - University of Patras)
# Python Project 2021
# Christos-Panagiotis Balatsouras, StudentID: 1054335

# import python libraries
import requests
import xlrd

# Global Variables
files_downloaded_count = 0

# download data in .xlsx format from the WEB
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
