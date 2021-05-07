import random 
data = random.sample(range(100), 10)
print(data)

v = len(data);
def sum(v):
    if v <= 0:
        return data[v]

    return data[v] + sum(v-1)

print(sum(v-1))

def sum_list(data):
    if len(data) == 1:
        return data[0]
    return data(len(data-1)) + sum_list()

print(sum_list(data))
