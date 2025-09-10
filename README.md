
# LibraryProject

This Django project demonstrates advanced features and access control using permission decorators.

## Structure

- `LibraryProject/bookshelf/views.py`: Contains permission-protected views like `book_list`.
- `models.py`: Defines the `Book` model.
- `templates/bookshelf/`: Holds HTML templates for book views.

## Permissions

Custom permissions used:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

These are enforced using `@permission_required(..., raise_exception=True)` decorators.

## Setup

Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
