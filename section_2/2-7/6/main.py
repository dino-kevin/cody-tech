# Read input for the three matches
match1 = {"Alice", "Bob", "Charlie", "Diana"}
match2 = {"Charlie", "Diana", "Eve", "Frank"}
match3 = {"Alice", "Diana", "Frank", "George"}

# 1. Find players who participated in all three matches
find_participated_players_in_all_matches = list(sorted(match1.intersection(match2, match3)))

# 2. Find players who participated in exactly two matches
find_players_in_matches_repeated = set.union(match1.intersection(match2), match2.intersection(match3), match3.intersection(match1))
players_not_in_matches_repeated = set.union(find_players_in_matches_repeated.difference(match1), find_players_in_matches_repeated.difference(match2), find_players_in_matches_repeated.difference(match3))
players_in_only_two_matches = list(sorted(players_not_in_matches_repeated))

# 3. Find players who participated in only one match
find_only_one_player_peer_match = list(sorted(match1.difference(match2, match3) ^ match2.difference(match1, match3) ^ match3.difference(match1, match2)))

# 4. Count total unique players
total_unique_players = (len(match1.union(match2, match3)))

# 5. Find players in Match 1 only
find_only_one_player = list(sorted(match1.difference(match2, match3)))

# Print results in the specified format
print(f"Players in all matches: {(find_participated_players_in_all_matches)}")
print(f"Players in exactly two matches: {(players_in_only_two_matches)}")
print(f"Players in only one match: {(find_only_one_player_peer_match)}")
print(f"Total unique players: {(total_unique_players)}")
print(f"Players in Match 1 only: {(find_only_one_player)}")
