# Fitting ellipsoids to 3D grains in RVE
This repository discusses how we can fit a 3D ellipsoid to an arbitrary 3D shape for RVE evaluation. The idea of this method is mostly based on [this paper](https://doi.org/10.1016/S0191-8141(03)00093-2), so I would recommend reading it first (especially Appendix B). Here I extend that idea into fitting a 3D ellipsoid to an arbitrary 3D shape.

## Source data
The RVE data used in this evaluation is first analyzed from MTEX and generated from DREAM3D, which is stored in ```fit-ellipsoid/data``` for reference.

## Methodology
The report of the method is stored in ```fit-ellipsoid/report/Fitting an ellipsoid to an arbitrary 3D shape.pdf```, with detail explanation on the mathematical motivation of the method.

## Running the code
First, open Git Bash (on Windows, or just terminal on Linux) in a location you want to store the code and run (only for the first time):
```
git clone https://github.com/dinhtrung21/fit-ellipsoid.git
```
Then, on Git Bash we open VSCode to the folder:
```
code fit-ellipsoid
```
From this point we will work on VSCode terminal. Make sure that you have install Python for VSCode terminal, this can be easily checked by the command ```python3```. Then, we install the needed packages using this line:
```
pip3 install –r requirements.txt
```
Finally, the automatic evaluation process can be initiated by running ```evaluate.py``` from the command line as following:
```
python3 evaluate.py
```
After the first time, you can run the code straight from the terminal on Windows (PowerShell) without using Git Bash.

## Results
The results are stored in ```fit-ellipsoid/result``` for reference.

## Development
-  To adjust the RVE parameters or experimental constants, see ```evaluate.py```.
-  If you are interested in the algorithms of the fitting method, see ```ellipsoid.py```.
-  If you are interested in the algorithms of the Hellinger distance, see ```util.py```.
