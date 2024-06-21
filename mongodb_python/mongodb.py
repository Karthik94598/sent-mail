import pymongo
myClient = pymongo.MongoClient("mongodb://localhost:27017")  # connecting to mongodb
db = myClient["employee"]  # creating object for database , here database name is "employee"
st =myClient["students"]   #  creating object for another database , here database name is "student"

fe=db["frontend"] # creating object for collection in employee database , here collection name is "frontend"
be=db["backend"]  # creating object for another collection in employee database , here collection name is "backend"
analy=db["analyst"] # creating object for another collection in employee database , here collection name is "analyst"

ten=st["tenth"] # creating object for  collection in student database , here collection name is "tenth"
nin=st["ninth"] # creating object for another collection in student database , here collection name is "ninth"

fe.delete_many({}) # deleting all documents in frontend collection why becuz when we are running multiple times it is inserting multiple times
ten.delete_many({}) # deleting all documents in tenth collection

# create in crud operation.
y=fe.insert_many([
    {"name" : "karthik", "age" : 21 , "skill": "react js"}, 
    {"name" : "lalith", "age" : 27 , "skill": "vue js"}, 
    {"name" : "karthik", "age" : 21 , "skill": "react js"}, 
    {"name" : "giridhar", "age" : 78 , "skill": "react js"},
    {"name" : "sai", "age" : 68 , "skill": "react"},
    {"name" : "charan", "age" : 88 , "skill": "react js"},
    {"name" : "murthy", "age" : 58 , "skill": "react"},
    {"name" : "ramana", "age" : 28 , "skill": "react js"},
    {"name" : "kuldeep", "age" : 98 , "skill": "react js"},
    {"name" : "raju", "age" : 178 , "skill": "react"},
    ]) # inserting documents in frontend collection

x=ten.insert_many([
    {"name": "sai", "cgpa":9.8 , "city": "vishakapatnam"},
    {"name": "charan", "cgpa":7.0 , "city": "vizag"},
    {"name": "balu", "cgpa":8.9 , "city": "sklm"},
    {"name": "sai", "cgpa":9.8 , "city": "vishakapatnam"}
]) # inserting documents in tenth collection

emlist = db.list_collection_names()
if "frontend" in emlist:
    print("frontend collection existed in this database") # to check the a collection in database

print(myClient.list_database_names()) # to show all database in server
print(db.list_collection_names()) # to show all collection names in database
print(st.list_collection_names())
print(y.inserted_ids) # to print id of all documents in a collection.
print(x.inserted_ids)

# read in crud operation
print(fe.find_one()) # to get access of first element in the collection
print(fe.find_one({"name" : "lalith"})) # to get access of first element in the collection which satisfys the condition
for doc in fe.find({"name" : "karthik"}):
    print(doc) # to get access of all documents in the collection  which satisfys the condition
for doc in fe.find():
    print(doc) # to get access of all documents in the collection 

#query , queries are used to filtter the data

mq = {"age" : {"$gt" :50 , "$lt":100}}
result = fe.find(mq)
for mydoc in result:
    print(mydoc)     # filtering the data greater than 50 and less than 100
mq ={"age": {"$gt" : 50} , "skill":"react js"}
result1 = fe.find(mq)
for mydoc1 in result1:
    print(mydoc1)  # filtering the data by age greater than 50 and skill equal to react js
if result == result1:
    print("they are same")
else:
    print('they are not same')    # comparing the data
mq = {"name" : {"$regex" : "^r"} , "skill" :{ "$regex" : "js"}} # here we are using regex operator "^" this will check whether it will start with it or nor otherswise it will check the substring is in the field or not.
result2 = fe.find(mq)
for mydoc2 in result2:
    print(mydoc2)
mq = {"$or":[{"name" : {"$regex" : "^r"}} , {"skill" :{ "$regex" : "js"}}]} # here we are using or operator with regex operator.
result3 = fe.find(mq)
for mydoc3 in result3:
    print(mydoc3)
#sort
so=fe.find().sort("name") # sorting in alphabet order
for i in so:
    print(i)
so=fe.find().sort("name" ,-1) # descending order sorting
for i in so:
    print(i)

# delete operation in crud 
mq = {"skill":"vue js"}
fe.delete_one(mq) # delete one in the collection
for x in fe.find():
    print(x)
mq = {"skill":"react"}
fe.delete_many(mq) # delete all documnents in the collection which satisfies the condition.
for x in fe.find():
    print(x)
fe.delete_many({}) # delete all documnents in the collection.
for x in fe.find():
    print(x)
nin.insert_many([
    {"name": "sai", "cgpa":9.8 , "city": "vishakapatnam"},
    {"name": "charan", "cgpa":7.0 , "city": "vizag"},
    {"name": "balu", "cgpa":8.9 , "city": "sklm"},
    {"name": "sai", "cgpa":9.8 , "city": "vishakapatnam"}
]) # inserting documents in nin collection
ten.drop() # it will delete the ten collection
print(st.list_collection_names())
myClient.drop_database('employee')  # it will delete the employee database
print(myClient.list_database_names())
#update operation in crud operation
mq={"name":"karthik"}
nv ={"$set":{"email":"krthik@gmail.com"}}
fe.update_one(mq,nv) # update one field which satisfy the conditiom
print(fe.find_one({"name":"karthik"}))
mq={}
nv={"$set":{"adress":"India"}}
fe.update_many(mq,nv) # update a field in every document
for x in fe.find():
    print(x)
mq={"name":"karthik"}
nv ={"$unset":{"email":"krthik@gmail.com"}} # using unset operation
fe.update_one(mq,nv)# it is using to delete a field which satisfy the topics
print(fe.find_one({"name":"karthik"}))

mr = fe.find().limit(5) # it will give only limited documents that you mentioned as output
for x in mr:
    print(x)
print(fe.count_documents({})) # it gives the count of no.of documents in a collection.
