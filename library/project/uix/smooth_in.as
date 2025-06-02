# Set up values
render.modify $f(1) position.smoothing 3
render.modify $f(1) sprite.ghost.smoothing 3
# Y tampering
render.get $f(1) position.y.current temp.y # gets the y pos of the object
render.modify $f(1) position.y.goal $v(temp.y) # sets the target y to the current y pos
variable.operation temp.y - 30 # changes the y var to move down 1
render.modify $f(1) position.y.current $v(temp.y) # teleports the object to modified Y
# Sets the ghost to 100 and shows the sprite, to later show it again
render.modify $f(1) sprite.ghost.current 100
render.modify $f(1) sprite.visible true
render.modify $f(1) sprite.ghost.to 0
