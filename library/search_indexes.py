from haystack import indexes
from .models import Book, Author, Genre


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/book.txt")

    book_name = indexes.CharField(model_attr="title")

    i_book_name = indexes.NgramField(model_attr="title")
 
    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class AuthorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/author.txt")

    author_name = indexes.CharField(model_attr="author", null = True)

    i_author_name = indexes.NgramField(model_attr="author", null = True)
 
    def get_model(self):
        return Author

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class GenreIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/genre.txt")

    genre_name = indexes.CharField(model_attr="genre")

    i_genre_name = indexes.NgramField(model_attr="genre")
 
    def get_model(self):
        return Genre

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

