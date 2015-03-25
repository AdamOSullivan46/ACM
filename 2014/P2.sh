for i in 1 10 100 1000
do
    for j in 1 10 100
    do
        P2testGen.py "$i" "$j" > P2inGen.txt
        printf "%d i, %d j:\n" "$i" "$j"
        printf "Python:"
        timeout 1 python3 P2.py < P2inGen.txt
        printf "\n\n"
    done
done
