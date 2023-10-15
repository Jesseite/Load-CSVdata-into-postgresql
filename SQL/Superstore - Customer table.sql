CREATE TABLE superstore.customer
(
    customer_id varchar(100),
    customer_name varchar(100),
    segment varchar(100),
    country varchar(100),
    city varchar(100),
    state varchar(100),
    postal_code int,
    region varchar(100),
    CONSTRAINT customer_pkey PRIMARY KEY (customer_id)
)
