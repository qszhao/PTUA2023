for ((i=0;i<10;i++))
do
    if ((array[i]%2==0))
    then
        even=$((array[i]+even))
    else 
        odd=$((array[i]+odd))
    fi
done
