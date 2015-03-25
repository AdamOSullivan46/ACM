for i in 1 10 100 1000 10000 100000 100000 1000000
do
    P1testGen.py "$i" > P1inGen.txt
    printf "%d elements:\n" "$i"
    printf "Python:"
    time python3 P1.py < P1inGen.txt
    printf "C:"
    time P1 < P1inGen.txt
    printf "\n\n"
done
