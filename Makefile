simulate:
	-rm TrapAC.x_axis.out
	-rm TrapAC.y_axis.out
	-rm TrapAC.zAC_axis.out
	-rm TrapDC.zDC_axis.out
	python3 geo_write.py
	python3 Axes_write.py
	scuff-static < args_xAC
	scuff-static < args_yAC
	scuff-static < args_zDC
	python3 Plot.py

show:
	python3 geo_write.py
	scuff-analyze --geometry TrapDC.scuffgeo --WriteGMSHFiles
	gmsh TrapAC.pp

mesh:
	gmsh Endcap.stl -2 -format msh2
	gmsh Rod.stl -2 -format msh2
	mmgs -hausd 0.01 Endcap.msh
	mmgs -hausd 0.1 Rod.msh

Surface:
	-rm TrapAC.plane.out
	python3 Axes_write.py
	python3 Plane_axes.py
	scuff-static < args_Plane

Planes:
	python3 Plane_axes.py
	-rm TrapAC.xy_plane.out
	-rm TrapAC.xz_plane.out
	-rm TrapAC.yz_plane.out
	scuff-static < args_xyplane
	scuff-static < args_xzplane
	scuff-static < args_yzplane
