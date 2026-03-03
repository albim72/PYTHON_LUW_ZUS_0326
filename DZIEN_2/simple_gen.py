
import dis

def count_to(n):
    for i in range(1,n+1):
        yield i

print(count_to(19))
print(list(count_to(19)))

for number in count_to(6):
    print(number)

print(dis.dis(count_to))
