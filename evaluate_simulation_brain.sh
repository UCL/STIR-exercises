#! /bin/sh -e

  cd working_folder/brain

  for s in prompts randoms; do
    n=${s}
    echo "extracting segments and creating profiles for $n"
    # Extract segment
    # Note that we use some scripting trickery (IO re-direction) to
    # void extract_segments asking questions and writing output.
    echo 1|extract_segments my_${n}.hs >/dev/null 2>&1
    # Store profile in a text file 
    list_image_values  profile_${n}.txt my_${n}seg0_by_sino.hv 4 4 -42 42 0 0
  done

  cd ../..

echo "Done"

