#! /bin/sh -e

# convert BrainWeb segmented data to PET input
# Do this using Linux utilities (as we don't want to rely on matlab or so)
# This is of course a bit crazy, but it works for here.

# BrainWEB labels:
#0=Background, 1=CSF, 2=Grey Matter, 3=White Matter, 4=Fat, 5=Muscle/Skin, 6=Skin, 7=Skull, 8=Glial Matter, 9=Connective

# First create the emission image
# We will use "tr" to replace the labels with other integers 
# (we have to use octal notation)
tr '\001\002\003\004\005\006\007\010\011' '\000\002\007\001\001\001\000\001\001' <phantom_1.0mm_normal_crisp.rawb  > preemission.rawb
# copy Interfile header
sed -e s/phantom_1.0mm_normal_crisp/preemission/ < phantom_1.0mm_normal_crisp.hv > preemission.hv
# zoom z-spacing to what we need for the forward projection
zoom_image emission.hv preemission.hv 211 1 0 0 15 0.148148148 -42.75

# Now create the attenuation image
# We will use "tr" to replace the labels with other integers 
# We have to use unsigned bytes, so we will set "tissue" to 2, and "skull" to 3,
# which is about the correct ratio for 511 keV
tr '\001\002\003\004\005\006\007\010\011' '\000\002\002\002\002\002\003\002\002' <phantom_1.0mm_normal_crisp.rawb  > preattenuation.rawb
# copy Interfile header
sed -e s/phantom_1.0mm_normal_crisp/preattenuation/ < phantom_1.0mm_normal_crisp.hv > preattenuation.hv

# zoom z-spacing to what we need for the forward projection
zoom_image preattenuation_zoomed.hv preattenuation.hv 211 1 0 0 15 0.148148148 -42.75

# now convert to cm^-1 ("tissue" will become 0.096)
# we have to take the zoom-factor into account for this
stir_math --including-first --times-scalar 0.048 --divide-scalar 6.75 attenuation.hv preattenuation_zoomed.hv

rm preemission.*v preattenuation*v

# zoom T1 image to same dimensions
zoom_image --template emission.hv T1.hv t1_icbm_normal_3mm_pn3_rf20.hv
