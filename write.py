'''program to read data from json files '''

def load_db_table(df, conn, table_name, key):
    min_key = df[key].min()
    max_key = df[key].max()
    df.to_sql(table_name, conn, if_exists='append', index=False)
    print(f'Loaded data for {table_name} with in the range of {min_key} and {max_key}')


if __name__ == '__main__':
    import pandas as pd
    import os
    BASE_DIR = os.environ.get(BASE_DIR)
    TABLE_NAME = os.environ.get(TABLE_NAME)
    fp = f'{BASE_DIR}/{TABLE_NAME}'
    data = os.environ.get(fp)
    df = pd.DataFrame(data)
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'

    load_db_table(df, conn, 'users', 'user_id')
