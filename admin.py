# Import the json module to allow us to read and write data in JSON format.
import json


# This function repeatedly prompts for input until an integer is entered.
def inputInt(prompt):
    while True:
        try:
            intInput = int(input(prompt))
            if intInput <= 0:
                print('Please enter integer greater than zero')
            else:
                break
        except ValueError:
            print('Invalid input!! Please enter an integer.')
    return intInput


# This function repeatedly prompts for input until something (not whitespace)
# is entered.

def inputSomething(prompt):
    while True:
        dataInput = input(prompt)
        if dataInput == '':

            print('Please enter something')
        else:
            break
    return dataInput.strip()


# This function opens "data.txt" in write mode and writes the data to it in
# JSON format.
def saveChanges(dataList):
    f = open('data.txt', 'w')
    json.dump(dataList, f)
    f.close()
    print('Changes saved')


def main():
    try:
        f = open('data.txt', 'r')
        data = json.load(f)
        f.close()
    except:
        print('Error!!! File not found')
        data = []

    print('Welcome to the Admin Program.')

    while True:
        print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
        choice = input('> ').lower()

        # Add a new menu item.
        if choice == 'a':
            movieName = inputSomething('Enter movie name: ')
            year = inputInt('Enter release year: ')
            duration = inputInt('Enter duration: ')
            genres = input('Enter genres: ')

            dict = {'name': movieName, 'year': year, 'duration': duration, 'genres': genres, }
            data.append(dict)
            saveChanges(data)


        # List the current menu items.
        elif choice == 'l':
            if len(data) == 0:  # if the list is empty, show empty list message
                print('Data not found.')

            else:  # otherwise, loop through the list and show each item
                print('List of movies :')
                listNum = 1
                for item, Name in enumerate(data):
                    print(listNum, ')', Name['name'])
                    listNum += 1



        # Search the current menu items.
        elif choice == 's':
            search = (inputSomething('Type a movie name to search:')).lower()
            count = 0
            # search.lower()
            if len(data) == 0:
                print('No data found')
            else:
                for item, Name in enumerate(data):

                    if (search in Name['name'].lower()):
                        count += 1
                        print(count, Name['name'])


        # View a menu item.
        elif choice == 'v':
            if len(data) == 0:
                print('No data Saved')

            else:
                while True:
                    listNum = inputInt('Menu movie number  : ')
                    try:
                        movie = data[listNum - 1]
                        print(movie['name'])
                        print('year: ', movie['year'])
                        print('duration: ', movie['duration'])
                        print('genres: ', movie['genres'])
                        break
                    except IndexError:
                        print('Invalid Index Number! Please enter an integer')


        # Delete a menu item.
        elif choice == 'd':
            if len(data) == 0:
                print('No data found')
            else:

                while True:
                    listNum = inputInt('Menu item number to delete: ')
                    try:
                        del data[listNum - 1]
                        f = open('data.txt', 'w')
                        saveChanges(data)
                        f.close()
                        print('Menu item deleted.')


                    except IndexError:
                        print('Invalid number! Please enter an integer')
                    else:
                        break




        # Quit the program.
        elif choice == 'q':
            print('Goodbye')
            break


        else:
            print('Invalid choice!!!')


main()
