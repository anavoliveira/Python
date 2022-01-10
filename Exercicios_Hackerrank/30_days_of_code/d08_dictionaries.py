# Enter your code here. Read input from STDIN. Print output to STDOUT

phone_book = { }

n = int(input())

for i in range(0, n):
    name, phone_number = input().split(' ')
    phone_book[name]=phone_number

for j in range(0,n):
    i=input()
    if i in phone_book:
        print(f'{i}={phone_book[i]}')
    else:
        print('Not found')
  