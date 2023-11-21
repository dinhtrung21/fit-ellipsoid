# Multiphase RVE evaluation by fitting ellipsoids to 3D grains
This repository discuss how we can fit a 3D ellipsoid to an arbitrary 3D shape for RVE evaluation. The idea of this method is mostly based on [this paper](https://doi.org/10.1016/S0191-8141(03)00093-2), so I would recommend reading it first (especially Appendix B). Here I extend that idea into fitting a 3D ellipsoid to an arbitrary 3D shape.

## Running the code
Run the file by first open Git Bash (on Windows, or just terminal on Linux) in a location you want to store the code and run:

```
git clone https://github.com/dinhtrung21/fit-ellipsoid.git # Only for the first run
pip3 install –r requirements.txt                           # NumPy, Matplotlib, SciPy
python3 evaluate.py
```
## Methodology
The report of the method is stored in ```fit-ellipsoid/report/Fitting an ellipsoid to an arbitrary 3D shape.pdf```, with detail explanation on the mathematical motivation of the method.

## Results
The results are stored in ```fit-ellipsoid/result``` for reference.
