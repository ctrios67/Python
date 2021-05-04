CREATE TABLE dev_etl.etl_data_source_tracker
(
    data_source_id                          VARCHAR(4000)
    ,etl_processing_id                      VARCHAR2(4000)
    ,processing_date                        DATE
    ,data_source_name                       VARCHAR2(4000)
    ,data_source_raw_table                  VARCHAR2(4000)
    ,data_source_stg_table                  VARCHAR2(4000)
    ,data_source_rpt_table                  VARCHAR2(4000)
    ,data_source_collection_status          VARCHAR2(4000)
    ,data_source_raw_etl_status             VARCHAR2(4000)
    ,data_source_stg_etl_status             VARCHAR2(4000)
    ,data_source_rpt_etl_status             VARCHAR2(4000)
    ,record_insert_date                     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ,record_update_date                     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ,record_last_update_date                TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
