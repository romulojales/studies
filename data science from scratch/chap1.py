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

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(j)
    users[j]["friends"].append(i)


def number_of_friends(user):
    return len(user["friends"])


def friends_of_friends(user):
    friends_of_friends = []
    for friend in user["friends"]:
        friends_of_friend = users[friend]["friends"]
        for fof in friends_of_friend:
            if user["id"] != fof and fof not in user["friends"]:
                friends_of_friends.append(fof)
    return friends_of_friends


def not_the_same(user, other_user):
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    return other_user["id"] not in user["friends"]


def friends_of_friends_ids(user):
    return Counter(friends_of_friends(user))


num_of_users = len(users)
total_connections = sum(number_of_friends(user) for user in users)

avg_connections = total_connections / num_of_users

num_of_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

sorted(num_of_friends_by_id, key=lambda x: x[1], reverse=True)

print("Total Connections", total_connections)

print("Number of users", num_of_users)

print("Average of connections", avg_connections)

print("Number of friends by id", num_of_friends_by_id)

print("Number of friends by id ordered", num_of_friends_by_id)

print("Friends of Friends of user 0:", friends_of_friends(users[0]))

print(friends_of_friends_ids(users[3]))
