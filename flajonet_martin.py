'''
This code was mainly taken from
https://github.com/SrGrace/Hacktoberfest-1/blob/master/Python/flajolet-martin-algorithm.py
this link and partly modified.
'''

import numpy as np

class flajonet_martin_estimator():
	def __init__(self, stream_data):
		self.stream_data = stream_data

	def count(self):
		inputCount = 5
		abcList = [[3, 5, 9], [4, 6, 8], [7, 5, 4], [5, 7, 11], [13, 33, 23]]
		finalCountsRecorded = []

		for i in abcList:
			binElems = []
			for j in set(self.stream_data):
				binElems.append(str(bin((i[0]*j+i[1])%i[2])).split("b")[1])
			greatestTrailing = 0
			for k in binElems:
				reversedCount = k[::-1]
				count = 0
				for i in reversedCount:
					if(i=='1'):
						if(count>greatestTrailing):
							greatestTrailing = count
						break
					else:
						count+=1
			finalCountsRecorded.append(2**greatestTrailing)
		average = round(np.mean(finalCountsRecorded))
		print('average:', average)
		return average
