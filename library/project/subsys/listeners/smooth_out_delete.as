render.get $@() sprite.ghost.current temp.ghost
condition.eval temp.ghost > 99 temp.eval
branch.if $v(temp.eval) lib.tools.stop_listener $@().uix.smooth_out_delete
branch.if $v(temp.eval) lib.tools.delete_object $@()
