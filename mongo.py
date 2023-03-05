from pymongo import MongoClient
import urllib


database_user = urllib.parse.quote_plus('plgadmin1')
database_pass = urllib.parse.quote_plus('plg@2o2o&*(')

mongo_connection = MongoClient(r'mongodb://' + database_user + ':' + database_pass +'@34.251.243.79/?authMechanism=SCRAM-SHA-1&authSource=admin&retryWrites=true&w=majority')
db = mongo_connection['plg1']
cl = db['test2']


cl.insert_many([{"name":"arun","gender":"male"},{"name":"vijay","gender":"male"},{"name":"vignesh","gender":"male"}])

# db.getCollection("test2").find({'name':{$in:['vignesh','arun']}})
# print(cl.find({'name':{$in:['vignesh','arun']}}))


# print

# for x in (cl.find(
#     { 'name': { '$in': ['arun', 'vignesh'] }, 'gender': { '$in': ['male'] } },
#     )):
#     print(x) 

print((cl.find(
    {},
    )).count())

for x in (cl.find(
    {},
    )):
    print(x) 




# result = cl.find({"name":"arun","name":"vick"})

# for i in result:
#     print(i)

# cl.find({})