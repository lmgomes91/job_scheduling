import pandas as pd
import numpy as np


def open_dataset() -> pd.DataFrame:
    df = pd.read_excel('./data/Book1.xlsx', sheet_name='Sheet1', header=0, skiprows=1)
    df.replace({np.nan: None}, inplace=True)

    return df
