#!/bin/bash

function do_test() {
    echo "threads=$threads rampup=$rampup loops=$loops" 
    rm -v "result/result_"$threads"_"$loops"_"$rampup".jtl"
    jmeter "-Jthreads=$threads" "-Jrampup=$rampup" "-Jloops=$loops" -n -t pod_contacts_generic.jmx -l "result/result_"$threads"_"$loops"_"$rampup".jtl" 
    sleep 10
}

#threads=1   ; rampup=1   ;  loops=1   ; do_test
#threads=5   ; rampup=1   ;  loops=1   ; do_test
threads=10  ; rampup=1   ;  loops=10  ; do_test
#threads=50  ; rampup=1   ;  loops=10  ; do_test
#threads=65 ; rampup=60   ;  loops=10  ; do_test
#threads=70 ; rampup=60   ;  loops=10  ; do_test
#threads=75 ; rampup=60   ;  loops=10  ; do_test
#threads=77 ; rampup=60   ;  loops=10  ; do_test
#threads=79 ; rampup=60   ;  loops=10  ; do_test
#threads=80 ; rampup=60   ;  loops=10  ; do_test
#threads=85 ; rampup=60   ;  loops=10  ; do_test
#threads=90 ; rampup=60   ;  loops=10  ; do_test
#threads=100 ; rampup=1   ;  loops=10  ; do_test
#threads=100 ; rampup=1   ;  loops=50  ; do_test
#threads=500 ; rampup=1   ;  loops=10  ; do_test
#threads=50  ; rampup=60  ;  loops=10  ; do_test
#threads=100 ; rampup=60  ;  loops=10  ; do_test
#threads=100 ; rampup=60  ;  loops=50  ; do_test
#threads=500 ; rampup=60  ;  loops=10  ; do_test



