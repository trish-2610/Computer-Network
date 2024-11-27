def transmitter():
    transmitted_lst = []
    while(True):
            try:
                data = int(input("Enter Transmitted Data : "))
                if(data == 0):
                    break
                transmitted_lst.append(data)
            except:
                print("Not an Integer")
                break

    print(transmitted_lst)

    checksum_transmitted_data= 0 
    for i in transmitted_lst:
        checksum_transmitted_data += i 
    print(checksum_transmitted_data)
    return checksum_transmitted_data

def receiver():
    received_lst = []
    while(True):
            try:  
                data = int(input("Enter Received Data : "))
                if(data == 0):
                    break
                received_lst.append(data)
            except:
                print("Not an Integer")
                break

    print(received_lst)

    checksum_received_data= 0 
    for i in received_lst:
        checksum_received_data += i 
    print(checksum_received_data)
    return checksum_received_data

checksum_trans_data = transmitter()
checksum_rec_data = receiver()

Total = checksum_trans_data - checksum_rec_data

if(Total == 0):
    print("No Error")
else :
    print("Error")



      