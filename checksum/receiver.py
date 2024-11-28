import os


def receiver():
    # Read data from the file saved by the transmitter
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "data.txt")
        with open(file_path, "r") as f:
            lines = f.readlines()
            received_lst = list(map(int, lines[0].strip().split()))
            checksum_transmitted_data = int(lines[1].strip())
    except FileNotFoundError:
        print("Data file not found. Please run the transmitter first.")
        return

    print("Received Data:", received_lst)

    checksum_received_data = sum(received_lst)
    print("Checksum of Received Data:", checksum_received_data)

    # Verify the checksum
    if checksum_transmitted_data == checksum_received_data:
        print("No Error")
    else:
        print("Error")


if __name__ == "__main__":
    receiver()
