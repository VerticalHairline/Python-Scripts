balls = ([1,23], [1,3,4])

balls2 = [x.copy() for x in balls]

balls2.append("hi")

balls2[0].append("hi")
