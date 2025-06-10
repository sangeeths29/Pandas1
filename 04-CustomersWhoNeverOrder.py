# Problem 4 - Customer Who Never Order ( https://leetcode.com/problems/customers-who-never-order/ )
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]
    return df[['name']].rename(columns = {'name':'Customers'})