import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate(
    "cleatus-fbbd2-firebase-adminsdk-1f5lo-d212a489c0.json")

fb = firebase_admin.initialize_app(
    cred, {
        'databaseURL': 'https://cleatus-fbbd2.firebaseio.com',
        'storageBucket': 'cleatus-fbbd2.appspot.com'
    })

db = firestore.client()


def fetch_data_from_firestore(collection_name):
    try:
        collection_ref = db.collection(collection_name)

        docs = collection_ref.stream()

        result = []
        for doc in docs:
            result.append(doc.to_dict())

        return result
    except Exception as e:
        print(f"An error occurred: {e}")
