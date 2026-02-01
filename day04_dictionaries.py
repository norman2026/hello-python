# Day 4 – Dictionaries

service_ports = {
    "http": 80,
    "https": 443,
    "ssh": 22
}

print(service_ports)

print("HTTP runs on port:", service_ports["http"])
print("SSH runs on port:", service_ports["ssh"])

# Add a new service
service_ports["ftp"] = 21

print("After adding ftp:", service_ports)

# Update an existing value
service_ports["ssh"] = 2222

print("After updating ssh:", service_ports)



print("\nService Ports:")

for keycounter, valuecounter in service_ports.items():
    print(f"Service: {keycounter} runs on port {valuecounter}")


servers = {
    "web01": "192.168.1.10",
    "db01": "192.168.1.20",
    "cache01": "192.168.1.30"
}

print("\nServer Inventory:")

for name, ip in servers.items():
    print(f"Server {name} has IP address {ip}")

print ("Now adding new server: backup01 with IP address 192.168.1.40")
servers["backup01"]= "192.168.1.40"

#Change the IP of "web01" to "10.0.0.10"
print("Changing the IP address of web01.")
servers["web01"]="10.0.0.10"
print("The Servers in the updated dictionary are:",servers)