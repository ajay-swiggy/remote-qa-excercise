
import logging
import requests
from config.local import *
from endpoints.endpoints import *
logging = logging.getLogger(__name__)

class GetPointsHelper():
    ids = []
    points=[]
    dupe = 0
     
    def get_top_points():
        url = baseurl + getUsersWithMaxPointsEndpoint
        logging.info('Calling "' + url + '"')
        return requests.get(url)
             
    def check_dupe(dict):
        for x in dict:
            if(x['id'] not in GetPointsHelper.ids):
                GetPointsHelper.ids.append(x['id'])        
            else:
                GetPointsHelper.dupe += 1    
                
            if(x['points'] not in GetPointsHelper.points):
                GetPointsHelper.points.append(x['points'])        
            else:
                GetPointsHelper.dupe += 1                       
        return GetPointsHelper.dupe