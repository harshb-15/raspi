import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
cred = credentials.Certificate(
    r"C:\Users\hbhan\StudioProjects\Coding\AppDev\rasberryfire\serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(f'Received document snapshot: {doc.to_dict()["first"]}')

doc_ref = db.collection(u'users').document(u'harsh')
doc_watch = doc_ref.on_snapshot(on_snapshot)
while 2>1:
    continue
