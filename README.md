# LRA-analysis
##### _Testing the denoising performance for spectroscopic dataset and how it affects the peak parameters_


----


#### Dependencies

- Python3, numpy, scipy, matplotlib

-----
Refer to the jupyter notebook file (.ipynb). Needs the dependency `lra_core.py` in `src` for execution.

-----

#### Description:

Low-rank approximation (LRA) (also known as SVD denoising) is widely used in signal processing for general denoising. Here, the denoising performance is analyzed with regard to spectroscopic dataset and how the approximated dataset from LRA is affected in terms of peak parameters, namely peak height, width, area and SNR. 

An objective filter for rank cutoff is used for retaining all spectral information.

-----

#### Discussed in :

["Posthandling Spectral Information Enhancement for Single Cell Raman Molecular Mapping Analysis" ](https://pubs.acs.org/doi/10.1021/acs.analchem.5c03915).


