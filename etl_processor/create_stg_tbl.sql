CREATE TABLE etl.ws_opendata_nyc_tlc_fhv_ps
(
    data_source_id                          INT
    ,processing_date                        DATE
    ,license_number                         VARCHAR(4000)
    ,name                                   VARCHAR(4000)
    ,driver_type                            VARCHAR(4000)
    ,expiration_date                        VARCHAR(4000)
    ,accessibility_trained                  VARCHAR(4000)
    ,last_date_updated                      VARCHAR(4000)
    ,last_time_updated                      VARCHAR(4000)
    ,etl_insert_date                        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ,etl_update_date                        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
