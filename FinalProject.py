import unittest
import itertools
import collections
import json
import sqlite3
import facebook
import fb_info
import requests
import datetime
import calendar
import csv
from pprint import pprint

CACHE_FNAME = "finalproject.json"

try:
    cache_file = open(CACHE_FNAME,'r')# Attempt to read  data from the file
    cache_contents = cache_file.read()# If it's there, get it into a string format to read
    cache_file.close()# The data is in a dict and can thus be closed
    CACHE_DICTION = json.loads(cache_contents)# Load said data into a dictionary
except:
    CACHE_DICTION = {}

facebook_access_token = fb_info.facebook_access_token
facebook_user_id = fb_info.facebook_user_id

def get_FB_info(my_access_token):
    my_graph = facebook.GraphAPI(access_token = my_access_token, version='2.1')
    my_results = my_graph.request('me?fields=feed{comments.limit(100),created_time}')
    user_id = my_results['id']
    if user_id in CACHE_DICTION:
        print ('using cached data')
        returned_data = CACHE_DICTION[user_id]
    else:
        print ('fetching data')
        my_data = my_results['feed']['data']
        returned_data = {}
        for post in my_data:
            count = 0
            if 'comments' in post.keys():
                for comment in post['comments']['data']:
                    count += 1
            year = post["created_time"][:4]
            month = post["created_time"][5:7]
            day = post["created_time"][8:10]
            my_weekday_tuple = (year, month, day)
            weekday = datetime.datetime(int(year), int(month), int(day))
            day_of_week = weekday.weekday()
            
            if day_of_week == 0:
                weekday ="Monday"
            elif day_of_week == 1:
                weekday ="Tuesday"
            elif day_of_week == 2:
                weekday ="Wednesday"
            elif day_of_week == 3:
                weekday ="Thursday"
            elif day_of_week == 4:
                weekday ="Friday"
            elif day_of_week == 5:
                weekday ="Saturday"
            elif day_of_week == 6:
                weekday = "Sunday"
            returned_data[post['id']] = (count, weekday)

        CACHE_DICTION[user_id] = my_results
        my_file = open(CACHE_FNAME, 'w')
        my_file.write(json.dumps(CACHE_DICTION))
        my_file.close()
    return returned_data


pprint(get_FB_info(fb_info.facebook_access_token))


#print (json.dumps(my_feed, indent=4))