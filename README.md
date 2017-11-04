# Get Your Guide Python engineer - marketing technology take home test

### Metrics
- A higher CTR means the ads reach a more suitable audience.
- A lower Position value (1 is lower than 2) means less was paid for the ads.
- A higher Revenue/Cost ratio (`ratio = revenue / (impressions * cost)`, assuming cost is per impression) means
the campain is more profitable.

The SEM Performance metric (SEMP) will be `(impressions * cost * position) / (ctr * revenue)`. The smaller SEMP
is, the better.

### How to use
1. Install python 3
2. Give script execute permission
```
chmod +x measure_semp.py
```
3. Run script with data file 
```
./measure_semp.py take_home_test_data.csv
```

### Todo
1. Refactor logic into a class for better reusability and testability
2. Write tests
