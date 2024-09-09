"""
❓ PROMPT
Given a vertex and edge list of users of a social network and two user IDs, return whether they are friends of friends.

Example(s)
users = ["Jeff", "Susan", "Ed", "Fred", "Jason", "Zach"]
friends = [("Jeff", "Susan"), ("Jeff", "Fred"), ("Susan", "Ed"), ("Ed", "Fred"), ("Jason", "Zach")]

Jeff---|
 |     |
Susan  |   Jason - Zach
 |     |
 Ed - Fred

isFOF(users, friends, "Jeff", "Ed") -> True
isFOF(users, friends, "Jeff", "Susan") -> False
isFOF(users, friends, "Jeff", "Jeff") -> False


🔎 EXPLORE
List your assumptions & discoveries:
It's a good idea to ask these questions in an interview.
Q: What should it return if the person is a direct friend or 3 degrees away?
A: False. This is for friends exactly 2 degrees away.

Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()


📆 PLAN
Outline of algorithm #:


🛠️ IMPLEMENT
function isFOF(vertex_list, edge_list, user1, user2) {
def isFOF(vertex_list: list[str], edge_list: list, user1: str, user2: str) -> bool:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.
"""
import collections
def isFOF(vertex_list: list[str], edge_list: list, user1: str, user2: str):

    graph = collections.defaultdict(list)
    q = collections.deque()

    visited = set()

    graph = {friend:[] for friend in vertex_list}
    for source , neighbor in edge_list:
        graph[source].append(neighbor)

    q.append(user1)
    visited.add(user1)

    level = 0
    while q and level<=2:
        level+=1
        for _ in range(len(q)):

            friend = q.popleft()

            fof = graph.get(friend)
            if not fof or len(fof)==0:
                continue

            for friend in fof:
                if friend in visited:
                    continue

                if level ==2 and friend==user2:
                    return  True

                else:
                    q.append(friend)
                    visited.add(friend)

    return False


users = ["Jeff", "Susan", "Ed", "Fred", "Jason", "Zach"]
friends = [
    ("Jeff", "Susan"),
    ("Jeff", "Fred"),
    ("Susan", "Ed"),
    ("Ed", "Fred"),
    ("Jason", "Zach")
]

# Jeff---|
#  |     |
# Susan  |   Jason - Zach
#  |     |
#  Ed - Fred

# Happy path
print(isFOF(users, friends, "Jeff", "Ed"))
print(isFOF(users, friends, "Ed", "Jeff"))
print(isFOF(users, friends, "Susan", "Fred"))
print(isFOF(users, friends, "Fred", "Susan"))

# Too close: Jason -> Zach (distance 1)
print(isFOF(users, friends, "Jason", "Zach"))

# Distance 1 or 3: Jeff -> Fred / Jeff -> Susan -> Ed -> Fred
print(isFOF(users, friends, "Jeff", "Fred") == False)

# Nonexistent path
print(isFOF(users, friends, "Zach", "Jeff") == False)
print(isFOF(users, friends, "Jeff", "Zach") == False)

# Users not in the network
print(isFOF(users, friends, "Foo", "Jeff") == False)
print(isFOF(users, friends, "Jeff", "Foo") == False)
print(isFOF(users, friends, "Foo", "Bar") == False)



users = ["Ben", "Emily", "Ana", "Chris", "John", "Jess", "Ken"]
friends = [
    ("Chris", "Ben"),
    ("Chris", "Emily"),
    ("Chris", "Ana"),
    ("Chris", "John"),
    ("Chris", "Jess"),
    ("Chris", "Ken"),
]

# Ben ---|  |--- Emily
# Ana -- Chris - John
# Jess --|  |--- Ken

print(isFOF(users, friends, "Ben", "Ana"))
print(isFOF(users, friends, "Ana", "Ben"))
print(isFOF(users, friends, "Jess", "Ana"))
print(isFOF(users, friends, "Emily", "Ben"))
print(isFOF(users, friends, "John", "Ken"))
print(isFOF(users, friends, "Ken", "Emily"))

print(isFOF(users, friends, "Chris", "Ben") == False)
print(isFOF(users, friends, "Chris", "Ana") == False)
print(isFOF(users, friends, "Chris", "Jess") == False)
print(isFOF(users, friends, "Chris", "Emily") == False)
print(isFOF(users, friends, "Chris", "John") == False)
print(isFOF(users, friends, "Chris", "Ken") == False)
print(isFOF(users, friends, "Ken", "Chris") == False)


users = ["Ben", "Emily", "Ana", "Tony", "Chris", "John", "Jess", "Ken"]
friends = [
    ("Tony", "Ben"),
    ("Tony", "Jess"),
    ("Tony", "Ana"),
    ("Tony", "Chris"),  # friend bridge
    ("Chris", "Emily"),
    ("Chris", "John"),
    ("Chris", "Ken"),
]

# Ben ---|        |---- Emily
# Ana - Tony -- Chris - John
# Jess --|        |---- Ken

print(isFOF(users, friends, "Chris", "Ben"))
print(isFOF(users, friends, "Chris", "Ana"))
print(isFOF(users, friends, "Chris", "Jess"))
print(isFOF(users, friends, "Tony", "Emily"))
print(isFOF(users, friends, "Tony", "John"))
print(isFOF(users, friends, "Tony", "Ken"))

# Distance 3
print(isFOF(users, friends, "Ben", "Emily") == False)
print(isFOF(users, friends, "Ana", "John") == False)
print(isFOF(users, friends, "Jess", "Ken") == False)