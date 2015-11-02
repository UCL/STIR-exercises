#! /bin/sh
mkdir -p working_folder
mkdir -p working_folder/randoms
rsync -auv EX_randoms/* working_folder/randoms
cd working_folder/randoms
construct_randoms_from_singles mean_randoms.hs true_singles template_sinogram_span1.hs 1

poisson_noise my_randoms.hs mean_randoms.hs 1 1

# generate file with text to tell next command that we don't want to display results,
# but have output at every iteration
cat <<EOF > input_parameters.txt
0
1
1
EOF
find_ML_singles_from_delayed estimated_singles my_randoms.hs  15 < input_parameters.txt

construct_randoms_from_singles estimated_randoms.hs estimated_singles my_randoms.hs 5


cd ../..
