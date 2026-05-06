# Define file paths
allow_list_file = "allow_list.txt"
remove_list_file = "remove_list.txt"

# Read IPs from the allow list
with open(allow_list_file, "r") as file:
    ip_addresses = file.read().split()

# Read IPs from the remove list
with open(remove_list_file, "r") as file:
    remove_list = file.read().split()

# Remove IPs found in the remove list
for ip in remove_list:
    if ip in ip_addresses:
        ip_addresses.remove(ip)

# Write the updated IPs back to the file
with open(allow_list_file, "w") as file:
    file.write("\n".join(ip_addresses))

print("✅ Allow list successfully updated.")