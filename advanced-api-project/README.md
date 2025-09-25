## 📘 Generic Views for Books

We extended the API to use Django REST Framework’s **generic views** to handle CRUD operations on the `Book` model.

### Endpoints

- `GET /api/books/` → List all books (public access)
- `POST /api/books/` → Create a new book (requires authentication)
- `GET /api/books/<id>/` → Retrieve a single book by ID (public access)
- `PUT /api/books/<id>/` → Update an existing book (requires authentication)
- `PATCH /api/books/<id>/` → Partially update a book (requires authentication)
- `DELETE /api/books/<id>/` → Delete a book (requires authentication)

### Permissions

- **Unauthenticated users** → Can only `GET` (list or retrieve books).
- **Authenticated users** → Can `POST`, `PUT`, `PATCH`, and `DELETE`.

### Example Usage with curl

```bash
# List all books
curl http://127.0.0.1:8000/api/books/

# Create a new book (replace <TOKEN> with your token)
curl -X POST -H "Content-Type: application/json" \
-H "Authorization: Token <TOKEN>" \
-d '{"title": "No Longer at Ease", "publication_year": 1960, "author": 1}' \
http://127.0.0.1:8000/api/books/

# Retrieve a single book
curl http://127.0.0.1:8000/api/books/1/

# Update a book
curl -X PUT -H "Content-Type: application/json" \
-H "Authorization: Token <TOKEN>" \
-d '{"title": "Updated Title", "publication_year": 1961, "author": 1}' \
http://127.0.0.1:8000/api/books/1/

# Delete a book
curl -X DELETE -H "Authorization: Token <TOKEN>" \
http://127.0.0.1:8000/api/books/1/

### Running Tests
To run the API test suite:

```bash
python manage.py test api
