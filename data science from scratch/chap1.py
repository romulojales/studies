from collections import Counter

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
    users[i]["friends"].append(j)
    users[j]["friends"].append(i)


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


def friends_of_friends(user):
    friends_of_friends = []
    for friend in user["friends"]:
        friends_of_friend = users[friend]["friends"]
        for fof in friends_of_friend:
            if user["id"] != fof and fof not in user["friends"]:
                friends_of_friends.append(fof)
    return friends_of_friends


print("Friends of Friends of user 0:", friends_of_friends(users[0]))


def not_the_same(user, other_user):
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    return other_user["id"] not in user["friends"]


def friends_of_friends_ids(user):
    return Counter(friends_of_friends(user))


print(friends_of_friends_ids(users[3]))
