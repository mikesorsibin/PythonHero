def ran_check(num,low,high):
    if num in range(low,high):
        print(f"{num} is in range of {low} and {high}")
    else:
        print(f"{num} not in range")

ran_check(2,1,9)
ran_check(2,3,9)


def ran_check_bool(num,low,high):
    return num in range(low,high)

print(ran_check_bool(2,1,9))
print(ran_check_bool(2,3,9))
        
