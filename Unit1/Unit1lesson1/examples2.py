# beatles = ("John", "Paul", "George", "Ringo")
# for b in beatles:
#     print(b)

# actors = {
#     "Kyle MacLachlan": "Dale Cooper",
#     "Sheryl Lee": "Laura Palmer",
#     "Lara Flynn Boyle": "Donna Hayward",
#     "Sherilyn Fenn" : "Audrey Horne"
# }

# for a in actors:
#     print actors[a]

# for a in actors.values():
#     print a

# for key, value in actors.iteritems():
#     print value


# Try it!
# Use a while loop to solve the following
# problem: A slow, but determined, walker
# sets off from Leicester to cover the
# 102 miles to London at 2 miles per hour.
# sets off from London heading to Leicester
# going at 1 mile per hour. Where do they meet?

a,b  = 0,102
aplus, bplus = 2,1
while a!=b:
    a, b = a+aplus, b-bplus
else:
    print("They meet at " + str(a) + " miles.")
