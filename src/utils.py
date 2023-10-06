import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

def save_object(file_path , obj):
   try:
      dir_path = os.path.dirname(file_path)

      os.makedirs(dir_path,exist_ok=True)

      with open(file_path,'wb') as file_obj:
         pickle.dump(obj, file_obj)

   except Exception as e:
      raise CustomException(e,sys)
   

#   #Raeding train data and test data
#          train_df = pd.read_csv(train_path)
#          test_df = pd.read_csv(test_path)

#          logging.info('Reading train and test data completed')
#          logging.info(f'Train DataFrame Head {train_df.head().to_string()}')
#          logging.info(f'Test DataFrame Head {test_df.head().to_string()}')

#          logging.info('Obtaining preprocessing object')
#          preprocessor_obj = self.get_data_transformation_object()

#          target_column_name = 'price'
#          drop_columns = [target_column_name,'id']

#          input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
#          target_feature_train_df = train_df[target_column_name]

#          input_feature_test_df = test_df.drop(columns=drop_columns,axis=1)
#          target_feature_test_df = test_df[target_column_name]

#          logging.info('Applying preprocessing object on training and testing datasets')

#          input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
#          input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

#          #concate

#          train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
#          test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]


#          save_object(
#             file_path=self.data_transformation_config.preproccesor_obj_file_path,
#             obj = preprocessor_obj
#          )
#          logging.info('Preprocessor pickle file saved')


#          return(
#             train_arr,
#             test_arr,
#             self.data_transformation_config.preproccesor_obj_file
 