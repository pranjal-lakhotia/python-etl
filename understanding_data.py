import pandas as pd
def main():
    fp = 'C:\\Users\\Pranjal Lakhotia\\Projects\\retail_db_json\\retail_db_json\\order_items\\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'
    df = pd.read_json(fp,lines=True)
    # print(df.columns)
    # print(df.count())
    #print(df.shape)
    print(df.describe())


if __name__ == '__main__':
    main()