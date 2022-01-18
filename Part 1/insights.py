from numpy import NaN
import pandas as pd

#insight 1
df = pd.read_csv("U.S. President Biodata.csv")
numOnlyPresident = df["President"].tolist().count(NaN)
numOnlyVice = df["Vice President"].tolist().count(NaN)
numAll = len(df.index)
numBoth = numAll - numOnlyPresident - numOnlyVice
print ("There are %d people who have been a president or a vice president of the US" % numAll)
#print ("Of them %d have only been president" % numOnlyPresident)
#print ("%d have only been vice president" %numOnlyVice)
print ("but only %d have been both president and vice president" % numBoth)
#print()
#print ("This means only %d%% of presidents were also vice presidents" % round(numBoth/(numBoth + numOnlyPresident) * 100, 2))
#print ("and only %d%% of vice presidents went on to become president" % round(numBoth/(numBoth + numOnlyVice) * 100, 2))
print ("this is only %d%%!" % round(numBoth/numAll * 100, 2))
print()

#insight 2
numNoSpouse = df["Spouse(s)"].tolist().count(NaN)
numNoChildren = df["Children"].tolist().count(NaN)
print ("%d presidents did not have children" % numNoChildren)
print ("and Only %d did not have spouces" % numNoSpouse)