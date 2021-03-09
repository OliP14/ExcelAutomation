import pandas as pd
import os

compatible_file_path = ""
temp_filename = ""

def make_compatible():
    #given_file = '/Users/oliverpasquesi/Downloads/Copy of SUPERMOSS WEB.xls'
    given_file = input("Enter the path of the file you would like to convert: ")

    read_given_file = pd.read_excel(given_file)

    given_file_df = pd.DataFrame(read_given_file)
    adjusted_given_file_df = given_file_df.rename(columns={'SKU': 'Variant SKU', 'Description': 'Title', 'Primary\nVendor': 'Vendor', 'Repl Cost': 'Variant Cost', 'Retail': 'Variant Price'})
    adjusted_given_file_df = adjusted_given_file_df.drop(columns={"QOH", "QOO", "Pop Code", "YTD Units"})
    
    print(adjusted_given_file_df)
    #temp_filename = input("Enter the product line for temporary file: ")
    #compatible_file = adjusted_given_file_df.to_excel("Compatible" + temp_filename + "File.xlsx", index=False)

def get_path():
    global compatible_file_path

    dir_path = os.path.dirname(os.path.realpath(__file__))

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file == temp_filename:
                compatible_file_path = root + '/' + str(file)

def combine_files():
    template_file = '/Users/oliverpasquesi/OneDrive - College of Lake County/Store Spreadsheets/HeaderTemplate.xlsx'
    excel_files = [template_file, compatible_file_path]
    read_files = []

    file_name = input("File name: ")

    for file in excel_files:
        read_files.append(pd.read_excel(file))

    merged_file = pd.concat(read_files)
    # To add all of the universal column data, maybe turn merged_file into a new data frame and then add the data to each respective column that way?
    merged_file_df = pd.DataFrame(merged_file)
    merged_file.to_excel(file_name + ".xlsx", index=False)
    print(merged_file_df)


make_compatible()
get_path()
combine_files()