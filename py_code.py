# importing modules
import pandas as pd

# folder path
directory = r"C:\Users\v-sanysa\OneDrive\Github\Predict-Blood-Donations-by-datadriven.org"

# Importing application_train.csv
application_train = pd.read_csv(filepath_or_buffer = directory+r'\raw_datasets\application_train.csv',
                                sep=',',
                                encoding='latin-1')
bureau = pd.read_csv(filepath_or_buffer = directory+r'\raw_datasets\bureau.csv',
                     sep=',',
                     encoding='latin-1')
bureau_balance = pd.read_csv(filepath_or_buffer = directory+r'\raw_datasets\bureau_balance.csv',
                             sep=',',
                             encoding='latin-1')
credit_card_balance = pd.read_csv(filepath_or_buffer = directory+r'\raw_datasets\credit_card_balance.csv',
                                  sep=',',
                                  encoding='latin-1')
installments_payments = pd.read_csv(filepath_or_buffer = directory+r'\raw_datasets\installments_payments.csv',
                                    sep=',',
                                    encoding='latin-1')
POS_CASH_balance = pd.read_csv(filepath_or_buffer = directory+r'\raw_datasets\POS_CASH_balance.csv',
                               sep=',',
                               encoding='latin-1')
previous_application = pd.read_csv(filepath_or_buffer = directory+r'\raw_datasets\previous_application.csv',
                                   sep=',',
                                   encoding='latin-1')

application_train["TARGET"], pd.DataFrame({application_train["AMT_CREDIT"], application_train["AMT_ANNUITY"])

a = num_bin(Y = application_train["TARGET"],
             X = application_train["AMT_CREDIT"],
             n=10)

a = pd.DataFrame({"AMT_CREDIT" : application_train["AMT_CREDIT"],
                  "AMT_ANNUITY" : application_train["AMT_ANNUITY"]})
application_train.iloc[47531, 0]

b = char_bin(Y = application_train["TARGET"],
             X = application_train["NAME_INCOME_TYPE"])

