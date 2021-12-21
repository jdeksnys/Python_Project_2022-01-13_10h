# Remez Approximation Algorithm

## Additional variables
a - coefficient of p(x) polynomial;
self.name_dict - dictionary of value NAMES used in input prompt (lower, upper, n). Mapped to self.var_dict using variable names;
self.var_dict - dictionary of VALUES used to store input data (lower, upper, n);


## 2021-12-21 changes (jonas):
1. Added self. where needed (ex.: self.f, self.reference);
2. If initial reference points given (datatype 'list'!) when calling remez(), use that list (lower, upper, n sotred in self.var_dict);
3. If initial guesses not given, prompt user for input until correct data type given (numeric). Stored in self.var_dict;
4. Degree of polynomial is stored in self.n for easier readability;