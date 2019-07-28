# importing datasets
file_names = c(c()
               # ,"bureau_balance"
               # ,"credit_card_balance"
               # ,"installments_payments"
               # ,"POS_CASH_balance"
               # ,"previous_application"
                # ,"application_test"
               ,"application_train"
               ,"bureau"
               )
for(names in file_names){
  assign(names,
         read.csv(file = paste("/Users/sandeepsanyal/OneDrive/Github/Home_Credit_Default_Risk-by-kaggle.com/raw_datasets/",
                               names, ".csv", sep = ""),
                  na.strings = c("", " ", "NULL", "NA", "na"),
                  stringsAsFactors = FALSE))
}
remove(file_names, names)

id = "SK_ID_CURR"
dep_var = "TARGET"
ind_vars = colnames(application_train)[!colnames(application_train) %in% c(id, dep_var)]

# converting to factors
cat_vars = c()
for(i in c(dep_var, ind_vars)){
  if((length(unique(application_train[,i])) < 6) |
     (class(application_train[,i]) == "character")){
    application_train[,i] = factor(application_train[,i],
                                   levels = sort(unique(application_train[,i])))
    cat_vars = c(cat_vars, i)
  }
}
cat_vars = cat_vars[!cat_vars %in% dep_var]
num_vars = ind_vars[!ind_vars %in% c(id, dep_var, cat_vars)]

library(woeBinning)
binning = woe.binning(df = application_train,
                      target.var = dep_var,
                      pred.var = cat_vars,
                      min.perc.total = 0.2,
                      min.perc.class = 0.05,
                      stop.limit = 0.1,
                      abbrev.fact.levels = 50,
                      event.class = 1)
# deploying the binning results
data_binned = woe.binning.deploy(df = application_train,
                                 binning = binning,
                                 min.iv.total=0.02)
# choosing only the binned columns
cat_vars = colnames(data_binned[,c((ncol(application_train)+1):ncol(data_binned))])

binned_only = data_binned[,(colnames(data_binned) %in% c(id, dep_var, cat_vars, num_vars))]
ind_vars = c(cat_vars, num_vars)


col_type = data.frame("Variable" = as.character(),
                      "Type" = as.character(),
                      "Unique_values" = as.integer(),
                      "N_NA" = as.integer())
for(i in c(dep_var, ind_vars)){
  col_type = rbind(col_type,
                   data.frame("Variable" = as.character(i),
                              "Type" = as.character(class(binned_only[,i])),
                              "Unique_values" = as.integer(length(unique(binned_only[,i]))),
                              "N_NA" = as.integer(sum(is.na(binned_only[,i])))))
}
col_type = col_type[order(col_type$Unique_values),]

model = glm(formula = as.formula(paste(dep_var,
                                       paste(ind_vars,
                                                      collapse = "+"),
                                       sep = "~")),
            data = temp,
            family = binomial(link = "logit"))
View(summary(temp_model)$coefficients)
temp_model = step(object = model,
            direction = "both")

for(i in 1:nrow(binned_only)){
  if(sum(is.na(binned_only[i,])) < 1){
    temp = rbind(temp, binned_only[i,])
  }
}