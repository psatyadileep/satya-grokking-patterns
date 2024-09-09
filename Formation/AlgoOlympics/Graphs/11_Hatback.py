'''
❓ PROMPT
Oliver the Dog is missing his favorite hat and is asking his friends at the dog park if they've seen it. Each dog either has seen it or suggests a list of other dogs to ask. Return the name of the dog who has seen the hat. Oliver starts out by asking his best friend. This function will take two parameters. The first is a map of dogs to a list of their friends. The second is Oliver's best friend, who Oliver will ask first.

One of the most common uses of a queue is to keep a list of "work to be done". Just like doing housework, often new things get added to the to-do list while doing some other task. New jobs get added to the end of the queue, and when one is complete, the next one is taken from the top of the list.

As a follow-up, how would you handle it when there's circular knowledge? For example, Jono's suggestion is to ask Angus, and Angus' suggestion is to ask Jono. These 'cycles' aren't restricted to pairs of dogs, they can be of any size.

Example(s)
dogs = {
  'Carter': ['Fido', 'Ivy'],
  'Ivy': ["HAT"], // Ivy has seen the hat
  'Loki': ['Snoopy'],
  'Pepper': ['Carter'],
  'Snoopy': ['Pepper'],
  'Fido': []
}
findHat(dogs, 'Loki') == 'Ivy'


🔎 EXPLORE
List your assumptions & discoveries:


Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()


📆 PLAN
Outline of algorithm #:


🛠️ IMPLEMENT
function findHat(dogs, bestFriend) {
def findHat(dogs: dict, bestFriend: str) -> str:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

import collections
def findHat(dogs: dict, bestFriend: str) -> str:

    q = collections.deque()

    visited = set()


    q.append(bestFriend)
    visited.add(bestFriend)


    while q:
        for i in range (len(q)):
            friend = q.popleft()

            friends = dogs.get(friend)

            if not friends or len(friends)==0:
                continue


            for related in friends:
                if related == "HAT":
                    return friend

                if related in visited:
                    continue

                q.append(related)
                visited.add(related)

    return "Couldn't find the hat"



dogs = {
    'Carter': ['Fido', 'Ivy'],
    'Ivy': ["HAT"], # Ivy has seen the hat
    'Loki': ['Snoopy'],
    'Pepper': ['Carter'],
    'Snoopy': ['Pepper'],
    'Fido': []
}
print(findHat(dogs, 'Loki') == "Ivy")
print(findHat(dogs, 'Snoopy') == "Ivy")
print(findHat(dogs, 'Ivy') == "Ivy")
print(findHat(dogs, 'Fido') == "Couldn't find the hat")

dogs = {
    'Ariel': ['Bork'],
    'Bork': ['Cassie'],
    'Cassie': ['Drex'],
    'Drex': ['Zoe'],
    'Zoe': ["HAT"],
}
print(findHat(dogs, "Ariel") == "Zoe")
print(findHat(dogs, "Bork") == "Zoe")
print(findHat(dogs, "Cassie") == "Zoe")
print(findHat(dogs, "Drex") == "Zoe")
print(findHat(dogs, "Zoe") == "Zoe")