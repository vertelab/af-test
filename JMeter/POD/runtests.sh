#!/bin/bash
rm *.jtl
for fn in *.jmx; do
    jmeter -n -t "$fn" -l "autores/${fn%.*}.jtl"
    sleep 10
done
