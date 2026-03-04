n = int(input())
def create_star_row(rows: int):
        if rows:
            return str("*" * (rows) + "\n")
        else: 
            return ""

def calculate_star_rows (n: int):
    new_star_rows = ""
    for i in range(1, n + 1, 2):
            new_star_rows += (create_star_row(i))
    return new_star_rows

final_star_rows = calculate_star_rows(n)
print(final_star_rows)