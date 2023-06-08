import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('Zena Amazing Athleisure Catalog')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
