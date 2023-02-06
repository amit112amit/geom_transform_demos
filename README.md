# ME F318 CAD Geometric Transformations

This Github repository contains a collection of Jupyter notebooks to demonstrate different types of geometric transformations.

## How to use?

Click on the link / badge below to access this repository in a live Binder environment where you can run the notebooks.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amit112amit/geom_transform_demos/HEAD)

## About the Projective Transform demo

1. Elation is the 2D geometric transformation represented by the following matrix in homogeneous coordinates

$$
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
v_1 & v_2 & v
\end{bmatrix}
$$

2. In the demo, the original points and lines are shown in gray. Under the action of the elation matrix, the points are projected to the red points that lie in a 3D plane whose equation is $z = v_1 x + v_2 y + v$.

3. The final result of the projective transformation, shown in blue,  are obtained by modifying the homogeneous coordinates of the red-points such that their third coordinate is 1. This is equivalent to projecting them to $z = 1$ plane. If we join the blue points with their red counterparts, we will get lines which converge at the origin i.e. origin is the point of projection.

3. Go to the following link: ![https://www.geogebra.org/calculator/bhmuz5zh](https://www.geogebra.org/calculator/bhmuz5zh) to see the Geogebra demo.
