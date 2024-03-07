companies = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
companies_list = companies.split(",")
print(f"{len(companies_list)} companies in the list")
companies_list.sort(reverse=True)
print(companies_list)

companies_with_o = []
for company in companies_list:
    if 'o' in company.lower():
        companies_with_o.append(company)

print("Number of companies names with letter ‘o’:", len(companies_with_o))

companies_without_i = []
for company in companies_list:
    if 'i' not in company.lower():
        companies_without_i.append(company)

print("Number of companies names without letter ‘i’:", len(companies_without_i))

# Bonus
new_companies = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

unique_companies_set = set(new_companies)

unique_companies_list = list(unique_companies_set)

unique_companies_list.sort()

unique_companies_string = ", ".join(unique_companies_list)

print("Unique companies without duplicates:", unique_companies_string)
print("Number of companies now in the list:", len(unique_companies_list))

# Bonus 2
unique_companies_list.sort()

reversed_names = [company[::-1] for company in unique_companies_list]

print("List of manufacturers in ascending order with reversed letters:", reversed_names)

