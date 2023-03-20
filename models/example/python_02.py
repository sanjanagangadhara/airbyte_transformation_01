import pandas as pd
import json
import ast


def transformation_function(row):
    result = ast.literal_eval(row)
    after_normalizing = pd.json_normalize(result)
    return after_normalizing

    
def model(dbt, session):

    df = dbt.ref("python_01").to_pandas()
    final_result=pd.DataFrame()
    df_series = df["data"]
    
    new_list = df_series.apply(transformation_function) 
    
    for item in new_list:
        final_result =  pd.concat([final_result, item])

    # y = [str(type(final_result))]
    # final_df = pd.DataFrame(y)
    final_df = final_result
    final_df.columns = final_df.columns.astype(str)

    return final_df