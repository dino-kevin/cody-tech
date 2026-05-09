def get_capital(country_capitals: dict, country_name: str):
    # Write code here
    return country_capitals[country_name]
country_capitals = {"France": "Paris", "Japan": "Tokyo"}
single_capital = get_capital(country_capitals, "France")
print(f"{single_capital}")
