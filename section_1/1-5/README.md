# Program Instructions: Movie Eligibility Based on Age and Parental Guidance

## Objective
Write a program that determines eligibility for a movie based on age and parental guidance.

## Steps

1. **Create a variable `age`**  
   - Assign it a value from input (given).

2. **Create a variable `with_parent`**  
   - Assign it a `True`/`False` value from input (given).  
   - **Note:** The input will be the string `"true"` or `"false"` (lowercase).

3. **Create a variable `message`**  
   - Initialize it with the value `"None"` (given).

4. **Use nested if-else to determine the value of `message`:**
   - If `age` is **18 or older**:  
     - Set `message` to `"You can watch any movie"`.
   - If `age` is **under 18**:  
     - If `with_parent` is **True**:  
       - Set `message` to `"You can watch PG-13 movies"`.
     - If `with_parent` is **False**:  
       - Set `message` to `"You can only watch G-rated movies"`.

