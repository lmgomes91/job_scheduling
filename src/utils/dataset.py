import pandas as pd
import numpy as np


def open_dataset() -> pd.DataFrame:
    df = pd.read_excel('./data/Base01.xlsx', sheet_name='base', header=0, skiprows=0)
    df.replace({np.nan: None}, inplace=True)

    return df


def format_data(dataset: pd.DataFrame) -> list:
    service_orders = []

    for _, row in dataset.iterrows():

        service_order = {
            'id': row['OS'],
            'jobs': []
        }

        if row['CONVERTEDOR']:
            service_order['jobs'].append([row['CONVERTEDOR'], row['Tempo1']])

        if row['TRATAMENTO']:
            service_order['jobs'].append([row['TRATAMENTO'], row['Tempo2']])

        if row['TRATAMENTO.1']:
            service_order['jobs'].append([row['TRATAMENTO.1'], row['Tempo3']])

        if row['LINGOTAMENTO']:
            service_order['jobs'].append([row['LINGOTAMENTO'], row['Tempo4']])

        service_orders.append(service_order)

    return service_orders


def format_data_no_machine_specify(dataset: pd.DataFrame) -> list:
    service_orders = []

    for _, row in dataset.iterrows():

        service_order = {
            'id': row['OS'],
            'jobs': []
        }

        if row['CONVERTEDOR']:
            service_order['jobs'].append(['CONVERTEDOR', row['Tempo1']])

        if row['TRATAMENTO']:
            service_order['jobs'].append(['TRATAMENTO', row['Tempo2']])

        if row['TRATAMENTO.1']:
            service_order['jobs'].append(['TRATAMENTO', row['Tempo3']])

        if row['LINGOTAMENTO']:
            service_order['jobs'].append(['LINGOTAMENTO', row['Tempo4']])

        service_orders.append(service_order)

    return service_orders
