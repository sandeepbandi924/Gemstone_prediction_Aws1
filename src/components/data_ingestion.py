import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation

##Intialize the Data ingestion configuration

@dataclass
class DataIngestionConfig:
   train_data_path:str = os.path.join('artifacts','train.csv')
   test_data_path:str = os.path.join('artifacts','test.csv')
   raw_data_path:str = os.path.join('artifacts','raw.csv')

#create a class for data ingestion  
class DataIngestion:
   def __init__(self):
      self.ingestionconfig = DataIngestionConfig()

   def intiate_data_ingestion(self):
      logging.info('Data Ingestion method Starts')
      try:
         df = pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
         logging.info('Dataset read as pandas Dataframe')

         #go head and make my directory
         os.makedirs(os.path.dirname(self.ingestionconfig.raw_data_path),exist_ok=True)

         df.to_csv(self.ingestionconfig.raw_data_path,index=False)

         #we are reading traintestsplit and saving it
         logging.info('Train Test Split Initiated') 
         train_set , test_set = train_test_split(df , test_size=0.30,random_state=42)

         train_set.to_csv(self.ingestionconfig.train_data_path,index = False, header=True)
         test_set.to_csv(self.ingestionconfig.test_data_path,index=False,header=True)

         logging.info('Ingestion of data is completed')

         return (
            self.ingestionconfig.train_data_path,
            self.ingestionconfig.test_data_path
         )

      except Exception as e:
         logging.info('Exception occured at Data ingestion stage')
         raise CustomException(e,sys)
      

##Run data Ingestion

if __name__ == '__main__':
   obj = DataIngestion()
   train_data , test_data = obj.intiate_data_ingestion()
   data_transformation = DataTransformation()
   train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_path=train_data,test_path=test_data)

