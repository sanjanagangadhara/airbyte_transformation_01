import pandas as pd
import json


def model(dbt, session):

    df = dbt.ref("select_raw_table").to_pandas()

    




    final_df = df["DATA"]

    return final_df