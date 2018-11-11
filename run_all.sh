#! /bin/sh -e
# A script that runs all other scripts...
# This would be useful to generate all output data, and then evaluate it all afterwards.
#
# Author: Kris Thielemans

# Note that the scripts need to be executed in some order, so we try to do that here.

for script in ./run_simulation*sh  ./run_scatter_[013].sh ./run_MCIR*.sh ./run_randoms.sh
do
    echo ""
    echo "============================================================"
    echo "Running $script"
    $script
done


for data in brain thorax SPECT
do
    case ${data} in
        brain)
            data_folder=working_folder/${data}
            ;;
        thorax)
            data_folder=working_folder/single_slice
            ;;
        SPECT)
            data_folder=working_folder/single_slice_SPECT
            ;;
    esac
    
    for method in "" _MAP _PSF _PLS
    do
        script=./run_reconstruction_${data}${method}.sh
        if [ -r ${script} ]; then
            echo ""
            echo "============================================================"
            echo "Running $script (no noise)"
            $script

            # now do this with noise
            for scaling_factor in 0.5 1 2
            do
                ./run_generate_Poisson_${data}.sh ${scaling_factor}
                echo "============================================================"
                echo "Running $script (noise scaling factor ${scaling_factor})"
                $script
                # copy files
                rsync -aC --exclude noise_\* ${data_folder}/*.* ${data_folder}/noise_${scaling_factor}/
            done
            # restore noiseless data
            rsync -aC --exclude noise_\* ${data_folder}/noiseless/*.* ${data_folder}/
        fi
    done
done


echo ""
echo "All done!"

