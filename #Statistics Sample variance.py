#Statistics Sample variance

sample = np.arrange(5,25,5)
s_mean = sum(sample)/len(sample)
sq_s_deviation = [(i-s_mean)**2 for i in sample]
s_variance = sum(sq_s_deviation)/len(sample)-1
print('Sample variance : {}'. format(round(s_variance,2)))
