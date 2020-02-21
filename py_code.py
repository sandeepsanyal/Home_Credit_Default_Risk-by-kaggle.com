# importing modules
import numpy as np
import pandas as pd
import statsmodels
import statsmodels.discrete.discrete_model as sm
import sys

# importing user defined functions
sys.path.insert(0, "/Users/sandeepsanyal/PycharmProjects/tools/Python")
from missing_values import check_missing_values

# folder path
directory = r"/Users/sandeepsanyal/OneDrive/Github/Home_Credit_Default_Risk-by-kaggle.com"

# Importing application_train.csv
application_train = pd.read_csv(
    filepath_or_buffer = directory+r"/raw_datasets/application_train.csv",
    sep=',',
    encoding='latin-1'
)
bureau = pd.read_csv(
    filepath_or_buffer = directory+r"/raw_datasets/bureau.csv",
    sep=',',
    encoding='latin-1'
)
bureau_balance = pd.read_csv(
    filepath_or_buffer = directory+r"/raw_datasets/bureau_balance.csv",
    sep=',',
    encoding='latin-1'
)
credit_card_balance = pd.read_csv(
    filepath_or_buffer = directory+r"/raw_datasets/credit_card_balance.csv",
    sep=',',
    encoding='latin-1'
)
installments_payments = pd.read_csv(
    filepath_or_buffer = directory+r"/raw_datasets/installments_payments.csv",
    sep=',',
    encoding='latin-1'
)
POS_CASH_balance = pd.read_csv(
    filepath_or_buffer = directory+r"/raw_datasets/POS_CASH_balance.csv",
    sep=',',
    encoding='latin-1'
)
previous_application = pd.read_csv(
    filepath_or_buffer = directory+r"/raw_datasets/previous_application.csv",
    sep=',',
    encoding='latin-1'
)

# EDA
ids = ["SK_ID_CURR"]
dep_var = "TARGET"
numeric_vars = [
    "AMT_CREDIT"
    # ,"CNT_CHILDREN"
    # ,"AMT_INCOME_TOTAL"
    ,"AMT_ANNUITY"
    # ,"REGION_POPULATION_RELATIVE"
    # ,"DAYS_BIRTH"
    ,"DAYS_EMPLOYED"
    ,"DAYS_REGISTRATION"
    # ,"DAYS_ID_PUBLISH"
    # ,"OWN_CAR_AGE"
    # ,"EXT_SOURCE_1"
    ,"EXT_SOURCE_2"
    # ,"EXT_SOURCE_3"
    # ,"APARTMENTS_AVG"
    # ,"BASEMENTAREA_AVG"
    # ,"YEARS_BEGINEXPLUATATION_AVG"
    # ,"YEARS_BUILD_AVG"
    # ,"COMMONAREA_AVG"
    # ,"ELEVATORS_AVG"
    # ,"ENTRANCES_AVG"
    # ,"FLOORSMAX_AVG"
    # ,"FLOORSMIN_AVG"
    # ,"LANDAREA_AVG"
    # ,"LIVINGAPARTMENTS_AVG"
    # ,"LIVINGAREA_AVG"
    # ,"NONLIVINGAPARTMENTS_AVG"
    # ,"NONLIVINGAREA_AVG"
    # ,"OBS_30_CNT_SOCIAL_CIRCLE"
    # ,"DEF_30_CNT_SOCIAL_CIRCLE"
    # ,"OBS_60_CNT_SOCIAL_CIRCLE"
    # ,"DEF_60_CNT_SOCIAL_CIRCLE"
    # ,"DAYS_LAST_PHONE_CHANGE"
    # ,"AMT_REQ_CREDIT_BUREAU_HOUR"
    # ,"AMT_REQ_CREDIT_BUREAU_DAY"
    # ,"AMT_REQ_CREDIT_BUREAU_WEEK"
    # ,"AMT_REQ_CREDIT_BUREAU_MON"
    # ,"AMT_REQ_CREDIT_BUREAU_QRT"
    # ,"AMT_REQ_CREDIT_BUREAU_YEAR"
]
cat_vars = [
    "NAME_CONTRACT_TYPE"
    ,"CODE_GENDER"
    ,"FLAG_OWN_CAR"
    ,"FLAG_OWN_REALTY"
    ,"AMT_GOODS_PRICE"
    ,"NAME_TYPE_SUITE"
    ,"NAME_INCOME_TYPE"
    ,"NAME_EDUCATION_TYPE"
    ,"NAME_FAMILY_STATUS"
    ,"NAME_HOUSING_TYPE"
    ,"FLAG_MOBIL"
    ,"FLAG_EMP_PHONE"
    ,"FLAG_WORK_PHONE"
    ,"FLAG_CONT_MOBILE"
    ,"FLAG_PHONE"
    ,"FLAG_EMAIL"
    # ,"OCCUPATION_TYPE"
    ,"CNT_FAM_MEMBERS"
    ,"REGION_RATING_CLIENT"
    ,"REGION_RATING_CLIENT_W_CITY"
    # ,"WEEKDAY_APPR_PROCESS_START"
    # ,"HOUR_APPR_PROCESS_START"
    ,"REG_REGION_NOT_LIVE_REGION"
    ,"REG_REGION_NOT_WORK_REGION"
    ,"LIVE_REGION_NOT_WORK_REGION"
    ,"REG_CITY_NOT_LIVE_CITY"
    ,"REG_CITY_NOT_WORK_CITY"
    ,"LIVE_CITY_NOT_WORK_CITY"
    ,"ORGANIZATION_TYPE"
    # ,"FONDKAPREMONT_MODE"
    # ,"HOUSETYPE_MODE"
    # ,"WALLSMATERIAL_MODE"
    # ,"EMERGENCYSTATE_MODE"
    ,"FLAG_DOCUMENT_2"
    ,"FLAG_DOCUMENT_3"
    ,"FLAG_DOCUMENT_4"
    ,"FLAG_DOCUMENT_5"
    ,"FLAG_DOCUMENT_6"
    ,"FLAG_DOCUMENT_7"
    ,"FLAG_DOCUMENT_8"
    ,"FLAG_DOCUMENT_9"
    ,"FLAG_DOCUMENT_10"
    ,"FLAG_DOCUMENT_11"
    ,"FLAG_DOCUMENT_12"
    ,"FLAG_DOCUMENT_13"
    ,"FLAG_DOCUMENT_14"
    ,"FLAG_DOCUMENT_15"
    ,"FLAG_DOCUMENT_16"
    ,"FLAG_DOCUMENT_17"
    ,"FLAG_DOCUMENT_18"
    ,"FLAG_DOCUMENT_19"
    ,"FLAG_DOCUMENT_20"
    ,"FLAG_DOCUMENT_21"
]
# correlation matrix
cor_mat = application_train[numeric_vars].corr()

# missing values in application_train
missing_values = check_missing_values(
    df=application_train,
    columns=numeric_vars+cat_vars
)

train_data = application_train[ids+[dep_var]+numeric_vars+cat_vars]
# logistic regression model
logit=sm.Logit(
    endog=train_data[dep_var],
    exog=statsmodels.tools.tools.add_constant(train_data[numeric_vars]),
    missing='drop'
)
print(logit.fit().summary())









# merging dataframes
bureau = pd.merge(left=pd.read_csv(filepath_or_buffer = directory+r"/raw_datasets/application_train.csv",
                                   sep=',',
                                   encoding='latin-1')[['SK_ID_CURR',
                                                        'TARGET']],
                  right=pd.read_csv(filepath_or_buffer = directory+r"/raw_datasets/bureau.csv",
                                    sep=',',
                                    encoding='latin-1'),
                  how='left',
                  left_on='SK_ID_CURR',
                  right_on='SK_ID_CURR')
