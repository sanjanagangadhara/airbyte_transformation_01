import pandas as pd
import json


def model(dbt, session):

    dbt.config(
        materialized = "table",
        packages = ["pandas"]
    )
    df = dbt.ref("select_raw_table").to_pandas()
    new_list=[]
    for i in range (len(df["DATA"])):
        df_series = df.iloc[i]["DATA"]
        df_json = json.loads(df_series)
        
        for x in range (len(df_json)):
            new_list.append(str(df_json[x]))

    final_df = pd.DataFrame(new_list, columns=["data"])
    
    return final_df