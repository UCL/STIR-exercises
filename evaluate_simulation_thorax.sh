#! /bin/sh

for g in 1 2; do

  cd working_folder/GATE${g}

  for s in prompts randoms scatter; do
    n=${s}_g${g}
    echo "extracting segments and creating profiles for $n"
    # Extract segment
    # Note that we use some scripting trickery (IO re-direction) to
    # void extract_segments asking questions and writing output.
    echo 1|extract_segments my_${n}.hs >/dev/null 2>&1
    # Store profile in a text file 
    list_image_values  profile_${n}.txt my_${n}seg0_by_sino.hv 4 4 -95 95 0 0
  done

  cd ../..

done
echo "Done"

