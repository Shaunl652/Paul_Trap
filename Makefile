simulate:
	-rm TrapAC.u_axis.out
	-rm TrapAC.v_axis.out
	-rm TrapAC.z_axis.out
	-rm TrapDC.z_axis.out
	python3 geo_write.py
	python3 Axes_write.py
	scuff-static < args_uAC
	scuff-static < args_vAC
	scuff-static < args_zAC
	scuff-static < args_zDC
	python3 Plot.py

show:
	python3 geo_write.py
	scuff-analyze --geometry TrapAC.scuffgeo --WriteGMSHFiles
	gmsh TrapAC.pp

mesh:
	gmsh Endcap.stl -2 -format msh2
	gmsh Rod.stl -2 -format msh2
	mmgs -hausd 50 Endcap.msh
	mmgs -hausd 50 Rod.msh

Surface:
	-rm TrapAC.plane.out
	python3 Axes_write.py
	python3 Plane_axes.py
	scuff-static < args_Plane
	python3 Plot_Surf.py
