import pandas as pd
from typing import List
from .simulation import Customer

def create_results_dataframe(customers: List[Customer]) -> pd.DataFrame:
    data = {
        'customer_id': [c.customer_id for c in customers],
        'arrival_time': [c.arrival_time for c in customers],
        'service_start_time': [c.service_start_time for c in customers],
        'service_time': [c.service_time for c in customers],
        'departure_time': [c.departure_time for c in customers],
        'waiting_time': [c.service_start_time - c.arrival_time for c in customers],
        'system_time': [c.departure_time - c.arrival_time for c in customers]
    }
    return pd.DataFrame(data)

def save_results_to_csv(df: pd.DataFrame, filename: str = 'simulation_results.csv'):
    df.to_csv(filename, index=False)

def load_results_from_csv(filename: str = 'simulation_results.csv') -> pd.DataFrame:
    return pd.read_csv(filename)