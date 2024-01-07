# Admin No: 210455E, Name: Brandon Poon, Tutorial Group: IT2653-01

bookingRecords = [
    {'Package Name': 'Skating', 'Customer Name': 'Brandon', 'No. of Pax': '1', 'Cost per Pax': 10},
    {'Package Name': 'USS', 'Customer Name': 'Isaac', 'No. of Pax': '6', 'Cost per Pax': 5},
    {'Package Name': 'Bungee', 'Customer Name': 'Zachary', 'No. of Pax': '2', 'Cost per Pax': 9},
    {'Package Name': 'Golf', 'Customer Name': 'Darrek', 'No. of Pax': '7', 'Cost per Pax': 4},
    {'Package Name': 'Waterpark', 'Customer Name': 'Yu Xun', 'No. of Pax': '3', 'Cost per Pax': 8},
    {'Package Name': 'Zoo', 'Customer Name': 'Kenneth', 'No. of Pax': '8', 'Cost per Pax': 3},
    {'Package Name': 'Diving', 'Customer Name': 'Alvin', 'No. of Pax': '4', 'Cost per Pax': 7},
    {'Package Name': 'Chinatown', 'Customer Name': 'Vannsar', 'No. of Pax': '9', 'Cost per Pax': 2},
    {'Package Name': 'Cruise', 'Customer Name': 'Rachel', 'No. of Pax': '5', 'Cost per Pax': 6},
    {'Package Name': 'Garden', 'Customer Name': 'Bryan', 'No. of Pax': '10', 'Cost per Pax': 1}]


# Algorithms


# Bubble Sort
def bubbleSort(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j]['Customer Name'] > theSeq[j + 1]['Customer Name']:
                # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp


def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        smallNdx = i
        for j in range(i + 1, n):
            if theSeq[j]['Package Name'] < theSeq[smallNdx]['Package Name']:
                smallNdx = j
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp


# Sorts a sequence in ascending order using
# the insertion sort algorithm
def insertionSort(theSeq):
    n = len(theSeq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = theSeq[i]
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value['Cost per Pax'] < theSeq[pos - 1]['Cost per Pax']:
            # Shift the items to the right during the search
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
            # Put the saved value into the open slot.
            theSeq[pos] = value


def sequentialSearch(theValues):
    while True:
        target = input('What customer are you searching for? : ')
        n = len(theValues)
        for i in range(n):
            # If the target is in the ith element, return True
            if theValues[i]['Customer Name'].upper() == target.upper():
                print('{:>15} | {:>15} | {:>15} | {:>15}'.format('Package Name', 'Customer Name', 'No. of Pax', 'Cost per Pax'))
                print('{:>15} | {:>15} | {:>15} | {:>15}'.format(theValues[i]['Package Name'], theValues[i]['Customer Name'], theValues[i]['No. of Pax'], theValues[i]['Cost per Pax']))
                change = input('Would like to update this customer? (Y/N): ')
                if change.upper() == 'Y':
                    while True:
                        print('Previous Package Name:', theValues[i]['Package Name'])
                        newPName = input('New Package Name (Leave blank if none) : ')
                        if newPName.isalpha():
                            theValues[i]['Package Name'] = newPName
                            break
                        elif newPName == '':
                            break
                        else:
                            print('Customer Name must be in alphabets.')
                    while True:
                        print('Previous Customer Name:', theValues[i]['Customer Name'])
                        newCName = input('New Customer Name (Leave blank if none) : ')
                        if newCName.isalpha():
                            theValues[i]['Customer Name'] = newCName
                            break
                        elif newCName == '':
                            break
                        else:
                            print('Customer Name must be in alphabets.')

                    while True:
                        print('No. of Pax:', theValues[i]['No. of Pax'])
                        newPax = input('New No. of Pax (Leave blank if none): ')
                        if newPax.isdecimal():
                            theValues[i]['No. of Pax'] = newPax
                        elif newPax == '':
                            break
                        else:
                            print('Number of pax must be a number.')


                    while True:
                        print('Cost per Pax:', theValues[i]['Cost per Pax'])
                        newCost = input('New Cost per Pax (Leave blank if none): ')
                        if newCost.isdecimal():
                            theValues[i]['Cost per Pax'] = newCost
                        elif newCost == '':
                            break
                        else:
                            print('Cost per pax must a number.')

                    print('-----------------------------------------------------------------------')
                    print('Updated Customer Record.')
                    print('{:>15} | {:>15} | {:>15} | {:>15}'.format('Package Name', 'Customer Name', 'No. of Pax',
                                                                     'Cost per Pax'))
                    print('{:>15} | {:>15} | {:>15} | {:>15}'.format(theValues[i]['Package Name'],
                                                                     theValues[i]['Customer Name'],
                                                                     theValues[i]['No. of Pax'],
                                                                     theValues[i]['Cost per Pax']))
                    return

                elif change.upper() == 'N':
                    action = input('Returning you to menu...')
                    return
                else:
                    print('Please enter a valid option.')

        action = input('Customer not found. Returning you to menu...')


def binarySearch(theSeq):
    target = input('What package are you searching for?: ')
    n = len(theSeq)
    fNo = 0
    lNo = n - 1
    display()
    while fNo <= lNo:
        mNo = (fNo + lNo) // 2
        mValue = theSeq[mNo]['Package Name']
        print(mValue)
        if mValue.upper() == target.upper():
            print('{:>15} | {:>15} | {:>15} | {:>15}'.format('Package Name', 'Customer Name', 'No. of Pax','Cost per Pax'))
            print('{:>15} | {:>15} | {:>15} | {:>15}'.format(theSeq[mNo]['Package Name'], theSeq[mNo]['Customer Name'], theSeq[mNo]['No. of Pax'], theSeq[mNo]['Cost per Pax']))

            change = input('Would like to update this package? (Y/N): ')
            if change.upper() == 'Y':
                while True:
                    print('Previous Package Name:', theSeq[mNo]['Package Name'])
                    newPName = input('New Package Name (Leave blank if none) : ')
                    if newPName.isalpha():
                        theSeq[mNo]['Package Name'] = newPName
                        break
                    elif newPName == '':
                        break
                    else:
                        print('Customer Name must be in alphabets.')
                while True:
                    print('Previous Customer Name:', theSeq[mNo]['Customer Name'])
                    newCName = input('New Customer Name (Leave blank if none) : ')
                    if newCName.isalpha():
                        theSeq[mNo]['Customer Name'] = newCName
                        break
                    elif newCName == '':
                        break
                    else:
                        print('Customer Name must be in alphabets.')

                while True:
                    print('No. of Pax:', theSeq[mNo]['No. of Pax'])
                    newPax = input('New No. of Pax (Leave blank if none): ')
                    if newPax.isdecimal():
                        theSeq[mNo]['No. of Pax'] = newPax
                    elif newPax == '':
                        break
                    else:
                        print('Number of pax must be a number.')

                while True:
                    print('Cost per Pax:', theSeq[mNo]['Cost per Pax'])
                    newCost = input('New Cost per Pax (Leave blank if none): ')
                    if newCost.isdecimal():
                        theSeq[mNo]['Cost per Pax'] = newCost
                    elif newCost == '':
                        break
                    else:
                        print('Cost per pax must a number.')

                print('-----------------------------------------------------------------------')
                print('Updated Package Record.')
                print('{:>15} | {:>15} | {:>15} | {:>15}'.format('Package Name', 'Customer Name', 'No. of Pax',
                                                                 'Cost per Pax'))
                print('{:>15} | {:>15} | {:>15} | {:>15}'.format(theSeq[mNo]['Package Name'],
                                                                 theSeq[mNo]['Customer Name'],
                                                                 theSeq[mNo]['No. of Pax'],
                                                                 theSeq[mNo]['Cost per Pax']))
                return

            elif change.upper() == 'N':
                action = input('Returning you to menu...')
                return
            else:
                print('Please enter a valid option.')
        elif mValue.upper() > target.upper():
            lNo = mNo - 1
        else:
            fNo = mNo + 1

    action = input('No package found. Returning you to menu...')


def quickSort(theSeq):
    n = len(theSeq)
    if n <= 1:
        return theSeq
    else:
        pivot = theSeq.pop(n - 1)

    items_greater = []
    items_lower = []

    for item in theSeq:
        if item['Cost per Pax'] > pivot['Cost per Pax']:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


def display():
    print('{:>15} | {:>15} | {:>15} | {:>15}'.format('Package Name', 'Customer Name', 'No. of Pax', 'Cost per Pax'))
    for record in bookingRecords:
        print('{:>15} | {:>15} | {:>15} | {:>15}'.format(record['Package Name'], record['Customer Name'],
                                                         record['No. of Pax'], record['Cost per Pax']))


while True:
    print('-----------------------------------------------------------------------')
    print('1. Display all records')
    print('2. Sort record by Customer Name using Bubble sort')
    print('3. Sort record by Package Name using Selection sort')
    print('4. Sort record by Package Cost using Insertion sort')
    print('5. Search record by Customer Name using Linear Search and update record')
    print('6. Search record by Package Name using Binary Search and update record')
    print('7. List records range from $X to $Y. e.g $100-200')
    print('8. Search record by Package Cost using Quick Sort (BONUS)')
    print()

    sortOption = input('Please select one option: ')

    if sortOption == '1':
        display()

    elif sortOption == '2':
        bubbleSort(bookingRecords)
        display()

    elif sortOption == '3':
        selectionSort(bookingRecords)
        display()

    elif sortOption == '4':
        insertionSort(bookingRecords)
        display()

    elif sortOption == '5':
        sequentialSearch(bookingRecords)

    elif sortOption == '6':
        selectionSort(bookingRecords)
        binarySearch(bookingRecords)

    elif sortOption == '7':
        while True:
            fNo = input('First No: ')
            if fNo.isdecimal():
                lNo = input('Last No: ')
                if lNo.isdecimal() and lNo > fNo:
                    insertionSort(bookingRecords)
                    print('{:>15} | {:>15} | {:>15} | {:>15}'.format('Package Name', 'Customer Name', 'No. of Pax', 'Cost per Pax'))
                    for record in bookingRecords:
                        if int(fNo) <= record['Cost per Pax'] <= int(lNo):
                            print('{:>15} | {:>15} | {:>15} | {:>15}'.format(record['Customer Name'], record['Package Name'], record['No. of Pax'], record['Cost per Pax']))
                    break
        action = input('Returning you to menu...')

    elif sortOption == '8':
        bookingRecords = quickSort(bookingRecords)
        print('{:>15} | {:>15} | {:>15} | {:>15}'.format('Package Name', 'Customer Name', 'No. of Pax', 'Cost per Pax'))
        for record in bookingRecords:
            print('{:>15} | {:>15} | {:>15} | {:>15}'.format(record['Package Name'], record['Customer Name'],
                                                             record['No. of Pax'], record['Cost per Pax']))
    else:
        print('-----------------------------------------------------------------------')
        print('Please enter an option from 1 to 8.')
