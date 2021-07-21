# Expected Output
# 012, 013, 014, 015, 016, 017, 018, 019, 023, 024, 025, 026, 027, 028, 029, 034 ...

# pseudo code

# def nums(lst):
#     for 백의자리수 in lst:
#         for 십의자리수 in lst:
#             for 일의자리수 in lst:
#                 if 백의자리수 < 십의자리수:
#                     if 십의자리수 < 일의자리수:
#                         print()



number_list = range(0, 10)
numbers = []

def make_numbers(list):
    for hundred in list: 
        for ten in list: 
            for one in list: 
                if hundred < ten:
                    if ten < one:
                        target = '{}{}{}'.format(hundred, ten, one) # 세자리 수를 하나로 이어줌(문자열 형태로)
                        numbers.append(target)
                        

make_numbers(number_list)
print(numbers)