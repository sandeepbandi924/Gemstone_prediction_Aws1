# End to End ML project

## creating virtual environment
```
conda create -p venv python==3.8 
```

## created reqirements file
### install all neceesary libararies
```
pip install -r requirements.txt
```

## creating setup.py
```
convert project/folders into packages so that we can install into PYPI
it is over all package
```
## creating src folder
```
-> __init__.py is used for importing packages form one file to other
--> utils.py is generic functionality for entire project
--> exception and logging will always used for moduler coding
```



import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from src.utils import save_object

@dataclass
class DatatransformationConfig:
   preproccesor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
   def __init_(self):
      self.data_transformation_config = DatatransformationConfig()

   def get_data_transformation_object(self):
      '''
        This function is responsible for data transformation
        '''
      try:
         logging.info('Data Transformation intiated')

         # Define which columns should be ordinal-encoded and which should be scaled
         categorical_cols = ['cut', 'color','clarity']
         numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
         
         # Define the custom ranking for each ordinal variable
         cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
         color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
         clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
         
         logging.info('Pipeline intiated')
         # Numerical Pipeline
         num_pipeline = Pipeline(
            steps=[
               ('Imputer',SimpleImputer(strategy='median')),
               ('Scaling',StandardScaler())
            ]
         )

         #Categorical Pipeline
         cat_pipeline = Pipeline(
            steps=[
               ('imputer',SimpleImputer(strategy='most_frequent')),
               ('OrdinalEncoding',OrdinalEncoder(categories=[cut_categories,cut_categories,clarity_categories])),
               ('Scaling',StandardScaler())
            ]
         )

         logging.info(f'Categorical Columns: {categorical_cols}')
         logging.info(f'Numerical columns: {numerical_cols}')

         preprocessor = ColumnTransformer(
            [
               ('num_pipeline',num_pipeline,numerical_cols),
               ('cat_pipeline',cat_pipeline,categorical_cols)
            ]
         )
         logging.info('Pipeline completed')

         return preprocessor

      except Exception as e:
         logging.info('Exceprion occured in data transformation')
         raise CustomException(e,sys)
      
   def initiate_data_transformation(self,train_path,test_path):
      try:
         
         #reading train and test data
         train_df = pd.read_csv(train_path)
         test_df = pd.read_csv(test_path)

         logging.info('Reading train and test data completed')
         logging.info(f'Train DataFrame Head: \n {train_df.head().to_string()}')
         logging.info(f'Test DataFrame Head: \n {test_df.head().to_string()}')

         logging.info('Obtaining preprocessor object')

         preprocessor_obj = self.get_data_transformation_object()


         target_col_name = 'price'
         drop_column = [target_col_name , 'id']

         input_feature_train_df = train_df.drop(columns=drop_column, axis=1)
         target_feature_train_df = train_df[target_col_name]

         input_feature_test_df = test_df.drop(columns=drop_column, axis=1)
         target_feature_test_df = test_df[target_col_name]

         #Transforming using preprocessor obj
         input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
         input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

         logging.info('Applying preprocessing on training and testing datasets.')


         train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
         test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]


         save_object(
            file_path=self.data_transformation_cofig.preprocessor_obj_file_path,
            obj = preprocessor_obj
         )
         logging.info('Preprocessing pickle file saved')

         return(
            train_arr,
            test_arr,
            self.data_transformation_cofig.preprocessor_obj_file_path
         )

      except Exception as e:
         logging.info('Exception occured in initiate_data_transformation function')
         raise CustomException(e,sys)