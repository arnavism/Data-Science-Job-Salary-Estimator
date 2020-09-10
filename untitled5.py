# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:05:15 2020

@author: ARNAV
"""

import glassdoor_scraper as gs
import pandas as pd
path="C:/Users/ARNAV/Documents/ds_salary_proj/chromedriver"
df=gs.get_jobs('data scientist',15,False,path,15)