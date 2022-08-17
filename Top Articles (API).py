#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'topArticles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER limit as parameter.
# base url for copy/paste:
# https://jsonmock.hackerrank.com/api/articles?page=<pageNumber>
#

def topArticles(limit):
    # Write your code here
    import requests
    import json
    url = "https://jsonmock.hackerrank.com/api/articles?page="
    
    response = requests.get(url)
    data = response.json()
    total_pages = data['total_pages']
    per_page = data['per_page']
    titles = []
    num_comments = []
    new_list = []
    
    
    for page in range(1, total_pages+1):
        content = requests.get("https://jsonmock.hackerrank.com/api/articles?page={}".format(page)).json()
        for data_pp in range(per_page):
            if content['data'][data_pp]['title'] != None:
                titles.append(content['data'][data_pp]['title'])
            elif content['data'][data_pp]['title'] == None and content['data'][data_pp]['story_title'] != None:
                titles.append(content['data'][data_pp]['story_title'])
            else:
                titles.append(None)
            num_comments.append(content['data'][data_pp]['num_comments'])
    nc_title = zip(num_comments,titles)
    nc_title = list(nc_title)
    nc_title.sort(reverse=True)
    for i in range(limit):
        new_list.append(nc_title[i][1])
    return new_list



        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    limit = int(input().strip())

    result = topArticles(limit)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
