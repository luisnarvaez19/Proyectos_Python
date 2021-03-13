# The following statements create the two Blur nodes (Blur1 and Blur2) and assign them to variables b1 and b2.
b1 = nuke.nodes.Blur()
b2 = nuke.nodes.Blur()
# The following assigns the size control of the Blur1 node to the variable k1.
k1 = b1['size']
# The following three statements animate the control assigned to k1. At frame 30, its value is set to 10. At frame 40, it’s set to 20.
k1.setAnimated()
k1.setValue(10, time = 30)
k1.setValue(20, time = 40)
# The following assigns the size control of the Blur2 node to the variable k2.
k2 = b2['size']
# The following copies the animation curve from k1 (size on Blur1) to k2 (size on Blur2).
k2.copyAnimations(k1.animations())
