import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
cred = credentials.Certificate(r"C:\Users\hbhan\StudioProjects\Coding\AppDev\rasberryfire\serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'users').document(u'harsh')
doc_ref.set({
    'first': u'Harsh',
    u'last': u'Bhansali',
    u'born': 2003
})
print("Finished")
