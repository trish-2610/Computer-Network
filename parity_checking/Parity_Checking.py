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
