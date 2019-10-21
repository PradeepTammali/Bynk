This is simple and basic approach where it combines the data in different formats to single csv file. It loads the data direclty form the URLs to dataframes. We find the correlation between the different datasets and merge them together based on the column with dependecy in both dataframes. 

# Prerequisites
Python 3.7

# Usage
```
git clone https://github.com/PradeepTammali/Bynk.git
cd Approach-1
python3.7 -n pip install -r requirements.txt
python3.7 merge_files.py
```
After the script is executed successfully, you will find a file `merged_data.csv` which contains the merged data of loans, customers and visits.


