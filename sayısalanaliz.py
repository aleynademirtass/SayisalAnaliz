import math
a=math.pi/5
x=math.cos(a)
y=math.cos(0)-(math.sin(0)*(a-0))
birlikesme=x-y
print('bir terimli taylor seri acilimindaki kesme hatasi:',birlikesme)
z=math.cos(0)-(math.sin(0)*(a-0))-(math.cos(0)*a*a/2)
ikilikesme=x-z
print('iki terimli taylor seri acilimindaki kesme hatasi:',ikilikesme)