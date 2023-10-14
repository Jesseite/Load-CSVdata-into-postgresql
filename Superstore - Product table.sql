CREATE TABLE superstore.product
(
    product_id varchar(100),
    category varchar(100),
    sub_category varchar(100),
    product_name varchar(400),
    CONSTRAINT product_pkey PRIMARY KEY (product_id)
)