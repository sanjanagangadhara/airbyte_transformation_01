with source as 

(    select * from {{ source('RAW_BLOB_DATA', 'FASTAPI') }}),

final_01 as 

(    select * from source)

select * from final_01