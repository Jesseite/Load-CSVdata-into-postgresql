CREATE TABLE superstore.order
(
    order_id varchar(100),
    order_dt int,
    sales int,
    quantity int,
    discount int,
    profit int,
    customer_id varchar(100),
    product_id varchar(100),
    ship_id varchar(100),
    CONSTRAINT order_pkey PRIMARY KEY (order_id)
)