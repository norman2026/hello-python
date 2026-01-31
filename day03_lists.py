#Day 3 lists

tools = ["git","docker", "linux", "python"]
print("This prints the list verbatim:")
print(tools)

print("Now for the 1st item in the list tool:", tools[0])
print("Now for the Second item in list tool:", tools[1])


tools.append("kubernetes")
print("After append:", tools)

tools.remove("linux")
print("After remove:", tools)

print("\nMy DevOps tools:")

for tool in tools:
    print("I am learning:", tool)
tools.sort()
print("\nSorted tools list:", tools)

servers = ["web01", "db01", "cache01"]

print("\nServer list:")

for server in servers:
    print(f"Pinging server: {server}")

