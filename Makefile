simulate:
	-rm TrapAC.x_axis.out
	-rm TrapAC.y_axis.out
	-rm TrapAC.z_axis.out
	-rm TrapDC.z_axis.out
	python3 geo_write.py
	python3 Axes_write.py
	scuff-static < args_xAC
	scuff-static < args_yAC
	scuff-static < args_zAC
	scuff-static < args_zDC
	python3 Plot.py

show:
	python3 geo_write.py
	scuff-analyze --geometry TrapDC.scuffgeo --WriteGMSHFiles
	gmsh TrapDC.pp

mesh:
	gmsh Rod.stl -2 -format msh2
	mmgs -hausd 0.1 Rod.msh

