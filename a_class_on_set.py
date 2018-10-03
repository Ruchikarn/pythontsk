sample_list = [3, 3, 4, 5, 6]
print(set(sample_list))

A = {2, 3, 4, 5}
B = {4, 5, 6, 7}

A_U_B = A.union(B)
print(A_U_B)
A_n_B = A.intersection(B)
print(A_n_B)
A_minus_B = A - B  # A.difference(B)
B_minus_A = B - A
print(A_minus_B)
print(B_minus_A)

