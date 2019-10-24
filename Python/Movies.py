class Movie:
    def __init__(self, title, director, cast, length, rating=-1):
        self.title = title
        self.director = director
        self.cast = cast
        self.length = length
        self.rating = rating

    def get_info(self):
        return 'title: %s; director: %s; cast: %s; length: %d; rating: %d' % (self.title, self.director, self.cast, self.length, self.rating)

    def __str__(self):
        return 'title: %s; director: %s' % (self.title, self.director)


class Node:
    def __init__(self, element):
        self.element = element
        self.prev_node = None
        self.next_node = None


class Pyflix:
    def __init__(self):
        self.first = None
        self.current = None
        self.last = None
        self.size = 0

    def add_movie(self, movie):
        node = Node(movie)
        if self.first is None:
            self.first = node
            self.last = node
            self.current = self.first
        else:
            self.last.next_node = node
            node.prev_node = self.last
            self.last = node
        self.size += 1

    def get_current(self):
        print('Current movie:', end='  ')
        print(self.current.element)

    def next_movie(self):
        self.current = self.current.next_node

    def prev_movie(self):
        self.current = self.current.prev_node

    def reset(self):
        self.current = self.first

    def info(self):
        print('info:', end=' ')
        print(self.current.element.get_info())

    def remove_current(self):
        if self.size == 0:
            return None

        if self.current == self.first:
            temp = self.first.next_node
            temp.prev_node = None
            self.first = temp
            self.current = self.first
        elif self.current == self.last:
            temp = self.last.prev_node
            temp.next_node = None
            self.last = temp
            self.current = self.last
        else:
            self.current.prev_node.next_node = self.current.next_node
            self.current.next_node.prev_code = self.current.prev_node
            self.current = self.current.next_node

    def length(self):
        print(self.size)

    def rate(self):
        new_rate = int(input('Enter your rating[0, 4]: '))
        self.current.element.rating = new_rate
        print('Your rate was %d'%new_rate)

    def __str__(self):
        head = self.first
        return_str = ''
        while head is not None:
            if head == self.current:
                return_str += ('->  ' + head.element.title + head.element.director + '\n')
            else:
                return_str += ('\t' + head.element.title + head.element.director + '\n')
            head = head.next_node
        return return_str

    def search(self, word):
        head = self.first
        while head is not None:
            if word in head.element.get_info():
                self.current = head
                print(head.element.get_info())
                return None
            head = head.next_node
        print('No matching movie')
        return None


movies = Pyflix()
movie1 = Movie("El Camino", "Vince Gilligan", "Aaron Paul", 122)
movie2 = Movie("Joker", "Todd Phillips", "Joaquin Phoenix", 122)
movie3 = Movie("Midsommar", "An Aster", "Florence Pugh", 138)
movies.add_movie(movie1)
movies.add_movie(movie2)
movies.add_movie(movie3)
movies.next_movie()
movies.get_current()
movies.prev_movie()
movies.get_current()
movies.remove_current()
print(movies)
movies.get_current()
movie4 = Movie("Hustlers", "Lorene Scafaria", "Constance Wu, Jennifer Lopez", 110)
movies.add_movie(movie4)
movies.next_movie()
movies.next_movie()
movies.get_current()
print(movies)
movies.search('Ziyan Zhang')
movies.remove_current()
movies.get_current()