
# input: x1 = position, x2 = velocity
# math model:  f = x2' + a*x2 + b*x1
# state equations:
#       x2' = -a*x2 - b*x1 + f
#       x2 = x1'
# matrix format:
#        xX'  =    A *  x  + B * u
#       [x1'] = [ 0  1][x1]+[0]  f
#       [x2'] = [-b -a][x2] [1]

# Output equations:
#       y1 = x1
#       y2 = x2
# matrix format:
#        yX  =   C * x  + B * u
#       [y1] = [1 0][x1]+[0]  f
#       [y2] = [0 1][x2] [0]
print("start")