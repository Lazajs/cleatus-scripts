import MySQLdb
from uuid import uuid4
from settings import PS_HOST, PS_USER, PS_PASSWORD, PS_DATABASE

# MAIN branch at planetscale conn
conn = MySQLdb.connect(
    host=PS_HOST,
    user=PS_USER,
    password=PS_PASSWORD,
    database=PS_DATABASE,
    autocommit=True,
    ssl_mode="VERIFY_IDENTITY",
    ssl={"ca": "./ca-certificates.pem"}
)


def select_data_ps(query):
    # Establish connection to the database
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        tables = cursor.fetchall()

        return tables
    except MySQLdb.Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
