def binary_sum(string,string1):
    sum = int(string,2) + int(string1,2)
    sum = bin(sum)
    return sum[2:]