CREATE TABLE etl.wi_opendata_nyc_tlc_fhv_ps
(
    data_source_id                          INT
    ,processing_date                        DATE
    ,license_number                         VARCHAR(4000)
    ,name                                   VARCHAR(4000)
    ,driver_type                            VARCHAR(4000)
    ,expiration_date                        DATE
    ,accessibility_trained                  VARCHAR(4000)
    ,last_date_updated                      DATE
    ,last_time_updated                      TIME
    ,etl_insert_date                        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ,etl_update_date                        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
