# Pi Estimator: Monte Carlo Method

## Overview
This Python program estimates the value of $\pi$ using the Monte Carlo method. By randomly generating points within a square and checking whether they fall inside an inscribed circle, the program calculates an approximation of $\pi$. The estimate improves as the number of points increases.

## Concept and Formula
1. **Setup**:
   - The square has side length $2r$, and the circle has radius $r$, with the circle perfectly inscribed in the square.
   - The area of the square is $4r^2$, and the area of the circle is $\pi r^2$.

2. **Monte Carlo Method**:
   - Random points $(x, y)$ are generated within the square, where $x, y \in [-r, r]$.
   - A point is considered inside the circle if it satisfies $x^2 + y^2 \leq r^2$.

3. **Estimation of $\pi$**:
   - The ratio of points inside the circle ($N_\text{circle}$) to the total number of points ($N_\text{total}$) is approximately equal to the ratio of the circle's area to the square's area:
     $\frac{N_\text{circle}}{N_\text{total}} \approx \frac{\pi}{4}$
   - Rearranging, we estimate $\pi$ as:
     $\pi \approx 4 \cdot \frac{N_\text{circle}}{N_\text{total}}$

## Control Flow and Description
1. **Random Point Generation**:
   - Points are generated randomly within the square's bounds.

2. **Classification**:
   - Each point is classified as either inside the circle or outside the circle based on the condition $x^2 + y^2 \leq r^2$.

3. **Estimation**:
   - $\pi$ is calculated using the formula:
     $\pi \approx 4 \cdot \frac{N_\text{circle}}{N_\text{total}}.$
   - As the number of points ($N_\text{total}$) increases, the estimate converges toward the true value of $\pi$, though fluctuations may occur.

4. **Visualization**:
   - A graph displays the randomly generated points, showing their distribution within the square and the circle.
   - Another graph tracks:
     - The total number of trials ($N_\text{total}$).
     - The number of points inside the circle ($N_\text{circle}$).
     - The number of points outside the circle ($N_\text{total} - N_\text{circle}$).
     - The running estimate of $\pi$.

## GUI
The figure below shows a screenshot of the GUI at runtime. It includes:
- A graphical representation of the points distributed in the square and circle.
- Real-time statistics, including:
  - Number of points generated.
  - Points inside the circle.
  - Points outside the circle.
  - The current estimate of $\pi$.
  
<p align="center">
<img src="https://i.imgur.com/qcfEd5d.png" width="800">
</p>

## Notes
- The accuracy of the estimate improves as more points are generated.
- Results may vary slightly due to the stochastic nature of the method.
