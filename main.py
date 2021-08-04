import pandas as pd

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also

    all_products = pd.read_excel("./products.xlsx", )
    nan_tuple = ([(i, item) for i, item in enumerate(all_products["CodBarre"]) if not item > 0])
    for nan in nan_tuple:
        print(all_products.loc[[nan[0]]])
