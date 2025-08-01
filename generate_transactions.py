import pandas as pd, numpy as np, os, json
from datetime import datetime, timedelta

def generate_transactions(n=500):
    np.random.seed(0)
    data=[]
    for i in range(n):
        txn_id=f"TXN{100000+i}"
        amount=round(np.random.uniform(5,500),2)
        currency='USD'
        date=(datetime(2024,1,1)+ timedelta(days=int(np.random.rand()*365))).strftime('%Y-%m-%d')
        status=np.random.choice(['completed','pending','failed'], p=[0.7,0.2,0.1])
        customer_id=f"CUST{np.random.randint(1000,9999)}"
        data.append({'txn_id':txn_id,'amount':amount,'currency':currency,'date':date,'status':status,'customer_id':customer_id})
    df=pd.DataFrame(data)
    os.makedirs('data',exist_ok=True)
    df.to_csv('data/transactions.csv',index=False)
    df.to_json('data/transactions.json',orient='records',lines=False)
    print('Generated transactions in data/')


if __name__=='__main__':
    generate_transactions()
