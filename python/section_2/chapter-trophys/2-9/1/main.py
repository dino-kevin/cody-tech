def calculate_average_score(scores:list):
    # Write code here
    if scores:
        total_score = sum(scores)
        average_score = float(total_score / len(scores))
        return average_score
    else:
        return 0

# Test data
scores = [95,85,76,89,100,92,67]
average_score = calculate_average_score(scores)
print(average_score)

