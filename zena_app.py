import streamlit
import pandas
import requests
import snowflake.connector
#from urllib.error import URLError
streamlit.title('Zena Amazing Athleisure Catalog')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from catalog_for_website")
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)
