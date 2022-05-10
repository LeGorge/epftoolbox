"""
Simplified example for using the LEAR model for forecasting prices with daily recalibration
"""

# Author: Jesus Lago

# License: AGPL-3.0 License

# from epftoolbox.models import evaluate_lear_in_test_dataset
import os
from datetime import datetime
import sys
sys.path.append('../epftoolbox')
from epftoolbox.models import evaluate_lear_in_test_dataset

# Market under study. If it not one of the standard ones, the file name
# has to be provided, where the file has to be a csv file
dataset = 'BRA'

# Number of years (a year is 364 days) in the test dataset.
years_test = 1

# Number of days used in the training dataset for recalibration
calibration_window = 364 * 2

# Optional parameters for selecting the test dataset, if either of them is not provided, 
# the test dataset is built using the years_test parameter. They should either be one of
# the date formats existing in python or a string with the following format
# "%d/%m/%Y %H:%M"
begin_test_date = '13/01/2021'
end_test_date = '12/01/2022'
# begin_test_date = '25/12/2017'
# end_test_date = '24/12/2018'

path_datasets_folder = os.path.join('.', 'datasets')
path_recalibration_folder = os.path.join('.', 'experimental_files')

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
    
# evaluate_lear_in_test_dataset(path_recalibration_folder=path_recalibration_folder, 
#                              path_datasets_folder=path_datasets_folder, dataset=dataset, years_test=years_test, 
#                              calibration_window=calibration_window, begin_test_date=begin_test_date, 
#                              end_test_date=end_test_date, func_min_threshold=min_threshold,
#                              func_max_threshold=max_threshold)

evaluate_lear_in_test_dataset(path_recalibration_folder=path_recalibration_folder, 
                             path_datasets_folder=path_datasets_folder, dataset=dataset, years_test=years_test, 
                             calibration_window=calibration_window, begin_test_date=begin_test_date, 
                             end_test_date=end_test_date)