#Import peewee and date info
from peewee import *
import datetime


#create db connection
db = PostgresqlDatabase('bookmarks', user='postgres', password='', host='localhost', port=5432)

# add db Base model
class BaseModel(Model):
    class Meta:
        database = db
#define db Schema
class Bookmark(BaseModel):
    name = CharField()
    link = CharField()
    entered_date = DateField()

#starts connection to database
db.connect()

#Delete any current tables in Bookmark then
#Create new tables in Bookmark
db.drop_tables([Bookmark])
db.create_tables([Bookmark])

#Create some starter bookmarks
W3 = Bookmark(name='W3 Schools', link='https://www.w3schools.com/', entered_date=datetime.datetime.now()).save()
MDNWebDocs = Bookmark(name='MDN', link='https://developer.mozilla.org/en-US/', entered_date=datetime.datetime.now()).save()
StackOverflow = Bookmark(name='stack overflow', link='https://stackoverflow.com/', entered_date=datetime.datetime.now()).save()

#Main menu function lists user options
def main_menu():
    print('\nWelcome to your web developer help bookmark library!\nCreate a list of websites that will help you learn to be a better developer\nChoose number of the option you would like: \n 1. Create a new bookmark \n 2. List all bookmarks \n 3. Find a bookmark \n\nPress any key to quit')
    option = str(input('\nWhat would you like to do?: '))
    if option == '1':
        add_bookmark()
    elif option == '2':
        list_Bookmarks()
    elif option == '3':
        find_bookmark()
    else:
        print('Have a great day, see you later!')
        exit()

#Function to create a new bookmark

def add_bookmark():
    add_bookmark = input('What is the name of the bookmark?: \n' )
    new_link = input('Enter the link to the bookmarked site: \n')

    add_bookmark = Bookmark(name=add_bookmark, link=new_link, entered_date=datetime.datetime.now()).save()

    find_bookmark = Bookmark.select().where(Bookmark.name == add_bookmark)

    print('\nBookmark successfully entered!\n')

    for bookmark in find_bookmark:
        print(f'\nName: {bookmark.name} \n Link: {bookmark.link} \n Date Entered: {bookmark.entered_date}\n')
        print('\n----------------\n')

    main_menu()

#list function prints all bookmarks in the db
def list_Bookmarks():
    bookmarks = Bookmark.select()
    for bookmark in bookmarks:
        print(f'Site name: {bookmark.name} \nSite link: {bookmark.link} \nDate site entered {bookmark.entered_date}\n\n')

    main_menu()
#find function finds bookmark by name
def find_bookmark():
    try:
        find = input('What is the exact name of the site you would like to find? (case sensitive): \n')
        find_bookmark = Bookmark.select().where(Bookmark.name == find)
        for bookmark in find_bookmark:
            print(f'\n See {find} bookmark information below: \n')
            print(f'Name: {bookmark.name} \n Site Link: {bookmark.link} \n Entered: {bookmark.entered_date}\n\n')
           
    except:
        print(f'\n{find} not found.\n')
        main_menu()
#function below keeps it from exiting app
    main_menu()


main_menu()