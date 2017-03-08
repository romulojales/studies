users = [{"id": 0, "name": "Hero"},
         {"id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"},
         {"id": 4, "name": "Thor"},
         {"id": 5, "name": "Clive"},
         {"id": 6, "name": "Hicks"},
         {"id": 7, "name": "Devin"},
         {"id": 8, "name": "Kate"},
         {"id": 9, "name": "Klein"}]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[0]["friends"].append(users[j])


def number_of_friends(user):
    return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users)

print("Total Connections", total_connections)

num_of_users = len(users)

print("Number of users", num_of_users)

avg_connections = total_connections / num_of_users

print("Average of connections", avg_connections)

num_of_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

print("Number of friends by id", num_of_friends_by_id)

sorted(num_of_friends_by_id, key=lambda x: x[1], reverse=True)

print("Number of friends by id ordered", num_of_friends_by_id)
