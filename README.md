# Pi-estimator---Monte-Carlo-method
This python program estimates the value of Pi by randomly generating points (monte carlo) within certain bounds and calculating the ratio of total points to those that fell within certain parameters.

Random points (xy co-ordinates) are generated within a square. Within that square is a circle. The diameter of the circle is equal to the length
of one side of the square. An estimate of Pi is calculated with the following formula:
Pi is approximately equal to 4 * (Ninner/Ntotal)
where Ninner is the number of points generated that fell within the bounds of the circle and Nouter is the total number of points generated.
As more points are generated, the estimate of Pi tends closer and closer to its true value (allowing for fluctuations).
The graph of these points is displayed on one axis. In another axis, the following values are displayed:
the number of trials (points generated), the number of points inside the circle, the number of points outside the circle and the estimate of Pi.

The 'monte carlo method' refers to the use of random trial and error to perform some form of analysis, in this case, the value of Pi. This program
serves as a demonstration of a (somewhat trivial) application of the monte carlo method, rather than as an efficient method of calculating Pi.
