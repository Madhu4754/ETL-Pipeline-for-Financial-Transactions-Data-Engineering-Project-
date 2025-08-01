import pandas as pd, os, yaml
import sqlite3

def load_config(path='config.yaml'):
    with open(path) as f:
        return yaml.safe_load(f)

def etl_process(cfg):
    csv_path=cfg['input']['csv']
    df=pd.read_csv(csv_path)
    df.drop_duplicates(subset=['txn_id'], inplace=True)
    df.fillna({'status':'pending'}, inplace=True)
    df=df[df['amount']>0]
    os.makedirs('data', exist_ok=True)
    conn=sqlite3.connect('data/transactions.db')
    df.to_sql('transactions', conn, if_exists='replace', index=False)
    print('ETL complete. Loaded to DB. Records:', len(df))

if __name__=='__main__':
    cfg=load_config('config.yaml')
    etl_process(cfg)
