# LibraryProject

## Overview
This Django project demonstrates advanced features including secure HTTPS configuration, custom permissions, and group-based access control.

## Permissions and Groups
- Custom permissions added to the `Book` model: `can_view`, `can_create`, `can_edit`, `can_delete`.
- Groups configured:
  - **Admins**: Full access
  - **Editors**: Can create and edit books
  - **Viewers**: Can only view books

## Usage
- Assign users to groups via the Django admin.
- Views are protected with `@permission_required('bookshelf.can_edit', raise_exception=True)` and similar decorators.

## Security
- HTTPS enforced
- Secure cookies and headers configured
