import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Did not give all the required files")

    # TODO: Read database file into a variable
    data= []
    value=0
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        headerD ={header: value for header in headers[1:]}
        for row in reader:
            data.append(row)
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        _sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    found=False
    for h in headerD:
        temp=0
        i=0
        while i<len(_sequence):
            counter=0
            if h==_sequence[i:i+len(h)]:
                if i+len(h)<len(_sequence):
                    i+=len(h)
                else:
                    break
                found=True
                counter+=1
            while found:
                if h==_sequence[i:i+len(h)]:
                    if i+len(h)<len(_sequence):
                        i+=len(h)
                    else:
                        break
                    counter+=1
                else:
                    found=False
            if counter>temp:
                temp=counter
            i+=1
        headerD[h]=temp
    
    # TODO: Check database for matching profiles
    areEqual=True
    for row in data:
        areEqual=True
        temp=row["name"]
        for h in headerD:
            if int(row[h]) == headerD[h]:
                continue
            else:
                areEqual=False
                break
        if areEqual==True:
            return temp
    if areEqual==False:
        return "No match"


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


print(main())
