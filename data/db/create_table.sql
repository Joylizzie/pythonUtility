create table mechant

"TRANSACTION ID" varchar(100),
"BATCH TYPE" varchar(100),
"TRANSACTION TYPE" varchar(100)
,"PAY METHOD" varchar(100)
,"PAY PROCESSOR ID" varchar(100)
,"NET AMOUNT"
,"CURRENCY TYPE" varchar(3)
,"REVERSED" varchar(100)
,"BATCH DEPOSIT DATE"varchar(100)
,"ORIGINATION VENDOR" varchar(100);

create table crm

"Activity Date" DATE
,"Settlement Date" DATE
,"Vantiv Payment ID" varchar(100)
,"Parent Vantiv Payment ID" varchar(100)
,"Txn Type" varchar(100)
,"Settlement Currency" varchar(3)
, "Net Amount" numeric
,"Payment Type" varchar(100)