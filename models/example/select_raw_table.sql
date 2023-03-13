with source as 

(    select * from {{ source('RAW_BLOB_DATA', 'FASTAPI') }}),

final_01 as 

(    select * from source)

select DATA from final_01 ORDER BY _AIRBYTE_EMITTED_AT  