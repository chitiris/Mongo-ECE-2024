from pymongo import MongoClient

# Σύνδεση στη βάση δεδομένων MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bookstore"] # Όνομα Βάσης 
collection = db["books"]  #Όνομα Collection
# Ανάκτηση όλων των εγγραφών από τη συλλογή "books"
books = collection.find()
# Εμφάνιση του περιεχομένου των βιβλίων
for book in books:
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Pages:", book["pages"])
    print("Genre:", book["genre"])
    print("------------------------")
# Κλείσιμο της σύνδεσης με τη βάση δεδομένων
client.close()
