d = int(input("d:"))


b = ""
while d:
    b+=str(d%2)
    d //= 2

print(b[::-1])