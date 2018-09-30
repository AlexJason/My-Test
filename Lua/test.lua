if global.hasPassed == nil then
	global.hasPassed = false
end
script.on_event(defines.events.on_tick, function(event)
	local tick = event.tick
	if global.hasPassed then
		return
	end
	if tick > 0xed4e00 then
		global.hasPassed = true
		func()
	end
end)