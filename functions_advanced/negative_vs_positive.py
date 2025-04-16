nums = [int(el) for el in input().split()]

positives = [el for el in nums if el > 0]
negatives = [el for el in nums if el < 0]
total_sum_positives = sum(positives)
total_sum_negatives = sum(negatives)
print(total_sum_negatives)
print(total_sum_positives)
if abs(total_sum_negatives) > total_sum_positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
