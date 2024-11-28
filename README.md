# Error Detection Techniques in Computer Networks

## Submitted By:
- **Trishansh Sahane**  
- **Vaidik Lotan**

### Under the Guidance of:
- **Mrs. Deepali Panwar**

## Acknowledgement:
We express our heartfelt gratitude to **Deepali Panwar Mam** for her invaluable guidance throughout this project. Her mentorship helped us deeply understand error detection techniques.

## Introduction:
This project focuses on exploring various error detection techniques used in computer
networks to ensure the accurate transmission of data. These methods play a critical role in
identifying and minimizing data errors during communication, enhancing data integrity, and
reliability in networking systems.

In this project we have written the python code for various Error Detection Techniques used
to detect errors.

### Objective:
- To study, understand, and implement different error detection techniques.
- To analyze their applications in real-world scenarios.

### GitHub Repository:
[GitHub - Computer Network](https://github.com/trish-2610/Computer-Network)

## Techniques Implemented

### 1. Parity Checking

**Definition**:  
Parity checking is a simple error-detection technique used in digital
communication and storage systems to ensure data integrity. It involves adding a parity bit
to data to make the total number of `1s` in the binary representation either even or odd,
depending on the type of parity. In this an extra bit ( Parity bit ) is added to each word before transmitting.

**Types of Parity Checking**:
- **Even Parity**: Ensures the total number of `1s` (including the parity bit) is even.  
  Example:
  ```
  Data: 1010
  Parity Bit: 1 (Total 1s = 4, even)
  Transmitted Data: 10101
  ```
- **Odd Parity**: Ensures the total number of `1s` (including the parity bit) is odd.  
  Example:
  ```
  Data: 1010
  Parity Bit: 0 (Total 1s = 3, odd)
  Transmitted Data: 10100
  ```

**How It Works**:
1. **Sender**: Calculates and appends the parity bit to the data before transmission.  
2. **Receiver**: Recalculates the parity. If it matches, the data is error-free; otherwise, an error is detected.

**Limitations**:
- Can only detect errors but cannot correct them.
- Ineffective for errors affecting an even number of bits.
- Unsuitable for complex systems.

**Applications**:
- Detecting RAM errors.
- Verifying data integrity in basic communication protocols and storage systems.

**Python Code for Parity Checking**:
```python
try:
    data = int(input("Enter data : "))
    print("Actual Data = ", data)

    if type(data) is int:

        def dec_bin(data):
            data = bin(data)
            data = str(data)
            data = str.split(data, "b")[1]
            return data

        data = dec_bin(data)

        print(data)

        def even_parity(data):
            updated_even_data = "0" + str(data)
            print(updated_even_data)
            ones_count = 0
            for i in updated_even_data:
                if i == "1":
                    ones_count += 1
            if ones_count % 2 == 0:
                print("Even Parity : NO ERROR")
            else:
                print("Even Parity : ERROR")

        def odd_parity(data):
            updated_odd_data = "1" + str(data)
            print(updated_odd_data)
            ones_count = 0
            for i in updated_odd_data:
                if i == "1":
                    ones_count += 1
            if ones_count % 2 != 0:
                print("Odd Parity : NO ERROR")
            else:
                print("Odd parity : ERROR")

        even_parity(data)
        odd_parity(data)

    else:
        print("Exception : Not an Integer")

except Exception:
    print("Exception : Not an Integer Value")
```

**Output**:
```
Enter data : 36
Actual Data =  36     
100100
0100100
Even Parity : NO ERROR
1100100
Odd Parity : NO ERROR
```
```
Enter data : 31
Actual Data =  31
11111
011111
Even Parity : ERROR
111111
Odd parity : ERROR
```

### 2. Checksum

**Definition**:  
Checksum is an error-detection technique used in digital communication and data storage systems to verify data integrity. It involves generating a small fixed-size value
(checksum) from a block of data and comparing it during transmission or storage to detect errors.

**How It Works**:
1. **Sender**: Calculates the checksum using an algorithm and appends it to the data.
2. **Receiver**: Recalculates and compares the checksum with the received one. Any mismatch indicates an error.

**Advantages**:
- Easy to implement and lightweight.
- Effective for detecting common errors like flipped bits.

**Limitations**:
- Cannot correct errors.
- May fail in cases where multiple errors cancel each other out.

**Applications**:
- Ensuring integrity in TCP/IP protocols.
- Verifying file integrity during transfers.

**Python Code for Checksum**:
```python
def transmitter():
    transmitted_lst = []
    while True:
        try:
            data = int(input("Enter Transmitted Data : "))
            if data == 0:
                break
            transmitted_lst.append(data)
        except:
            print("Not an Integer")
            break

    print(transmitted_lst)

    checksum_transmitted_data = 0
    for i in transmitted_lst:
        checksum_transmitted_data += i
    print(checksum_transmitted_data)
    return checksum_transmitted_data


def receiver():
    received_lst = []
    while True:
        try:
            data = int(input("Enter Received Data : "))
            if data == 0:
                break
            received_lst.append(data)
        except:
            print("Not an Integer")
            break

    print(received_lst)

    checksum_received_data = 0
    for i in received_lst:
        checksum_received_data += i
    print(checksum_received_data)
    return checksum_received_data


checksum_trans_data = transmitter()
checksum_rec_data = receiver()

Total = checksum_trans_data - checksum_rec_data

if Total == 0:
    print("No Error")
else:
    print("Error")
```

**Output**:
```
Enter Transmitted Data : 12
Enter Transmitted Data : 32
Enter Transmitted Data : 43
Enter Transmitted Data : 0
[12, 32, 43]
87
Enter Received Data : 12
Enter Received Data : 32
Enter Received Data : 43
Enter Received Data : 0
[12, 32, 43]
87
No Error
```
```
Enter Transmitted Data : 12
Enter Transmitted Data : 98
Enter Transmitted Data : 0
[12, 98]
110
Enter Received Data : 34
Enter Received Data : 5
Enter Received Data : 0
[34, 5]
39
Error
```

## Conclusion:
This project demonstrated the implementation of Parity Checking and Checksum methods for error detection, providing insights into their practical applications and limitations. 
