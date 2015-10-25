#! /bin/sh
mkdir -p working_folder
mkdir -p working_folder/randoms
cp EX_randoms/* working_folder/randoms
cd working_folder/randoms
construct_randoms_from_singles true_randoms.hs true_singles template_sinogram_span1.hs 1

poisson_noise my_randoms.hs true_randoms.hs 1 1

find_ML_singles_from_delayed estimated_singles my_randoms.hs  5

construct_randoms_from_singles estimated_randoms.hs estimated_singles template_sinogram_span1.hs 5


cd ../..
