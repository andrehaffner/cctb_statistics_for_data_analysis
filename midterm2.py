from scipy import stats
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
    print("A3: The variances are equal!")
else:
    print("A3: The variances are not equal!")


###################################################### QUESTION 4 ######################################################

print("\nQ4: What's the p-value?")

t, p = stats.ttest_ind(sample1, sample2)
print(f"A4: p-value is {p}!")


###################################################### QUESTION 5 ######################################################

print("\nQ5: Suppose each sample replicate itself once, sample1 becomes 2 times longer with each element repeated. "
      "Is the new p-value larger or smaller?")


new_sample = np.repeat(sample1, 2)
new_t, new_p = stats.ttest_ind(sample1, sample2)

if new_p > p:
    print("A5: the new p value is larger!")
else:
    print("A5: the new p value is smaller!")


######################################################## DATA 2 ########################################################

print("\nSamples for questions 6 to 10:")

sample1 = np.array([2, 3, 5, 4, 6, 2, 4])
sample2 = np.array([1, 4, 3, 5, 2, 6, 4])
sample3 = np.array([4, 3, 2, 1, 6, 5, 4])
print(sample1, sample2, sample3)

# Combine samples into 1 array
data = np.concatenate((sample1, sample2, sample3))
# Calculate the F-statistic and p-value using one-way ANOVA
f_statistic, p_value = stats.f_oneway(sample1, sample2, sample3)

print(f"Q6-Q10: F-Statistic is {f_statistic}!")


###################################################### QUESTION 6 ######################################################

print("\nQ6: What is the mean of sample1?")

mean1 = np.mean(sample1)
print(f"A6: The mean of sample1 is {mean1}!")


###################################################### QUESTION 7 ######################################################

print("\nQ7: What's the inner product of sample1 and sample2")

inner1x2 = np.inner(sample1, sample2)
print(f"A7: The inner product of sample1 and sample2 is {inner1x2}")


###################################################### QUESTION 8 ######################################################

print("\nQ8: What's the p-value for the on-way ANOVA test?")

samples = [sample1, sample2, sample3]
f_statistic, p_val = stats.f_oneway(*samples)
print("A8: p-value:", p_val)


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
print(f"A10: SST = {sst}")
