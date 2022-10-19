import pandas
from pandas.io import gbq
from google.cloud import bigquery
import os


def getFlightJson():

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Keys\uploaddataframe_privatekey.json"

    client = bigquery.Client()
    table_id = 'uploaddataframe.DataSet_test.Teste'


    project = "uploaddataframe"
    dataset_id = "DataSet_test"

    dataset_ref = bigquery.DatasetReference(project, dataset_id)
    table_ref = dataset_ref.table("Teste")
    table = client.get_table(table_ref)

    # Retrieves top views from each streamer on that day
    sql = """
        SELECT *
        FROM `uploaddataframe.DataSet_test.Teste` 
    """


    df = client.query(sql).to_dataframe()
    df.iloc[:,0]= df.iloc[:,0].replace({'â':'a','á':'a','Á':'A','ç':'c','é':'e','ó':'o','ô':'o'}, regex=True)
    #return df.to_json(orient='records', lines=True)
    return df.to_dict('records')