# This entrypoint file to be used in development. Start by reading README.md
# from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["1 + 9", "9999 + 9999", "45 + 43", "123 + 49"], False))


# # Run unit tests automatically
# main(['-vv'])


# states = ['Massachusetts', 'Pennsylvania','Utah','Ohio','California']
# columns = ['Name', 'Population', 'Average Income', 'Crime Rate']
# p_f = '0'
# p_m = '1'
# av = '23'
# cr = '7'

# row_format = '{:>17}' * (len(columns))
# print('-'*90)
# print(row_format.format(*columns))
# print('-'*90)

# for state in states:
#     state_data = [p_f + '/' + p_m, av, cr]
#     print(row_format.format(state, *state_data))
