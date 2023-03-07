import pandas as pd
import json

def model(dbt, session):

    dbt.config(
        materialized = "table",
        packages = ["pandas"]
    )

    df = dbt.ref("select_raw_table").to_pandas()

    




    final_df = pd.DataFrame(df["DATA"])

    return final_df