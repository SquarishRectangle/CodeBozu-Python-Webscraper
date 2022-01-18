from math import nan
import pandas as pd
import htmlParser
from tools import *
from vars import *
import random



rBenchmark = []
for president in presidentNames:
    rBenchmark.append(htmlParser.benchmark(president))

print (rBenchmark)
benchmark = []
for b in rBenchmark:
    benchmark.append(sum(b))
print (benchmark)

df = pd.DataFrame([benchmark], columns=presidentNames)
df.to_csv("president benchmark.csv")

