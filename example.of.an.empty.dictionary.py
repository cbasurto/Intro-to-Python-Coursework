# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:52:20 2015

@author: ESAccount24
"""

empty = {}
RedFlowers = {"rose" :1,"poppy" :1, "narcissus" :2, "tulip" :1, "carnation" :1, "jasmine" :2}
#RedFlowers["rose"] returns 1
d = RedFlowers
for key in d:
    print key
    
#example dictionaries from list

dishes=["pizza","sauerkraut","paella","Hamburger"]
countries=["Italy","Germany","Spain","USA"]
country_specialties=zip(countries, dishes)
print country_specialties
