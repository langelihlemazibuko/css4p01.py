# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:23:26 2024

@author: lange
"""

import pandas as pd

from collections import Counter

df = pd.read_csv("C:/Users/lange/CSS4_ day2/data_02/movie_dataset.csv")
df.dropna(inplace=True)


print(df["Revenue (Millions)"]. mean())
print(Counter(df["Year"]))

print(Counter(df["Genre"]))

print(df["Actors"].mode())

print(df["Rating"].max())
print(df["Revenue (Millions)"].loc[2015 -2017].mean)
import numpy as np
"""
a = np.asarray(df["Runtime (Minutes)"])
b = np.asarray(df["Rating"])
c = np.asarray(df["Votes"])
d = np.asarray(df["Revenue (Millions)"])
e = np.asarray(df["Metascore"])
sum_a = np.sum(a)
sum_b = np.sum(b)
sum_c = np.sum(c)
sum_d = np.sum(d)
sum_e = np.sum(e)

sum_a1 = np.sum(np.square(a))
sum_b1 = np.sum(np.square(b))
sum_c1 = np.sum(np.square(c))
sum_d1 = np.sum(np.square(d))
sum_e1 = np.sum(np.square(e))
n = 838
sum_ab = np.sum(a*b)
sum_ac = np.sum(a*c)
sum_cd = np.sum(c*d)
sum_be = np.sum(b*e)
print(f"sum_a = {sum_a}")
print(f"sum_a1 = {sum_a1}")
print(f"sum_b = {sum_b}")
print(f"sum_b1 = {sum_b1}")
print(f"sum_ab = {sum_ab}")
print(f"n = {n}")
top1 = n*sum_ab - sum_a*sum_b
print(f"top1= {top1}")
bot_x = np.sqrt(n*sum_a1 - np.square(sum_a))
bot_y = np.sqrt(n*sum_b1 - np.square(sum_b))
bot2 = bot_x*bot_y
print(f"bot2 = {bot2}")
R_1 = np.square(top1/bot2)
print(f"R_1 = {R_1}")

print(f"sum_c = {sum_c}")
print(f"sum_c1 = {sum_c1}")

top3 = n*sum_ac - sum_a*sum_c
print(f"top3= {top3}")
bot_t = np.sqrt(n*sum_a1 - np.square(sum_a))
bot_w = np.sqrt(n*sum_c1 - np.square(sum_c))
bot4 = bot_t*bot_w
print(f"bot4 = {bot4}")
R_2 = np.square(top3/bot4)
print(f"R_2 = {R_2}")

print(f"sum_d = {sum_d}")
print(f"sum_d1 = {sum_d1}")

top5 = n*sum_cd - sum_c*sum_d
print(f"top5= {top5}")
bot_z = np.sqrt(n*sum_c1 - np.square(sum_c))
bot_z1 = np.sqrt(n*sum_d1 - np.square(sum_d))
bot6 = bot_z*bot_z1
print(f"bot6 = {bot6}")
R_3 = np.square(top5/bot6)
print(f"R_3 = {R_3}")

print(f"sum_e = {sum_e}")
print(f"sum_e1 = {sum_e1}")

top7 = n*sum_be - sum_b*sum_e
print(f"top7= {top7}")
bot_z3 = np.sqrt(n*sum_b1 - np.square(sum_b))
bot_z4 = np.sqrt(n*sum_e1 - np.square(sum_e))
bot8 = bot_z3*bot_z4
print(f"bot8 = {bot8}")
R_4 = np.square(top7/bot8)
print(f"R_4 = {R_4}") """



