# set up values
render.modify $f(1) position.smoothing 3
render.modify $f(1) sprite.ghost.smoothing 3
# get current y pos and modify it
render.get $f(1) position.y.current temp.y
variable.operation temp.y - 30
# move the object
render.modify $f(1) position.y.goal $v(temp.y)
# start ghost anim
render.modify $f(1) sprite.ghost.to 100
# start listener
listener.start $f(1).uix.smooth_out_delete $f(1) tick lib.subsys.uix.smooth_out_delete
