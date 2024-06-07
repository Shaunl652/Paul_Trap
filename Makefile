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
	scuff-analyze --geometry TrapAC.scuffgeo --WriteGMSHFiles
	gmsh TrapAC.pp

mesh:
	gmsh Endcap_top.stl -2 -format msh2
	gmsh Endcap_bottom.stl -2 -format msh2
	gmsh RF_Upper.stl -2 -format msh2
	gmsh RF_Lower.stl -2 -format msh2
	mmgs -hausd 0.3 Endcap_top.msh
	mmgs -hausd 0.3 Endcap_bottom.msh
	mmgs -hausd 0.3 RF_Upper.msh
	mmgs -hausd 0.3 RF_Lower.msh

Surface:
	-rm TrapAC.plane.out
	python3 Axes_write.py
	python3 Plane_axes.py
	scuff-static < args_Plane
	
