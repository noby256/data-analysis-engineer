## E2 - crawling, data extraction of a static website
A user asks about how he can obtain data of a website without spending days to extract the data by hand
Look at https://www.urparts.com/index.cfm/page/catalogue and check for manufacturer, then look into the categories, then the models and the result set where the part (number) before ‘ - ‘ and the part category
crawl the catalog and create a CSV file with the following data (example):

```
manufacturer,category,model,part,part_category
Ammann,Roller Parts,ASC100,ND011710,LEFT COVER
Ammann,Roller Parts,ASC100,ND011758,VIBRATOR
Ammann,Roller Parts,ASC100,ND011785,RIGHT COVER
Ammann,Roller Parts,ASC100,ND017673,ECCENTRIC
Ammann,Roller Parts,ASC100,ND017675,ECCENTRIC
Ammann,Roller Parts,ASC100,ND018184,HUB
Ammann,Roller Parts,ASC100,ND018193,BRACKET
Ammann,Roller Parts,ASC100,ND018214,LEFT SHAFT
Ammann,Roller Parts,ASC100,ND018216,RIGHT SHAFT
```

#### Solution
```
scrapy runspider data_engineer/E2/catalogue_spider.py -o data_engineer/E2/1.csv
```