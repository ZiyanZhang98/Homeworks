
#######################
# Note change to build_tree(filename) method at end of file
# and clarification of the difference between search() and search_node()
# Changed on 15/11/2019
#######################
from functools import total_ordering
import math
import sys

@total_ordering
class Movie:
    """ Represents a single Movie. """

    def __init__(self, i_title, i_date, i_runtime):
        """ Initialise a Movie Object. """
        self._title = i_title
        self._date = i_date
        self._time = i_runtime

    def __str__(self):
        """ Return a short string representation of this movie. """
        outstr = self._title
        return outstr

    def full_str(self):
        """ Return a full string representation of this movie. """
        outstr = self._title + ": "
        outstr = outstr + str(self._date) + "; "
        outstr = outstr + str(self._time)
        return outstr

    def get_title(self):
        """ Return the title of this movie. """
        return self._title

    def __eq__(self, other):
        """ Return True if this movie has exactly same title as other. """
        if (other._title == self._title):
            return True
        return False

    def __ne__(self, other):
        """ Return False if this movie has exactly same title as other. """
        return not (self._title == other._title)

    def __lt__(self, other):
        """ Return True if this movie is ordered before other.

        A movie is less than another if it's title is alphabetically before.
        """
        if other._title > self._title:
            return True
        return False


class BSTNode:
    """ An internal node for a Binary Search Tree.

    This is a general BST, but with a small number of additional methods to
    implement a movie library. The title of the Movie is used as the search
    key.
    """
    
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        if self is not None:
            outstr = self._element.__str__()
            outstr = self._leftchild.__str__() + ' ' + outstr
            outstr = outstr + ' ' + self._rightchild.__str__()
            return outstr
        else:
            return ''

    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
               + '; height = ' + str(self.height()))
  
    def search(self, title):
        """ Return the Movie object with that movie title, or None.

        Args:
            title: a string for the title of a Movie
            # clarification added 15/11/2019

        This method is specific to the Movie library.
        """
        if self._element.get_title() == title:
            return self._element
        elif self._element.get_title() < title:
            if self._rightchild is not None:
                return self._rightchild.search(title)
            return None
        else:
            if self._leftchild is not None:
                return self._leftchild.search(title)
            return None

    def search_node(self, searchitem):
        """ Return the node (with subtree) containing searchitem, or None. 

        Args:
            searchitem: a Movie object  # clarification added 15/11/2019
        """
        if self._element == searchitem:
            return self
        else:
            if self._element < searchitem:
                if self._rightchild is not None:
                    return self._rightchild.search_node(searchitem)
                return None
            else:
                if self._leftchild is not None:
                    return self._leftchild.search_node(searchitem)
                return None

    def add(self, obj):
        """ Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        if self._element is None:
            self._element = obj
        elif self._element == obj:
            return None
        else:
            if obj < self._element:
                if self._leftchild is None:
                    self._leftchild = BSTNode(obj)
                    self._leftchild._parent = self
                else:
                    self._leftchild.add(obj)
            else:
                if self._rightchild is None:
                    self._rightchild = BSTNode(obj)
                    self._rightchild._parent = self
                else:
                    self._rightchild.add(obj)
        return obj

    def findmaxnode(self):
        """ Return the BSTNode with the maximal element at or below here. """
        if self._rightchild is None:
            return self
        else:
            return self._rightchild.findmaxnode()
    
    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """
        if self._leftchild is None:
            if self._rightchild is None:
                return 1
            else:
                return 1 + self._rightchild.height()
        elif self._rightchild is None:
            return 1 + self._leftchild.height()
        elif self._leftchild.height() > self._rightchild.height():
            return 1 + self._leftchild.height()
        else:
            return 1 + self._rightchild.height()

    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree.
        """
        size = 1
        if self._rightchild is not None:
            size += self._rightchild.size()
        if self._leftchild is not None:
            size += self._leftchild.size()
        return size

    def leaf(self):
        """ Return True if this node has no children. """
        if self.size() == 1:
            return True
        return False

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        if self.size() == 2:
            return True
        return False

    def full(self):
        """ Return true if this node has two children. """
        if self.size == 3:
            return True
        return False

    def internal(self):
        """ Return True if this node has at least one child. """
        if self.size() >= 2:
            return True
        return False

    def remove(self, title):
        """ Remove and return a movie.

        This method is specific to the Movie library.
        Remove the movie with the given title from the tree rooted at this node.
        Maintains the BST properties.
        """
        movie = self.search(title)
        if movie is None:
            return None
        else:
            node = self.search_node(movie)
            node._element = None
            return movie

    @property
    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        parent = self._parent
        out = self._element
        if self.full() is True:
            new_node = self._leftchild.findmaxnode()
            if parent._element < self._element:
                parent._rightchild = new_node
            else:
                parent._leftchild = new_node
            self._rightchild._parent = new_node
            self._leftchild._parent = new_node
            new_node._parent._rightchild = None
            new_node._parent = parent
            new_node._leftchild = self._leftchild
            new_node._rightchild = self._rightchild
        elif self.leaf() is True:
            if self._element < parent._element:
                self._parent._leftchild = None
            else:
                self._parent._rightchild = None
        elif self._rightchild is None and self._leftchild is not None:
            new_node = self._leftchild
            if self._element < parent._element:
                parent._leftchild = new_node
            else:
                parent._rightchild = new_node
            self._leftchild._parent = new_node
            new_node._parent = parent
            new_node._leftchild = self._leftchild
            new_node._rightchild = self._rightchild
        else:
            new_node = self._rightchild
            if self._element < parent._element:
                parent._leftchild = new_node
            else:
                parent._rightchild = new_node
            self._rightchild._parent = new_node
            new_node._parent = parent
            new_node._leftchild = self._leftchild
            new_node._rightchild = self._rightchild
        self = None
        return out


def build_tree(filename):
    """ Return a BST tree of Movie files built from filename. """

    # open the file
    file = open(filename, 'r')

    # Create the root node  of a BST with a Movie object created from the
    # first line in the file
    inputlist = file.readline().split('\t')
    movie = Movie(inputlist[0], inputlist[1], inputlist[2])
    bst = BSTNode(movie)
    count = 1
    for line in file:
        inputlist = line.split('\t')
        movie = Movie(inputlist[0], inputlist[1], inputlist[2])
        added = bst.add(movie)
        # if added != None:  # changed on 15/11/2019 - this line fails when
        #                      the BST adds a new movie, since the BST returns
        #                      a movie object, and Python then calls the 
        #                      __ne__ method on the Movie class with None as
        #                      as the other argument; but None has no 
        #                      _title field, and so Python crashes.
        #                      The following line works, because Python
        #                      treats 'is not' differently -- it is checking
        #                      that the two objects are different things in
        #                      in memory, regardless of their values..
        #                      You could also do     if added:
        #                      but relying on the None object to fail the
        #                      test is said to be not good coding style ...
        if added is not None:
            count += 1

    # print out some info for sanity checking
    print("Built a tree of height " + str(bst.height()))
    print("with", count, "movies")
    return bst


def using_bst(bst):
    balanced_h = int(math.log(bst.height(), 2) + 1)
    print('height:'+str(bst.height())+', unique movies:'+str(bst.size())+', minimum height of balanced tree:'+str(balanced_h))
    get_node("Four Lions", bst)
    get_node("Wonder Woman", bst)
    get_node("Touch of Evil", bst)
    get_node("Delicatessen", bst)


def get_node(name, bst):
    m = bst.search(name)
    if m is None:
        print("None")
        return
    node = bst.search_node(m)
    if node is not None:
        print(m)
        print('Ordered:', node)


node1 = build_tree('smallmovies.txt')
using_bst(node1)
node2 = build_tree('small_repeated_movies.txt')
using_bst(node2)
x = 5000
sys.setrecursionlimit(x)
node3 = build_tree('movies.txt')
using_bst(node3)