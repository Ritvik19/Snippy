import hashlib 
  
str = "String"

result = hashlib.md5(str.encode()) 
  
print(f"The hexadecimal equivalent of hash is : result.hexdigest()")