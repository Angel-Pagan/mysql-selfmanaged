from click import open_file
from sqlalchemy import create_engine
import pandas as pd

""" assigning .env files to variables """
host_name = open('.login/host.env')
host = host_name.read()

user_name = open('.login/user.env')
user = user_name.read()

password = open('.login/password.env')
pw = password.read()


""" Login Credintials for mySQL """
MYSQL_HOSTNAME = host 
MYSQL_USER = user
MYSQL_PASSWORD = pw
MYSQL_DATABASE = 'db1'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string

db = create_engine(connection_string)

df = pd.read_sql(query, con=db)

""" Importing a csv file into DATABASE db1"""

facebook_fact_check = pd.read_csv('https://raw.githubusercontent.com/gsantia/BuzzFace/master/facebook-fact-check.csv')
facebook_fact_check #View DataSet

real_df.to_sql('FB_Fact_Check_TABLE', con=db, if_exists='replace') #Uploading DATASET Into mySQL and creating a table called FB_Fact_Check_TABLE