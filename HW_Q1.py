num_of_ip_bits = 32

# The function takes 2 arguments, IP address with three octets and subnet mask and does calculations on the subnet
def CalculatIpAddreses(given_ip, given_subnet_mask):
    num_of_bits_host = num_of_ip_bits - given_subnet_mask

    # Network address and Broadcast address aren't available host and can't be used as an endpoint
    num_of_available_hosts = 2 ** num_of_bits_host - 2
    num_of_endpoints = num_of_available_hosts

    # Convert subnet mask to binary subnet mask list
    binary_subnet_mask = '1' * given_subnet_mask + '0' * num_of_bits_host
    subnet_mask_list = []
    for i in range(0, len(binary_subnet_mask), 8):
        subnet_mask_list.append(binary_subnet_mask[i: i + 8])

    # Convert ip address to binary IP list
    given_ip = given_ip[0:-1]  # Remove last dot "."
    splitted_ip_octets = given_ip.split('.') + ['0']
    binary_ip_list = []
    for octet in splitted_ip_octets:
        binary_octet_ip = bin(int(octet))[2:].zfill(8)
        binary_ip_list.append(binary_octet_ip)

    # Network address calculation
    network_address_bin_list = []
    for mask_chunk, ip_chunk in zip(subnet_mask_list, binary_ip_list):
        network_address_bin_list.append(bin(int(mask_chunk, 2) & int(ip_chunk, 2))[2:].zfill(8))
    network_address = ConvertBinListToDotDecimal(network_address_bin_list)

    # Calculate first endpoint IP
    # It's the first address after the network address
    first_endpoint_bin_list = CalculateDesiredEndpointIP(network_address_bin_list, 1)
    first_endpoint_ip = ConvertBinListToDotDecimal(first_endpoint_bin_list)

    # Calculate complement of subnet mask in order to calculate broadcast IP address
    complement_subnet_mask_bin_list = []
    for mask_chunk in subnet_mask_list:
        complement_subnet_mask_bin_list.append(bin(255 - int(mask_chunk, 2))[2:].zfill(8))

    # Calculate broadcast IP address
    broadcast_address_bin_list = []
    for network_address_chunk, complement_mask_chunk in zip(network_address_bin_list, complement_subnet_mask_bin_list):
        broadcast_address_bin_list.append(
            bin(int(network_address_chunk, 2) | int(complement_mask_chunk, 2))[2:].zfill(8))
    broadcast_address = ConvertBinListToDotDecimal(broadcast_address_bin_list)

    # Calculate last endpoint IP
    # It's the address before the broadcast address
    last_endpoint_bin_list = CalculateDesiredEndpointIP(broadcast_address_bin_list, -1)
    last_endpoint_ip = ConvertBinListToDotDecimal(last_endpoint_bin_list)

    # Special case, where subnet mask == 31, in this case it's point-to-point connection,
    # the subnet has only 2 addresses, both are used for hosts
    if given_subnet_mask == 31:
        num_of_available_hosts = 2
        num_of_endpoints = 2
        first_endpoint_ip = network_address
        last_endpoint_ip = broadcast_address
        network_address = "There is no separate address reserved for network identification in" \
                          " a point-to-point connection with a /31 subnet mask"
        broadcast_address = "There is no broadcast address in a point-to-point connection with a /31 subnet mask"

    print("The numbers of available hosts in the subnet: ", num_of_available_hosts)
    print("The number of endpoints: ", num_of_endpoints)
    print("The network address: ", network_address)
    print("The First endpoint IP: ", first_endpoint_ip)
    print("The Last endpoint IP: ", last_endpoint_ip)
    print("The Broadcast IP address: ", broadcast_address)


# This function takes address as binary list and a number(distance from the given address) and returns
# the desired address as binary list
# Helps to calculate first and last endpoints to prevent code duplication
def CalculateDesiredEndpointIP(base_address_bin_list, desired_address_distance):
    base_address_binary = ''.join(base_address_bin_list)
    desired_endpoint_ip_int = int(base_address_binary, 2) + desired_address_distance
    desired_endpoint_ip_binary = bin(desired_endpoint_ip_int)[2:].zfill(num_of_ip_bits)
    desired_endpoint_ip_binary_list = []
    for i in range(0, len(desired_endpoint_ip_binary), 8):
        desired_endpoint_ip_binary_list.append(desired_endpoint_ip_binary[i: i + 8])
    return desired_endpoint_ip_binary_list


# Converts binary list to dot decimal string
def ConvertBinListToDotDecimal(given_binary_list):
    dot_decimal_list = []
    for chunk in given_binary_list:
        dot_decimal_list.append(str(int(chunk, 2)))
    dot_decimal_number = ".".join(dot_decimal_list)
    return dot_decimal_number

if __name__ == '__main__':
    print(" Input: '192.168.0.', 24 \n Output: ")
    CalculatIpAddreses('192.168.0.', 24)
    print("\n Input: '192.168.5.', 24 \n Output: ")
    CalculatIpAddreses('192.168.5.', 24)
    print("\n Input: '192.168.0.', 28 \n Output: ")
    CalculatIpAddreses('192.168.0.', 28)
    print("\n Input: '192.168.0.', 31 \n Output: ")
    CalculatIpAddreses('192.168.0.', 31)