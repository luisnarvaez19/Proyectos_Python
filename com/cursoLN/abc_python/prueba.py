## lopping ten times using _
for _ in range(5):
    print(_)

## iterating over a list using _
## you can use _ same as a variable
languages = ["Python", "JS", "PHP", "Java"]
for _ in languages:
    print(_)

_ = 5
while _ < 10:
    print(_, end = ' ') # default value of 'end' id '\n' in python. we're changing it to space
    _ += 1