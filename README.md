# README

This is a set of code designed to characterise a Paul trap geometry and then predict the parameters that lead to stable trapping.
For use in the Swansea University Optomechanics lab, this is very early work.

## Files
Here is a brief explanation of what each file is/does. We start by going through the <code>.py</code> files.
1) <code>Axes_Write.py</code>: This will write a number of <code>.dat</code> files containing the points in Cartesian coordinates where we want to measure the electrostatic potential.
2) <code>Charge_Estimate.py</code>: This will estimate the charge on the particle from a given trap frequency. Results are given in $C kg^{-1}$, $C$, and number of elementary charges.
3) <code>geo_write.py</code>: This will write two <code>.scuffgeo</code> files. One for the AC voltages, and one for the DC voltages. These files describe the geometric transformations of the <code>Rod.o.msh</code> file to make the trap we have designed. They are identical in content but have different names to differentiate the SCUFF-EM output files.
4) <code>Paschen_Law.py</code>: I couldn't find a nice simple graph that showed the Paschen curve in nice units. This plots a graph whose x axis is in mBar m.
5) <code>Plot.py</code>: This reads in the <code>.out</code> files that SCUFF-EM outputs and finds the geometric factors $\alpha_r^{\text{AC}}$, $\alpha_z^{\text{AC}}$, and $\alpha_z^{\text{DC}}$.
6) <code>Stability.py</code>: Plots the Stability diagram and lets you change the values with sliders.

### Makefile
We also have a <code>Makefile</code>. This contains a number of commands that can be used to simulate the trap and calculate the geometric factors. I give the commands in the suggested order to run them.
1) <code>make mesh</code>: This takes <code>Rod.stl</code> and converts it into <code>Rod.o.msh</code> which SCUFF-EM can work with. By changing the number in the second line (<code>mmgs -hausd 0.1 Rod.msh</code>) you can change the mesh density. Smaller numbers make more triangles (The number is the max distance from the re-meshed version and the 'perfect' original <code>.stl</code> file).
2) <code>make show</code>: This runs <code>geo_write.py</code> to ensure the relevant <code>.scuffgeo</code> files exist and then shows what the trap looks like using gmsh.
3) <code>make simulate</code>: The last step. This removes all <code>.out</code> files from SCUFF-EM (the files append and do not overwrite without this step). Then it ensures that the write <code>.dat</code> files exist by running <code>Axes_Write.py</code>. When all the necessary files exist, it runs SCUFF-EM for each axis and relevant excitations using the various <code>args</code> files. Finally, we plot the potentials and prints the values for each geometric factor.

### Other Files
There are a number of other files necessary, this is a drief description of them.
1) various <code>args</code> files: There contain the names of files that SCUFF-EM uses when simulating the relevant data.
2) <code>dims.txt</code>: This contains the trap dimensions in mm.
3) <Rod.stl</code>: The mesh for the rod that will be used as the RF and DC electrodes. This is meshed in the centre of the coordinate axis and copied and moved by the <code>.scuffgeo</code> files.
4) Various <code>.out</code> and <code>.pp</code> files: The outputs of SCUFF-EM.
5) <code>VAC.Excitations</code> and <code>VDC.Excitations</code>: The potential in each set of electrodes when calculating the electrostatic field.
