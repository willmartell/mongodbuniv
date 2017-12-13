import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

def find():

    db=connection.test
    db2=connection.test
    db3=connection.test
    images= db.images
    images_remove= db3.images
    albums = db2.albums
    print "find(), reporting for duty"


    query = {}

    try:
        cursor = images.find(query) 

    except Exception as e:
        print "Unexpected error:", type(e), e

    limit = 99999999999
    i = 0
    for doc in cursor:
        if(i > limit):
            break
        image_id = doc['_id']

        try:
            cursor2 = albums.find({'images':image_id})
        except Exception as e:
            print "eeror:",type(e),e

        if(cursor2.count() == 0):
            #remove
            cursor3 = images_remove.remove({'_id':image_id},{'justOne':True})
            for doc4 in cursor3:
                print 'image id:',image_id,' removed'
            pass
        else:
            for doc2 in cursor2:
                print 'image id:',image_id,' is found in ',doc2['_id']

        #print image_id
        i = i + 1




find()
