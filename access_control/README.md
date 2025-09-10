# Access Control Implementation

## Objective
Implement and manage permissions and groups to control access to various parts of the Django application.

## Model: Resource
Custom permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Views
Each view is protected using `@permission_required`:
- List: `can_view`
- Create: `can_create`
- Edit: `can_edit`
- Delete: `can_delete`

## Testing
Users were manually assigned to groups via Django admin.
Access to views was verified by logging in as each user and checking permission enforcement.
