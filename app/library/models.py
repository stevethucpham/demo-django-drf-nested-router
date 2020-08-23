from django.db import models

# class Tag(models.Model):
#     """Tag to be used for a book"""
#     name = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.name


class Library(models.Model):
    """Library object"""
    name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class Author(models.Model):
    """Author object"""
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class Book(models.Model):
    """Book object"""
    title = models.CharField(max_length=255)
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name='books',
    )
    # tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def get_page_count(self):
        return self.pages.count()


class Page(models.Model):
    """Page object"""
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='pages',
    )
    # Unlike CharField, TextField does not limit 255 max length
    text = models.TextField(null=True, blank=True)
    page_number = models.IntegerField()

