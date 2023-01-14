# Revealing the similarity between urban transportation networks and optimal transport-based infrastructures

By Daniela Leite and Caterina De Bacco

**What is Opt-urban Nextrout about?** - This project uses a method inspired by optimal transport theory to generate networks that show similarity with the structure of real public transportation networks. By taking in input a set of latitude-longitude coordinates, our algorithm outputs a network structure that represents the optimal topology connecting such points. 

Our inputs correspond to real origin-destination station coordinates across multiple cities. We  then measure similarities between the existing structures and the outputs of our algorithm by computing different metrics. More details can be found at: 

- [_Revealing the similarity between urban transportation networks and optimal transport-based infrastructures_](https://arxiv.org/abs/2209.06751) (currently under review). If you use this software please cite this work.

## Prerequisites

We use the approach described in [_Nextrout_](https://github.com/Danielaleite/Nextrout), which requires the following dependencies:

	* A Fortran compiler (any gfortran version>4 but version 5);
 	* Blas and Lapack libraries;
 	* Python 3;	
 	* Meshpy;
    * Click;
    * Numpy v<1.19;
    * f90wrap; 

## Installation

**Linux/OSX**

If all dependencies are installed, you just need to clone this repository:

```
git clone https://github.com/Danielaleite/opt-urban-nextrout
cd opt-urban-nextrout
python setup.py
```

This will download and install "_Nextrout_" and all required python dependencies. If you have any issues with the installation of `Nextrout`, feel free to reach me out.  =)

The execution of `setup.py` takes a few minutes to complete (dont't panic if you notice it's taking a while). After that, you should find the following folders:

* **code**
* **data**

Inside **code** you will find the **Nextrout** folder, which contains:

* **dmk_utilities**
* **nextrout_core**

Inside **dmk_utilities** there are all the files related to the DMK solver. These are needed to execute **NextRout**. In **nextrout_core**, you will find the main python scripts and subfolders where the entire procedure takes place. In case of errors during installation, please visit [_DMK solver_](https://gitlab.com/enrico_facca/dmk_solver), section **Troubleshooting**. 


## How to perform a simulation?

You can simply check our [_tutorial_] (https://github.com/Danielaleite/opt-urban-nextrout/blob/master/code/opt_urban_nextrout_tutorial.ipynb)

## Contributing

We appreciate any help or suggestions for further improvement. Do not hesitate to contact us in case you want to contribute or have any questions.
