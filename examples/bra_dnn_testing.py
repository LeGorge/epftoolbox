
from unittest import mock
# import epftoolbox
# from epftoolbox import models
# from ../epftoolbox/models/evaluate import evaluate_dnn_in_test_dataset
from datetime import datetime
import os
import sys
sys.path.append('../epftoolbox')
from epftoolbox.models import evaluate_dnn_in_test_dataset

# Number of layers in DNN
nlayers = 2

# Market under study. If it not one of the standard ones, the file name
# has to be provided, where the file has to be a csv file
dataset = 'BRA'

# Number of years (a year is 364 days) in the test dataset.
years_test = 1

# Boolean that selects whether the validation and training datasets were shuffled when
# performing the hyperparameter optimization. Note that it does not select whether
# shuffling is used for recalibration as for recalibration the validation and the
# training datasets are always shuffled.
shuffle_train = 1

# Boolean that selects whether a data augmentation technique for DNNs is used
data_augmentation = 0

# Boolean that selects whether we start a new recalibration or we restart an existing one
new_recalibration = 1

# Number of years used in the training dataset for recalibration
calibration_window = 2

# Unique identifier to read the trials file of hyperparameter optimization
experiment_id = 3

# Optional parameters for selecting the test dataset, if either of them is not provided, 
# the test dataset is built using the years_test parameter. They should either be one of
# the date formats existing in python or a string with the following format
# "%d/%m/%Y %H:%M"
begin_test_date = '13/01/2021'
end_test_date = '12/01/2022'
# begin_test_date = '25/12/2017'
# end_test_date = '24/12/2018'

# Set up the paths for saving data (this are the defaults for the library)
path_datasets_folder = os.path.join('.', 'datasets')
path_recalibration_folder = os.path.join('.', 'experimental_files')
path_hyperparameter_folder = os.path.join('.', 'experimental_files')

def parse_date(string_date):
  return datetime.strptime(string_date, '%d/%m/%Y')

# Functions to retrieve min threshold for a specific date
def min_threshold(date):
  if parse_date('01/01/2021') <= date <= parse_date('31/12/2021'):
    return 49.77
  if parse_date('01/01/2022') <= date <= parse_date('31/12/2022'):
    return 55.70
  return 0

def max_threshold(date):
  if parse_date('01/01/2021') <= date <= parse_date('31/12/2021'):
    return 583.88
  if parse_date('01/01/2022') <= date <= parse_date('31/12/2022'):
    return 646.58
  return sys.float_info.max

# evaluate_dnn_in_test_dataset(experiment_id, path_hyperparameter_folder=path_hyperparameter_folder, 
#                                path_datasets_folder=path_datasets_folder, shuffle_train=shuffle_train, 
#                                path_recalibration_folder=path_recalibration_folder, 
#                                nlayers=nlayers, dataset=dataset, years_test=years_test, 
#                                data_augmentation=data_augmentation, calibration_window=calibration_window, 
#                                new_recalibration=new_recalibration, begin_test_date=begin_test_date, 
#                                end_test_date=end_test_date, func_min_threshold=min_threshold,
#                                func_max_threshold=max_threshold)

evaluate_dnn_in_test_dataset(experiment_id, path_hyperparameter_folder=path_hyperparameter_folder, 
                               path_datasets_folder=path_datasets_folder, shuffle_train=shuffle_train, 
                               path_recalibration_folder=path_recalibration_folder, 
                               nlayers=nlayers, dataset=dataset, years_test=years_test, 
                               data_augmentation=data_augmentation, calibration_window=calibration_window, 
                               new_recalibration=new_recalibration, begin_test_date=begin_test_date, 
                               end_test_date=end_test_date)