import os


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

    print("Transmitted Data:", transmitted_lst)

    checksum_transmitted_data = sum(transmitted_lst)
    print("Checksum of Transmitted Data:", checksum_transmitted_data)

    # Save data to a file to send to the receiver
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data.txt")
    with open(file_path, "w") as f:
        f.write(" ".join(map(str, transmitted_lst)) + "\n")
        f.write(str(checksum_transmitted_data))


if __name__ == "__main__":
    transmitter()
