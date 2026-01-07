from logic import compare_services

print("AWS Compute Service Referee Tool")

budget = input("Enter budget (low/medium/high): ")
scalability = input("Scalability need (low/high): ")
management = input("Management preference (minimal/full): ")

results = compare_services(budget, scalability, management)

print("\nComparison Results:")
for item in results:
    print("-", item)
