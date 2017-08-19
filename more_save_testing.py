#more_save_testing.py
import os, sys, pickle

save_file = 'save_test.txt'
swaglist = ['pallet_town', 'left', 343]

def save():
	pickle.dump(swaglist, save_file)
	
def load():
	swaglist = pickle.load(save_file)
	
print swaglist
save()
swaglist = ['clear', 'all clear here']
print swaglist
load()
print swaglist