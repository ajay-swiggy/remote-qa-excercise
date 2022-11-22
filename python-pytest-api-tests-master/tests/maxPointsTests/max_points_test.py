import logging
import json
import time
import calendar
from datetime import datetime
from helper.GetPointsHelper import GetPointsHelper
logging = logging.getLogger(__name__)

class TestPoints(GetPointsHelper):

 
     def test_points_randomness(self):
          repetetive_count=0
          logging.info("Calling the API 4 times to verify if the id or points are not repeated multiple times")
          for x in range(1,5) :
               reponse = GetPointsHelper.get_top_points()
               dict = json.loads(reponse.text)['users']                         
               repetetive_count = GetPointsHelper.check_dupe(dict)
               logging.info(dict)
               if(x<=4) :
                    logging.info("Waiting 60 seconds for the points to be updated") 
                    time.sleep(60)   
                    
          logging.info("The total number of repetitive instances of id or points is :" + str(repetetive_count)) 
          logging.info("Verifying if the total instance of duplicate id or points is Less Than 3 ")                             
          assert repetetive_count <= 2, 'Id/Points seems to be repeated too frequently'
          
     def test_timestamp_update(self):
          GetPointsHelper.get_top_points()
          reponse = GetPointsHelper.get_top_points()
          latest_timestamp = json.loads(reponse.text)['timestamp']
          date_time_pattern = '%Y-%m-%dT%H:%M:%S.%f'
          latest_timestamp_in_epoch = int(calendar.timegm(time.strptime(latest_timestamp, date_time_pattern)))
          current_time_in_epoch = int(time.time())
          logging.info("Verifying if the timestamp of the last request is updated")                             
          assert (current_time_in_epoch - latest_timestamp_in_epoch) <=1, "Timestamp of the last request is not updated"
         
     
     def test_response_and_status_code(self):
          reponse = GetPointsHelper.get_top_points()
          logging.info("Status Code : " + str(reponse.status_code))
          logging.info("Response : " + reponse.text)
          
          logging.info("Verifying if the Http Response Status code is 200")                             
          assert reponse.status_code is 200, 'Http Response Status code is not 200'
          
          reponse_body = json.loads(reponse.text)      
              
          logging.info("Verifying if exactly two users are returned in the response")                             
          assert len(reponse_body['users']) == 2,'The number of users returned is not two'
          
          logging.info("Verifying if id is not repeated")                             
          assert reponse_body['users'][0]['id'] != reponse_body['users'][1]['id'] , 'Ids are repeated'
          
          logging.info("Verifying if the points is within the range") 
          assert reponse_body['users'][0]['points'] in range(1,101) and reponse_body['users'][1]['points'] in range(1,101), 'Points is not within the range of 1-100'
         