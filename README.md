# ZOLA-3D-M290

This repository utilize the Macro codes, i.e.ImageJ Macro Language IJM, of ImageJ APP, i.e., Fuji, to apply the ZOLA plug-in on M290 beam shaping machine, i.e., InShaPe dataset to do phase retrieval for the LCOS-SLM phase of M290 machine by fitting on the beam shapes using the Newton-Raphson Maximum Possion Likelihood Estimation MLE method.


1, First, create subfolders "bench", "gaussian", "ring", "rectophat", "tophat", and "tear" in the folder "/InShaPe TestSet/".

2, Download the test set for each beam shape from the original InShaPe dataset: https://doi.org/10.6084/m9.figshare.27650703.v2

3, Download the Fiji JAVA APP in the folder "/Fiji.app/": https://imagej.net/software/fiji/downloads

4, Run the .ijm Macro scripts in the folder "/ZOLA Macros scripts/", e.g., "/ZOLA Macros scripts/FinalOpt-ZOLA/chair-opt.ijm" to start the Newton-Raphson fitting on the test set of the corresponding beam shape and save the fitted beam shapes in the folder e.g., " /psf_bench/" +d2s(i, 0)+ ".tif". Please note that the PSF folders need to be created by yourself in the working directory of the .ijm scripts. Meanwhile, the fitting process will be logged in the json files and the .txt files in log folders like "TXTanalysis-opt-RI=1.6".


The original paper of ZOLA-3D:

Aristov, A., Lelandais, B., Rensen, E., & Zimmer, C. (2018). ZOLA-3D allows flexible 3D localization microscopy over an adjustable axial range. Nature communications, 9(1), 1-8.

DOI: https://doi.org/10.1038/s41467-018-04709-4


The original paper of the original InShaPe dataset and the design of M290's beam shaping optical system:

Yan, S., Off, R., Yayak, A. B., Wudy, K., Aghajani-Talesh, A., Birg, M., ... & Meratnia, N. (2025). Deep learning based phase retrieval with complex beam shapes for beam shape correction. Optics Express, 33(5), 10806-10834.

DOI: https://doi.org/10.1364/OE.547138
