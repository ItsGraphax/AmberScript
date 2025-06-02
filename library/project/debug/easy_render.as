render.new $f(1) $f(2) 0 0
render.modify $f(1) sprite.visible true
render.modify $f(1) position.smoothing 10
render.smoothmove $f(1) $r(-240,240) $r(-180,180)
render.modify $f(1) sprite.ghost.smoothing 10