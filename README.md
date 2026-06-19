# Blog Post: Isolating Zero-Shot Super-Resolution in Neural Operators

## Motivation: Zero-shot super-resolution
Resolution is important when considering data that describes a continuous function. Resolution determines the spatial grid - how often and at what intervals do we pick a point in order to represent the function. The neural operator AI model hypothesizes a zero-shot super-resolution [1]. This means that the neural operator, as described in the paper "Neural Operator: Learning Maps Between Function Spaces" [1], hypothetically should be able to be trained on low resolution data, and still perform when tested on a test set with a higher resolution. Standard neural networks on the other hand, have shown to require the exact same spatial grid under testing conditions in order to retain or approach their training performance. Neural operators actually attempt to learn the continuous mappings between function spaces, allowing the option to train the neural operator on a low-resolution spatial grid, but evaluate it on a high-resolution one. This generalization to denser grids is what is specifically called zero-shot super-resolution. It is an important concept, as achieving it would mean being able to train the neural operator much faster and just once, but still being able to use it for problems and datasets with spatial grids of different sizes. To validate zero-shot super-resolution, we must test a neural operator on the same problem, but with a spatial grid different than the one it was trained on.

## Problem: PDE datasets introduce confounding numerical errors
Existing evaluations use Partial Differential Equations (PDEs) like the Burgers' equation. Those PDEs lack exact mathematical or analytical solutions and require numerical solvers to generate the ground-truth dataset. The numerical solvers lead to approximation errors, which are different for the different spatial grids. As a consequance of that, testing a neural operator on a PDE with a different resolution mixes the actual neural operator error with the approximation error difference. We need to isolate the two errors to properly test zero-shot super-resolution.

## Proposed Control Dataset: A 1D integral
We propose a 1D dataset of an integral that has an analytical solution to isolate zero-shot super-resolution. The input function is a sine wave, while the output function is the exact integral of that wave. This integral has an exact mathematical solution, meaning that we will not encounter any error introduced by a numerical solver. Therefore a performance drop on higher-resolution datasets would be caused only by the neural operator failing to generalize, and would mean a failure at zero-shot super-resolution. This means that our dataset would provide a precise control test.

## Data Generation
The control dataset is generated for two different spatial grids. The generation happens via Python code using NumPy, and is later saved in a .mat file using SciPy. A subset of the points is also plotted via MatPlotLib to ensure that the data generation was successful. The training dataset consists of 800 samples generated at a low-resolution spatial grid of 64 points equally spread between x=0 and x=1. The testing dataset consists of 200 samples generated at a high-resolution spatial grid of 1024 points equally spread between x=0 and x=1. To be compatible with the existing neural operator codebases, the data is saved in a .mat format, containg the input array "a" and the output array "u". This matches the structure of the 1D Burgers' dataset used in "Neural Operator: Learning Maps Between Function Spaces".

## Examples
An example from our dataset maps a frequency-randomized sine wave to its integral:
### Input a: a(x) = sin(c * 2 * pi * x)
### Output u: u(x) = (1 - cos(c * 2 * pi * x)) / (c * 2 * pi) - the exact mathematical solution
Here, c is a random constant between 1 and 5.

A concrete example of input values when c=1 would be:
TODO

## Links
### Generation code: https://github.com/gdimitrovdev/neural-operator-control-dataset
### Train (grid size 64) and test (grid size 1024) datasets: https://doi.org/10.5281/zenodo.20754083

## References
[1] Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., & Anandkumar, A. (2021). Neural Operator: Learning Maps Between Function Spaces. arXiv preprint arXiv:2108.08481.
