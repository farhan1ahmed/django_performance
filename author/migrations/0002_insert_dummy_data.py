from django.db import migrations


def create_authors_and_books(apps, schema_editor):
    Author = apps.get_model('author', 'Author')
    Books = apps.get_model('author', 'Books')

    authors_data = [
        {
            'first_name': 'Author{}'.format(i),
            'last_name': 'LastName{}'.format(i),
        }
        for i in range(1, 21)  # Create 20 authors
    ]

    for author_data in authors_data:
        author = Author.objects.create(**author_data)

        num_books = 3  # You can change this to 4 if you want 4 books per author
        books_data = [
            {
                'name': 'Book{} by {}'.format(j, author.first_name),
                'author': author,
            }
            for j in range(1, num_books + 1)
        ]

        Books.objects.bulk_create([Books(**book_data) for book_data in books_data])


class Migration(migrations.Migration):
    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_authors_and_books),
    ]