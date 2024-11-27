checksum = 36
data = int(input("Enter data : "))
print("Actual Data = ",data)

if(type(data) is int) :
    def dec_bin(data):
            data = bin(data)
            data = str(data)
            data = str.split(data,"b")[1]
            return data 

    data = dec_bin(data)

    print(data,type(data))
    
    n_data = data[2:]
    print(n_data)
    new = data[0:2]
    print(new)

    a = int(n_data)
    b = int(new)

    print(a,type(a))
    print(b,type(b))

    binary_like_integer = a # Treated as a decimal integer by Python
    decimal_value = int(str(binary_like_integer), 2)  # Convert to a decimal integer
    print(decimal_value) 
    binary_like_integer1 = b # Treated as a decimal integer by Python
    decimal_value1 = int(str(binary_like_integer1), 2)  # Convert to a decimal integer
    print(decimal_value1) 

    data1 = dec_bin(decimal_value)
    print(data1)
    data11 = int(data1)
    
    data2 = dec_bin(decimal_value1)
    print(data2)
    data22 = int(data2)

    res = data11 |data22
    print(res)
    binary_like_integer = res # Treated as a decimal integer by Python
    decimal_value = int(str(binary_like_integer), 2)  # Convert to a decimal integer
    print(decimal_value)
    print(~decimal_value)
    

   