# import packages
import csv
import streamlit as st
import pandas as pd
import numpy as np

# import modules
import bloom_filter as bf
import flajonet_martin as fm

def read_data():
    tsv_file = open("drugsCom_raw\drugsComTrain_raw.tsv", encoding="utf8")
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    data = []
    next(read_tsv) # skip first row
    for row in read_tsv:
        row[3] = '...'
        data.append(row)
    return data

# read data
data = read_data()

# visualize data
column_titles = ['ID', 'drugName', 'condition', 'review', 'rating', 'date',
'usefulCount']
df = pd.DataFrame(data[:3], columns=column_titles)
st.header('Visualization of Data')
st.write(df)

# extract unique IDs
id_data = []
for row in data:
    id_data.append(row[0])

# generate set with allowed IDs
n = len(id_data)
n_allowed = round(0.1 * n)
allowed_id_data = id_data[0:n_allowed]

# extract ratings
ratings = []
for row in data:
    ratings.append(int(float(row[4])))

# bloom filter
st.header('Bloom Filter')
# get array length of bloom filter as input
filter_array_length = st.slider('Choose a filter length for the Bloom Filter.',
1000, 10000000, step=100)
# get id as element for checking
id = st.number_input('Insert the ID which you want to check.')

# create bloom filter
bloom_filter = bf.BloomFilter(filter_array_length, allowed_id_data)
is_allowed = bloom_filter.check_element(id)

# print result of bloom filter
if is_allowed:
    bloom_filter_answer = 'This element is valid.'
else:
    bloom_filter_answer = 'This element is not valid.'
st.write(bloom_filter_answer)

# flajonet-martin
st.header('Counting different elements with Flajonet-Martin')

# create estimator
estimator = fm.flajonet_martin_estimator(ratings)
estimation = estimator.count()

# print results
estimation_answer = 'The estimated number of different element is ' + \
str(estimation) + '.'
st.write(estimation_answer)
real_answer = 'The real number of different elements is 10.'
st.write(real_answer)
