# importing modules
import pandas as pd

# folder path
directory = r"/Users/sandeepsanyal/OneDrive/Github/Home_Credit_Default_Risk-by-kaggle.com"

# Importing application_train.csv
application_train = pd.read_csv(filepath_or_buffer = directory+r"/raw_datasets/application_train.csv",
                                sep=',',
                                encoding='latin-1')
bureau = pd.read_csv(filepath_or_buffer = directory+r"/raw_datasets/bureau.csv",
                     sep=',',
                     encoding='latin-1')
bureau_balance = pd.read_csv(filepath_or_buffer = directory+r"/raw_datasets/bureau_balance.csv",
                             sep=',',
                             encoding='latin-1')
credit_card_balance = pd.read_csv(filepath_or_buffer = directory+r"/raw_datasets/credit_card_balance.csv",
                                  sep=',',
                                  encoding='latin-1')
installments_payments = pd.read_csv(filepath_or_buffer = directory+r"/raw_datasets/installments_payments.csv",
                                    sep=',',
                                    encoding='latin-1')
POS_CASH_balance = pd.read_csv(filepath_or_buffer = directory+r"/raw_datasets/POS_CASH_balance.csv",
                               sep=',',
                               encoding='latin-1')
previous_application = pd.read_csv(filepath_or_buffer = directory+r"/raw_datasets/previous_application.csv",
                                   sep=',',
                                   encoding='latin-1')

# EDA
numeric_vars = [
    "CNT_CHILDREN"
    ,"AMT_INCOME_TOTAL"
    ,"AMT_CREDIT"
    # ,"AMT_ANNUITY"
    ",REGION_POPULATION_RELATIVE"
    # ,"DAYS_BIRTH"
    ,"DAYS_EMPLOYED"
    ,"DAYS_REGISTRATION"
    ,"DAYS_ID_PUBLISH"
    ,"OWN_CAR_AGE"
    ,"EXT_SOURCE_1"
    ,"EXT_SOURCE_2"
    ,"EXT_SOURCE_3"
    ,"APARTMENTS_AVG"
    # ,"BASEMENTAREA_AVG"
    ,"YEARS_BEGINEXPLUATATION_AVG"
    # ,"YEARS_BUILD_AVG"
    # ,"COMMONAREA_AVG"
    # ,"ELEVATORS_AVG"
    # ,"ENTRANCES_AVG"
    # ,"FLOORSMAX_AVG"
    # ,"FLOORSMIN_AVG"
    # ,"LANDAREA_AVG"
    # ,"LIVINGAPARTMENTS_AVG"
    # ,"LIVINGAREA_AVG"
    ,"NONLIVINGAPARTMENTS_AVG"
    ,"NONLIVINGAREA_AVG"
    ,"OBS_30_CNT_SOCIAL_CIRCLE"
    ,"DEF_30_CNT_SOCIAL_CIRCLE"
    # ,"OBS_60_CNT_SOCIAL_CIRCLE"
    # ,"DEF_60_CNT_SOCIAL_CIRCLE"
    ,"DAYS_LAST_PHONE_CHANGE"
    ,"AMT_REQ_CREDIT_BUREAU_HOUR"
    ,"AMT_REQ_CREDIT_BUREAU_DAY"
    ,"AMT_REQ_CREDIT_BUREAU_WEEK"
    ,"AMT_REQ_CREDIT_BUREAU_MON"
    ,"AMT_REQ_CREDIT_BUREAU_QRT"
    ,"AMT_REQ_CREDIT_BUREAU_YEAR"
]
# correlation matrix
cor_mat = application_train[numeric_vars].corr()

# missing values in application_train
missing_values = pd.DataFrame(data=((len(application_train.index)-application_train[numeric_vars].count())/len(application_train.index))*100,
                              columns=["Pecentage Missing"])
missing_values.sort_values(by="Pecentage Missing",
                           ascending=False,
                           axis=0,
                           inplace=True)









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
