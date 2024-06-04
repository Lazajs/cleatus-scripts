from firestore import fetch_data_from_firestore
from planetscale import select_data_ps

result = select_data_ps('SELECT * FROM Naics')
# fetch_data_from_firestore('users')

print(result)
