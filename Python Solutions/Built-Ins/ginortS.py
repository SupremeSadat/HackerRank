arr = input()
sorted(arr)

lettersCaps = [x for x in arr if not x.isdigit() and x.isupper()]
lettersnoCaps = [x for x in arr if not x.isdigit() and x.islower()]
digits = [x for x in arr if x.isdigit() and int(x)%2 == 0]
digitsodd = [x for x in arr if x.isdigit() and int(x)%2 == 1]
arr = sorted(lettersnoCaps) + sorted(lettersCaps) + sorted(digitsodd) + sorted(digits)
print(*arr,sep="")