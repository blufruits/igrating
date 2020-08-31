# Instagram Rating

This repository exists purely to aid my learning of Python. The pyplot module from the matplotlib library is requried.

Background knowledge:

In Instagram you to follow others, and for others to follow you. It tends to be the case that these two values are not the same, the main culprit being celebrities and other famous indiviuals who do not follow back (this could be you). This is an an undesireable state to be in.
One way of remedying this (except for unfollowing famous people) is by following 'mutual' people. I will define these 'mutal' people as being people who follow you back. By following 'mutal' people your follower + following metrics will become more similar, which is what you want.

What the code does:

The code has two objectives - to display your current Instagram rating and to show (using pyplot) how this will evolve as you follow more 'mutal' accounts. The Instagram rating is simply a measure of how similar/dissimlar followed and following are. This is a ratio between followed and following (or the reciprocal of this if followed>following).

Mathematics:

All the script does is plot f(n) = (A+n)/(B+n) with A,B and the range of n being defined by the user. A,B,n ∈ Z*





