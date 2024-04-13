import pandas as pd
import psycopg2

# import dataset from CSV
df = pd.read_csv(r"C:\Users\Astto\Documents\project\Superstore.csv")

# convert the Postal Code column to integer
df = df.fillna(7)
df["Postal Code"] = df["Postal Code"].astype(int)

# customer columns to import
columns = ['Customer ID', 'Customer Name', 'Segment', 'Country/Region', 'City', 'State', 'Postal Code', 'Region']

df_selected_columns = df[columns]

# convert records into list
data_to_list = df_selected_columns.values.tolist()

print(df_selected_columns)
print(data_to_list)

# set up postgresql Connection
host ='<your host>'
user ='<your user>'
password ='<your password>'
database ='<your database>'

def connection_db(host, user, password, database):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

# set up DB connection object
try:
    c = connection_db(host, user, password, database)
except psycopg2.Error as err:
    print("Something went wrong: {}".format(err))

    
#Insert data into Customer table
insert = '''
    INSERT INTO superstore.customer
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
'''

# set up cursor connection
try:
    cursor = c.cursor()
    for data in data_to_list:
        # ensure all data are in string format
        data = [str(item) for item in data]
        cursor.execute(insert, data)
    c.commit()
    print('Successful')
except Exception as e:
    print(e)
