# Instagram Rating
This partly exists to aid my learning of Python. As a result of this there are some comments that will not be useful to others. The pyplot module from the matplotlib library is requried.

Background knowledge:

In Instagram you follow others and others follow you. It tends to be the case that these two values are not the same, the main culprit being celebrities and other famous individuals who do not follow back (this could be you). This is an an undesireable state to be in.
One way of remedying this (except by unfollowing famous people) is by following 'mutual' people. These 'mutal' people follow you back. By following 'mutal' people your follower + following metrics will become more similar, which is what you want.

What the code does:

The code has two objectives - to display your current Instagram rating and to show (using pyplot) how this will evolve as you follow more 'mutal' accounts. The Instagram rating is simply a measure of how similar/dissimlar followed and following are. This is a ratio between followed and following (or the reciprocal of this if followed>following).

Mathematics:

The script plots f(n) = (A+n)/(B+n) with A,B and the domain of f being defined by the user. A,B,n ∈ N





