import hashlib

hash_table = list([i for i in range(10)])

def get_key(data):
    return hash(data)
#hash(값) 하면 hash 함수가 값에 맞는 키값을 출력해줌 
def hash_function(data):
    return data % 8

def save_data(data,value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]
"""
save_data("min","55346038")
save_data("janet","37452546")
print(read_data("min"))
print(read_data("janet"))
print(hash_table)

pp = list([i for i in range(10)])
pp.append(["m",0])
pp.append(["p",1])
print(pp)
print(pp[10][0],pp[11])
"""

dataa = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(dataa)
hex_dig = hash_object.hexdigest()
print(hex_dig)
