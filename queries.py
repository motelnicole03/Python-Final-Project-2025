from db import get_connection

# -- THIS IS ALL FOR DATABASE FUNCTIONS --

# ---------- SELECT ALL ----------
def get_all_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ---------- INSERT ----------
def insert_product(p):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products(name, brand, category, eco_rating, price, eco_friendly)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (p["name"], p["brand"], p["category"], p["eco_rating"], p["price"], p["eco_friendly"]))
    conn.commit()
    conn.close()

# ---------- UPDATE ----------
def update_product(p, pid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE products SET
            name=%s, brand=%s, category=%s,
            eco_rating=%s, price=%s, eco_friendly=%s
        WHERE id=%s
    """, (p["name"], p["brand"], p["category"], p["eco_rating"], p["price"], p["eco_friendly"], pid))
    conn.commit()
    conn.close()

# ---------- DELETE ----------
def delete_product(pid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (pid,))
    conn.commit()
    conn.close()
