#!/bin/bash

echo 'WELCOME'

echo 'please input 1st 4-bit number'
read first

if echo $first | grep -v "[10]" > /dev/null;then

    echo 'not binary number !!! '
    exit
fi



echo 'please input 2nd 4-bit binary number '
read second

if echo $second | grep -v "[10]" > /dev/null;then

    echo 'not binary number !!! '
    exit
fi

#BY DEFAULT THIS CODE ADDS ADDITIONAL ZEROS TO THE LEFT IF NEEDED 
binOut=$( echo $((  $(echo "ibase=2;$first" | bc) + $( echo "ibase=2;$second" | bc )  )) )


echo "obase=2;$binOut" | bc







