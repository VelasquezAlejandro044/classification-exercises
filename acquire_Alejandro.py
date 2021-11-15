#imports
import pandas as pd
import numpy as np
import os
import seaborn as sns
from env import host, user, password

######## Connect to DB ################

# Let's make a function that takes in a database name as a string
# this function also performs our imports from env
def get_db_url(db_name):
    from env import user, host, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

sql = """
    SELECT * FROM passengers
"""

# Called the "Connection string" b/c it has all the info to connect
url = get_db_url("titanic_db")
df = pd.read_sql(sql, url)
df

#Fet URL for database function
def get_db_url(db_name):
    from env import user, host, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

# 1. Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame. Obtain your data from the Codeup Data Science Database.


def get_titanic_data():
       
    import pandas as pd
    from env import host, user, password
    sql = "SELECT * FROM passengers"
    url = get_db_url("titanic_db")
    df_titanic = pd.read_sql(sql, url)
    
    # info about data 
    print("You have uploaded the Titanic database successfully as df_titanic!")
    print()
    print(df_titanic.info())
    return df_titanic.head()

# 2. Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. The returned data frame should include the actual name of the species in addition to the species_ids. Obtain your data from the Codeup Data Science Database.

def get_iris_data():
       
    import pandas as pd
    from env import host, user, password
    sql = """
    SELECT * 
    FROM measurements m
    INNER JOIN species s ON m.species_id = s.species_id
    """
    if os.path.isfile('iris_df.csv'):
        df_iris = pd.read_csv('iris_df.csv', infex_col=0)
        print("You have uploaded the iris database successfully as df_iris!")
        print()
        print(df_iris.info())
        return df_iris.head()
    else:
        url = get_db_url("iris_db")
        df_iris = pd.read_sql(sql, url)
        print("You have uploaded the iris database successfully as df_iris!")
        print()
        print(df_iris.info())
        return df_iris.head()x

# 3. Make a function named get_telco_data that returns the data from the telco_churn database in SQL. In your SQL, be sure to join all 4 tables together, so that the resulting dataframe contains all the contract, payment, and internet service options. Obtain your data from the Codeup Data Science Database.

def get_telco_data():
       
    import pandas as pd
    from env import host, user, password
    sql = """
    SELECT * 
    FROM  customers c
    INNER JOIN internet_service_types ist ON c.`internet_service_type_id` = ist.`internet_service_type_id`
    JOIN contract_types ct ON c.`contract_type_id` = ct.`contract_type_id`
    JOIN payment_types pay ON c.`payment_type_id` = pay.payment_type_id
    """
    if os.path.isfile('telco.csv'):
        df_telco_churn = pd.read_csv('telco.csv', infex_col=0)
    else:
        url = get_db_url("telco_churn")
        df_telco_churn = pd.read_sql(sql, url)
    print("You have uploaded telco_churn database successfully as df_telco_churn!")
    print()
    print(df_telco_churn.info())
    return df_telco_churn.head().T

