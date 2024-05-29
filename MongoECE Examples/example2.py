from pymongo import MongoClient
#Σύνδεση στη βάση δεδομένων MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bookstore"]
collection = db["books"]
# Ανάκτηση εγγραφών με τον συγγραφέα "J.R.R. Tolkien"
query = {"author": "J.R.R. Tolkien"}
books = collection.find(query)
# Εμφάνιση του περιεχομένου των βιβλίων
for book in books:
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Pages:", book["pages"])
    print("Genre:", book["genre"])
    print("------------------------")
# Κλείσιμο της σύνδεσης με τη βάση δεδομένων
client.close()