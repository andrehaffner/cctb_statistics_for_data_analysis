from matplotlib import pyplot
from scipy import stats
import pandas as pd
import numpy as np


######################################################## DATA 1 ########################################################

print("\nSamples for questions 1 to 5")

sample1 = np.array([2, 3, 5, 4, 6, 2, 4])
sample2 = np.array([1, 4, 3, 5, 2, 6, 4])

print(sample1, sample2)


###################################################### QUESTION 1 ######################################################

print("\nQ1: What is the difference between the means of sample1 and sample2?")

diff_mean = np.mean(sample1) - np.mean(sample2)

print(f"A1: {diff_mean}")


###################################################### QUESTION 2 ######################################################

print("\nQ2: Is there a significant difference between the means "
      "of sample1 and sample2 at the 5% level of significance?")

t, p = stats.ttest_ind(sample1, sample2, equal_var=True)

if p < 0.05:
    print("A2: There is a significant difference between the means of sample1 and sample2.")
else:
    print("A2: There is not a significant difference between the means of sample1 and sample2.")


###################################################### QUESTION 3 ######################################################

print("\nQ3: Are the variances of sample1 and sample2 equal?")

var1 = np.var(sample1)
var2 = np.var(sample2)

if var1 == var2:
    print("A3: The variances are equal.")
else:
    print("A3: The variances are not equal.")


###################################################### QUESTION 4 ######################################################

print("\nQ4: What's the p-value?")

t, p = stats.ttest_ind(sample1, sample2)
print(f"A4: p-value is {p}.")


###################################################### QUESTION 5 ######################################################

print("\nQ5: Suppose each sample replicate itself once, sample1 becomes 2 times longer with each element repeated. "
      "Is the new p-value larger or smaller?")

new_sample = np.repeat(sample1, 2)
new_t, new_p = stats.ttest_ind(sample1, sample2)

if new_p > p:
    print("A5: the new p value is larger.")
else:
    print("A5: the new p value is smaller.")


######################################################## DATA 2 ########################################################

print("\nSamples for questions 6 to 10:")

sample1 = np.array([2, 3, 5, 4, 6, 2, 4])
sample2 = np.array([1, 4, 3, 5, 2, 6, 4])
sample3 = np.array([4, 3, 2, 1, 6, 5, 4])

print(sample1, sample2, sample3)

# Combine samples into 1 array
data = np.concatenate((sample1, sample2, sample3))
# Calculate the F-statistic and p-value using one-way ANOVA
f_statistic, p = stats.f_oneway(sample1, sample2, sample3)

print(f"Q6-Q10: F-Statistic is {f_statistic}.")


###################################################### QUESTION 6 ######################################################

print("\nQ6: What is the mean of sample1?")

mean1 = np.mean(sample1)

print(f"A6: The mean of sample1 is {mean1}.")


###################################################### QUESTION 7 ######################################################

print("\nQ7: What's the inner product of sample1 and sample2")

inner1x2 = np.inner(sample1, sample2)

print(f"A7: The inner product of sample1 and sample2 is {inner1x2}.")


###################################################### QUESTION 8 ######################################################

print("\nQ8: What's the p-value for the on-way ANOVA test?")

samples = [sample1, sample2, sample3]
f_statistic, p_val = stats.f_oneway(*samples)

print(f"A8: p-value: {p_val}.")


###################################################### QUESTION 9 ######################################################

print("\nQ9: What's the SSB?")

fStatistic, pValue = stats.f_oneway(*samples)
ssb = fStatistic * sum([len(sample) for sample in samples]) / len(samples) - 1

print(f"A9: SSB = {ssb}.")


##################################################### QUESTION 10 #####################################################

print("\nQ10: What's the SST?")

concat_samples = np.concatenate([sample1, sample2, sample3])
overall_mean = np.mean(concat_samples)
sst = np.sum((data - overall_mean)**2)

print(f"A10: SST = {sst}.")


##################################################### QUESTION 11 #####################################################

print("\nQ11: Given a NumPy array x = [2, 4, 6, 8, 10, 12, 14, 16], "
      "what is the 90th percentile of x using the percentile() function?")

x = np.array([2, 4, 6, 8, 10, 12, 14, 16])
per = np.percentile(x, 90)

print(f"A11: 90th percentile of x is {per}.")


##################################################### QUESTION 12 #####################################################

print("\nQ12: Given a NumPy array y = [1, 2, 3, 4, 5], what is the skewness of y?")

y = np.array([1, 2, 3, 4, 5])
s = stats.skew(y)

print(f"A12: Skewness of y is {s}.")


##################################################### QUESTION 13 #####################################################

print("\nQ13: Given a NumPy array z = [10, 20, 30, 40, 50], what is the kurtosis of z?")

z = np.array([10, 20, 30, 40, 50])
k = stats.kurtosis(z)

print(f"A13: The kurtosis of z is {k}.")


##################################################### QUESTION 14 #####################################################

print("\nQ14: Write a function that calculates the correlation coefficient of two arrays, without using NumPy library.")


def correlation_coefficient(x1, x2):
    m1 = sum(x1) / len(x1)
    m2 = sum(x2) / len(x2)
    n = sum((x1[i] - m1) * (x2[i] - m2) for i in range(len(x1)))
    d = (sum((x1[i]-m1)**2 for i in range(len(x1))) * sum((x2[i]-m2)**2 for i in range(len(x2))))**0.5
    if d == 0:
        return 0
    else:
        return n/d


print(f"A14: \ndef correlation_coefficient(x1, x2):\n\tm1 = sum(x1) / len(x1)\n\tm2 = sum(x2) / len(x2)\n\t"
      f"numerator = sum((x1[i] - m1) * (x2[i] - m2) for i in range(len(x1)))\n\t"
      f"denominator = (sum((x1[i]-m1)**2 for i in range(len(x1))) * sum((x2[i]-m2)**2 for i in range(len(x2))))**0.5"
      f"\n\tif denominator == 0:\n\t\treturn 0\n\telse:\n\t\treturn numerator/denominator")


##################################################### QUESTION 15 #####################################################

print("\nQ15: Given two NumPy arrays b = [1, 2, 3, 4, 5] and c = [2, 4, 6, 8, 10], "
      "what is the p-value for the null hypothesis that correlation coefficient between b and c is zero")

b = np.array([1, 2, 3, 4, 5])
c = np.array([2, 4, 6, 8, 10])
corr_coef, p_value = stats.pearsonr(b, c)

print(f"A15: p-value: {p_value}.")


##################################################### QUESTION 16 #####################################################

print("\nQ16: Generate 1000 random numbers from a chi-squared distribution with 5 degrees of freedom. "
      "The sum is close to which of the following values?")

numbers = np.random.chisquare(df=5, size=1000)
s = np.sum(numbers)

print(f"A16: The sum of the numbers is {s}.")


##################################################### QUESTION 17 #####################################################

print("\nQ17: Write a Python function that determine whether a year is a leap year. Is the Year 2200 a leap year?")


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(f"A17: Is the Year 2200 a leap year? {is_leap_year(2200)}.")


##################################################### QUESTION 18 #####################################################

print("\nQ18: Write a Python function to inverse the key-value relationship.")


def inverse_key_value(dictionary): return {value: key for key, value in dictionary.items()}


print("A18:\ndef inverse_key_value(dictionary): return {value: key for key, value in dictionary.items()}")


##################################################### QUESTION 19 #####################################################

print('\nQ19: Given a list of strings my_list = ["apple", "banana", "cherry", "apple", "banana", "apple"], '
      'write a Python program that counts the number of occurrences of each string in the list and stores '
      'the results in a dictionary.')


def list_ocurrrence(my_list): return {item: my_list.count(item) for item in my_list}


print("A19: \ndef list_ocurrrence(my_list): return {item: my_list.count(item) for item in my_list}")


##################################################### QUESTION 20 #####################################################

print(f"\nQ20: Write a Python program that flattens a list of lists with infinite depth.")


def flat_list(my_list):
    new_list = []
    for element in my_list:
        if type(element) == list:
            new_list += flat_list(element)
        else:
            new_list.append(element)
    return new_list


print("A20:\ndef flat_list(my_list):\n\tnew_list = []\n\tfor item in my_list:\n\t\tif type(item) == list:"
      "\n\t\t\tnew_list += flat_list(item)\n\t\telse:\n\t\t\tnew_list.append(item)\n\treturn new_list")


##################################################### QUESTION 21 #####################################################

print(f"\nQ20: Links to the dataset https://datahub.io/core/global-temp \n\tUse the link to "
      f"the dataset and show that there is a positive correlation between the number of year"
      f" and the average temperature.\n\tYou are free to make any assumptions as you see fit.")

data = "Source,Year,Mean,GCAG,2016,0.9363GISTEMP,2016,0.99GCAG,2015,0.8998GISTEMP,2015,0.87GCAG,2014,0.7408GISTEMP," \
       "2014,0.74GCAG,2013,0.6679GISTEMP,2013,0.65GCAG,2012,0.6240GISTEMP,2012,0.63GCAG,2011,0.5788GISTEMP,2011,0." \
       "6GCAG,2010,0.7014GISTEMP,2010,0.71GCAG,2009,0.6367GISTEMP,2009,0.64GCAG,2008,0.5419GISTEMP,2008,0.54GCAG,2" \
       "007,0.6100GISTEMP,2007,0.66GCAG,2006,0.6125GISTEMP,2006,0.63GCAG,2005,0.6585GISTEMP,2005,0.69GCAG,2004,0.5" \
       "783GISTEMP,2004,0.55GCAG,2003,0.6134GISTEMP,2003,0.62GCAG,2002,0.6023GISTEMP,2002,0.63GCAG,2001,0.5473GIST" \
       "EMP,2001,0.55GCAG,2000,0.4262GISTEMP,2000,0.42GCAG,1999,0.4438GISTEMP,1999,0.42GCAG,1998,0.6344GISTEMP,199" \
       "8,0.64GCAG,1997,0.5187GISTEMP,1997,0.48GCAG,1996,0.3228GISTEMP,1996,0.35GCAG,1995,0.4577GISTEMP,1995,0.46G" \
       "CAG,1994,0.3409GISTEMP,1994,0.32GCAG,1993,0.2853GISTEMP,1993,0.24GCAG,1992,0.2571GISTEMP,1992,0.23GCAG,199" \
       "1,0.4055GISTEMP,1991,0.43GCAG,1990,0.4328GISTEMP,1990,0.44GCAG,1989,0.2970GISTEMP,1989,0.29GCAG,1988,0.375" \
       "7GISTEMP,1988,0.41GCAG,1987,0.3696GISTEMP,1987,0.33GCAG,1986,0.2296GISTEMP,1986,0.19GCAG,1985,0.1342GISTEM" \
       "P,1985,0.12GCAG,1984,0.1490GISTEMP,1984,0.15GCAG,1983,0.3411GISTEMP,1983,0.3GCAG,1982,0.1815GISTEMP,1982,0" \
       ".13GCAG,1981,0.2999GISTEMP,1981,0.33GCAG,1980,0.2637GISTEMP,1980,0.27GCAG,1979,0.2273GISTEMP,1979,0.17GCAG" \
       ",1978,0.1123GISTEMP,1978,0.07GCAG,1977,0.1978GISTEMP,1977,0.18GCAG,1976,-0.0792GISTEMP,1976,-0.11GCAG,1975" \
       ",0.0034GISTEMP,1975,-0.02GCAG,1974,-0.0719GISTEMP,1974,-0.07GCAG,1973,0.1641GISTEMP,1973,0.15GCAG,1972,0.0" \
       "264GISTEMP,1972,0.01GCAG,1971,-0.0783GISTEMP,1971,-0.09GCAG,1970,0.0372GISTEMP,1970,0.02GCAG,1969,0.0929GI" \
       "STEMP,1969,0.07GCAG,1968,-0.0296GISTEMP,1968,-0.07GCAG,1967,-0.0131GISTEMP,1967,-0.02GCAG,1966,-0.0227GIST" \
       "EMP,1966,-0.05GCAG,1965,-0.0780GISTEMP,1965,-0.1GCAG,1964,-0.1495GISTEMP,1964,-0.2GCAG,1963,0.1068GISTEMP," \
       "1963,0.06GCAG,1962,0.0888GISTEMP,1962,0.03GCAG,1961,0.0775GISTEMP,1961,0.05GCAG,1960,0.0204GISTEMP,1960,-0" \
       ".02GCAG,1959,0.0596GISTEMP,1959,0.03GCAG,1958,0.1095GISTEMP,1958,0.07GCAG,1957,0.0488GISTEMP,1957,0.04GCAG" \
       ",1956,-0.1990GISTEMP,1956,-0.2GCAG,1955,-0.1354GISTEMP,1955,-0.15GCAG,1954,-0.1165GISTEMP,1954,-0.13GCAG,1" \
       "953,0.0952GISTEMP,1953,0.08GCAG,1952,0.0248GISTEMP,1952,0.01GCAG,1951,-0.0132GISTEMP,1951,-0.07GCAG,1950,-" \
       "0.1616GISTEMP,1950,-0.18GCAG,1949,-0.0568GISTEMP,1949,-0.09GCAG,1948,-0.0487GISTEMP,1948,-0.09GCAG,1947,-0" \
       ".0477GISTEMP,1947,-0.05GCAG,1946,-0.0040GISTEMP,1946,-0.04GCAG,1945,0.1710GISTEMP,1945,0.12GCAG,1944,0.292" \
       "8GISTEMP,1944,0.25GCAG,1943,0.1570GISTEMP,1943,0.13GCAG,1942,0.1538GISTEMP,1942,0.09GCAG,1941,0.1960GISTEM" \
       "P,1941,0.12GCAG,1940,0.0947GISTEMP,1940,0.08GCAG,1939,-0.0139GISTEMP,1939,-0.03GCAG,1938,-0.0288GISTEMP,19" \
       "38,-0.03GCAG,1937,-0.0157GISTEMP,1937,-0.03GCAG,1936,-0.1134GISTEMP,1936,-0.15GCAG,1935,-0.1392GISTEMP,193" \
       "5,-0.2GCAG,1934,-0.1015GISTEMP,1934,-0.14GCAG,1933,-0.2439GISTEMP,1933,-0.29GCAG,1932,-0.1168GISTEMP,1932," \
       "-0.17GCAG,1931,-0.0686GISTEMP,1931,-0.09GCAG,1930,-0.1003GISTEMP,1930,-0.15GCAG,1929,-0.2985GISTEMP,1929,-" \
       "0.36GCAG,1928,-0.1774GISTEMP,1928,-0.21GCAG,1927,-0.1546GISTEMP,1927,-0.21GCAG,1926,-0.0667GISTEMP,1926,-0" \
       ".1GCAG,1925,-0.1481GISTEMP,1925,-0.21GCAG,1924,-0.2486GISTEMP,1924,-0.28GCAG,1923,-0.2156GISTEMP,1923,-0.2" \
       "4GCAG,1922,-0.2304GISTEMP,1922,-0.28GCAG,1921,-0.1485GISTEMP,1921,-0.21GCAG,1920,-0.2105GISTEMP,1920,-0.27" \
       "GCAG,1919,-0.2055GISTEMP,1919,-0.22GCAG,1918,-0.2084GISTEMP,1918,-0.26GCAG,1917,-0.3146GISTEMP,1917,-0.4GC" \
       "AG,1916,-0.2930GISTEMP,1916,-0.34GCAG,1915,-0.0693GISTEMP,1915,-0.11GCAG,1914,-0.1395GISTEMP,1914,-0.16GCA" \
       "G,1913,-0.3162GISTEMP,1913,-0.34GCAG,1912,-0.3288GISTEMP,1912,-0.35GCAG,1911,-0.4332GISTEMP,1911,-0.44GCAG" \
       ",1910,-0.3789GISTEMP,1910,-0.42GCAG,1909,-0.4261GISTEMP,1909,-0.47GCAG,1908,-0.4396GISTEMP,1908,-0.43GCAG," \
       "1907,-0.3706GISTEMP,1907,-0.4GCAG,1906,-0.2174GISTEMP,1906,-0.23GCAG,1905,-0.2931GISTEMP,1905,-0.28GCAG,19" \
       "04,-0.4194GISTEMP,1904,-0.44GCAG,1903,-0.3369GISTEMP,1903,-0.35GCAG,1902,-0.2463GISTEMP,1902,-0.27GCAG,190" \
       "1,-0.1417GISTEMP,1901,-0.15GCAG,1900,-0.0679GISTEMP,1900,-0.09GCAG,1899,-0.1173GISTEMP,1899,-0.16GCAG,1898" \
       ",-0.2546GISTEMP,1898,-0.28GCAG,1897,-0.1224GISTEMP,1897,-0.11GCAG,1896,-0.0974GISTEMP,1896,-0.15GCAG,1895," \
       "-0.2290GISTEMP,1895,-0.21GCAG,1894,-0.2808GISTEMP,1894,-0.31GCAG,1893,-0.3212GISTEMP,1893,-0.3GCAG,1892,-" \
       ".3062GISTEMP,1892,-0.27GCAG,1891,-0.2532GISTEMP,1891,-0.24GCAG,1890,-0.3220GISTEMP,1890,-0.37GCAG,1889,-0." \
       "0982GISTEMP,1889,-0.12GCAG,1888,-0.1471GISTEMP,1888,-0.2GCAG,1887,-0.2489GISTEMP,1887,-0.33GCAG,1886,-0.20" \
       "03GISTEMP,1886,-0.31GCAG,1885,-0.2125GISTEMP,1885,-0.32GCAG,1884,-0.2009GISTEMP,1884,-0.28GCAG,1883,-0.142" \
       "4GISTEMP,1883,-0.21GCAG,1882,-0.0648GISTEMP,1882,-0.1GCAG,1881,-0.0628GISTEMP,1881,-0.12GCAG,1880,-0.1148G" \
       "ISTEMP,1880,-0.2"

data_list = data.split(",")

count = 0
year = []
mean = []
for item in data_list:
    if count == 0:
        count += 1
        pass
    elif count == 1:
        count += 1
        year.append(item)
    else:
        count = 0
        mean.append(item)

df = pd.DataFrame({'year': year, 'mean': mean})
df = df.sort_values(by='year')
pyplot.plot(df['year'], df['mean'], marker='o', linestyle='', markersize=5)
pyplot.xlabel('year')
pyplot.ylabel('Average Temperature')
pyplot.title('Average Global Temperature Over Years')
pyplot.show()
