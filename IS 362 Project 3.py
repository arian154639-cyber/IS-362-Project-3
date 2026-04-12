"""
The SQL code was mostly easy, though I had trouble with the exact order. I had some technical 
setup issues but got those fixed eventually. You are supposed to enter your password when 
running the script on your machine.
"""

import mysql.connector
import pandas as pd
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="chinook"
)

sql_script = """
SELECT
customer.LastName,
customer.FirstName,
track.Name,
album.Title
FROM customer
JOIN invoice ON customer.CustomerId = invoice.CustomerId
JOIN invoiceline ON invoice.InvoiceId = invoiceline.InvoiceId
JOIN track ON invoiceline.TrackId = track.TrackId
JOIN album ON track.AlbumId = album.AlbumId
ORDER BY customer.LastName; 
"""

dataframe_1 = pd.read_sql_query(sql_script, conn)
print(dataframe_1.head())
conn.close()