-- select top 10
-- 	*
-- from
-- 	[Home Credit Default Risk].[dbo].[application_train] a
-- left join
-- 	[Home Credit Default Risk].[dbo].[bureau] b
-- 	on
-- 		a.[SK_ID_CURR] = b.[SK_ID_CURR]
-- left join
-- 	[Home Credit Default Risk].[dbo].[bureau_balance] c
-- 	on
-- 		b.[SK_ID_BUREAU] = c.[SK_ID_BUREAU]
-- left join
-- 	[Home Credit Default Risk].[dbo].[previous_application] d
-- 	on
-- 		a.[SK_ID_CURR] = d.[SK_ID_CURR]
-- left join
-- 	[Home Credit Default Risk].[dbo].[POS_CASH_balance] e
-- 	on
-- 		d.[SK_ID_PREV] = e.[SK_ID_PREV]
-- left join
-- 	[Home Credit Default Risk].[dbo].[installments_payments] f
-- 	on
-- 		d.[SK_ID_PREV] = f.[SK_ID_PREV]
-- left join
-- 	[Home Credit Default Risk].[dbo].[credit_card_balance] g
-- 	on
-- 		d.[SK_ID_PREV] = g.[SK_ID_PREV]




SELECT * FROM home_credit_default_risk.bureau LIMIT 100;

DESCRIBE home_credit_default_risk.bureau;


SELECT 
    table_schema as `Database`, 
    table_name AS `Table`, 
    round(((data_length + index_length) / 1024 / 1024), 2) `Size in MB` 
FROM information_schema.TABLES 
ORDER BY (data_length + index_length) DESC;