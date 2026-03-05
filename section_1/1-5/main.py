# Get age as an integer
#print(f'Type an age of the movie viewer')
age = int(input())

message = None

if age >= 18:
    message= "You can watch any movie"
    print(message)
    exit

else:
    # Get parental guidance as a boolean (True/False)
    #print(f"Are you within guidance from a parental advisor, father or mother")
    with_parent = input() == "true"

    if with_parent:
        message = "You can watch PG-13 movies"
    else:
        message = "You can only watch G-rated movies"

    # Don't change below this line
    print(message)
