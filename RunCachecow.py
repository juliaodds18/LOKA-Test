#!/usr/bin/python
from PyMimircache import Cachecow
import sys

c = Cachecow() 
if (int(len(sys.argv)) < 2):
	print("Too few arguments, please input path to file you want to anal-yze")
	exit()
c.open(sys.argv[1])
c.heatmap('v', "hit_ratio_start_time_end_time", time_interval=-1, num_of_pixels=-1, algorithm="LRU", cache_params=None, cache_size=2000)


