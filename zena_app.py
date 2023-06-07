import streamlit
import pandas
import requests
import snowflake.connector
streamlit.title('Zena Amazing Athleisure Catalog')
from urllib.error import URLError
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from zenas_athleisure_db.products.catalog_for_website;")
    return my_cur.fetchall()
my_data_row = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_row)
  
