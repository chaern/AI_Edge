arr1 = []
arr2 = []

for val in range(97, 123):
    arr1.append(chr(val)) # a ~ z

for val in range(12593, 12623):
    arr2.append(chr(val)) # ㄱ ~ ㅎ

print(f"chr(97) ~ chr(122) : {arr1}")
print(f"chr(12593) ~ chr(12622) : {arr2}")

print()

print(f"ord('a') ~ ord('z') : ", end="")
for val in arr1:
    print(ord(val), end=" ")


print()
print(f"ord('ㄱ') ~ ord('ㅎ') : ", end="")
for val in arr2:
    print(ord(val), end=" ")