# Excel-tools

## Design

1. Input files were put at `resources/input`
2. Import all data from data_book to mongodb
3. Aggregate data
   - Group by SUP name
   - Group by Month
   - Group by customer
   - Make output


```text
'data_range': ('A', 1, 2271), // A - start from column A, 1 - start from row num 1, 2271 - end at row num 2271
```

## Run unit test

```bash
py -m unittest tests.excel_mongo_tool_test
```

## Docker
`./up.sh` to start
`./down.sh` to end and clean up

## Environment

$ py --version  
Python 3.6.5

openpyxl 2.5.2

NOTE: openpyxl 2.5.3 bug can not copy merge sheet

## Python hint:

Dependency guide: https://pip.pypa.io/en/stable/user_guide/#id1
1. create dependency file: `pip3 freeze > requirements.txt`
1. install dependencies: `pip install -r requirements.txt`
