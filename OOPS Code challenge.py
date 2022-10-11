1)
class Book:
    #instance variables
    def __init__ (self, authorlast, authorfirst, title, place, publisher,
                  year):
        self.last = authorlast
        self.first = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year
    
    #instance method
    def write_bib_entry (self):
        return (self.first+" "+ self.last+", "+ self.title+", "+
                self.place+", "+ self.publisher+", "+ self.year)
2)
#instances of book class
beauty= Book("Dubay", "Thomas", "The Evidential Power of Beauty",
             "San Francisco", "Ignatius Press", '1999')
pynut= Book("Martelli", "Alex", "Python in the Nutshell", 
             "Newyork", "O'Reilly Media", "2017")

3)
print(pynut.write_bib_entry())
print(Book.write_bib_entry(pynut))

4)
print(beauty.write_bib_entry())

5)
print(beauty.year)
beauty.year = '2021'
print(beauty.write_bib_entry())
















