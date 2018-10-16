import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres")
# "dbname=tethys user=postgres passwd=postgres"
cur = conn.cursor()

init_query = """
CREATE TABLE products (
    product_no SERIAL PRIMARY KEY,
    name text,
    price numeric
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    product_no SERIAL REFERENCES products (product_no),
    quantity integer
);
"""
cur.execute(init_query)

cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("apple iphone", 1000))
cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("samsung s3", 300))
cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("ibm watson", 7000))
cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("MS", 5000))
cur.execute("SELECT * FROM products;")
res_rows = cur.fetchall()
print(res_rows)
valid_index = [w[0] for w in res_rows]

cur.execute("INSERT INTO orders (product_no, quantity) VALUES (%s, %s)", (valid_index[0], 5))
cur.execute("INSERT INTO orders (product_no, quantity) VALUES (%s, %s)", (valid_index[1], 10))
cur.execute("INSERT INTO orders (product_no, quantity) VALUES (%s, %s)", (valid_index[2], 0))
cur.execute("SELECT * FROM orders;")
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()
