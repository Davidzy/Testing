string = raw_input()
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
def whether_palindrome(s):
    odd_times = 0
    d = {}
    #count char in s
    for s1 in s:
        if s1 in d:
            d[s1] += 1
        else:
            d[s1] = 1
    for k in d:
        if d[k] % 2 > 0: odd_times += 1
    if odd_times > 1:
        return False
    else: return True

found = whether_palindrome(string)
if not found:
    print("NO")
else:
    print("YES")
