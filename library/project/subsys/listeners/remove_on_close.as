condition.eval $v(system.app.current) = $l(1) temp.eval
condition.eval $v(temp.eval) not _ temp.eval
branch.if $v(temp.eval) lib.uix.smooth_out $@()
branch.if $v(temp.eval) lib.tools.stop_listener $@().app_listener
