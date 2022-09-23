import pandas as pd
import os
def read_data(base_dir,table_name):
    file_name = os.listdir(f'{base_dir}{table_name}')[0]
    fp = f'{base_dir}{table_name}{file_name}'
    df = pd.read_json(fp,lines=True)
    print(df.count())




if __name__ == "__main__":
    base_dir = 'C:\\Users\\Pranjal Lakhotia\\Projects\\retail_db_json\\retail_db_json\\'
    table_name = 'order_items\\'
    read_data(base_dir,table_name)
