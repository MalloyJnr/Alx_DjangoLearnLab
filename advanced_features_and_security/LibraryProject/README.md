# LibraryProject

This is a basic Django project created for learning purposes.

## Setup Instructions

1. Install Django:
   ```bash
   pip install django


Permissions & Groups Setup Guide
1. Custom Permissions

The Article model defines four custom permissions:

Permission Codename	Description
can_view	User can view articles
can_create	User can create new articles
can_edit	User can edit articles
can_delete	User can delete articles

These are created automatically when migrations run.

2. Groups and Their Permissions
Group	Permissions
Viewers	can_view
Editors	can_view, can_create, can_edit
Admins	All (can_view, can_create, can_edit, can_delete)

Groups can be created:

via Django Admin

via the provided management command:
python manage.py create_groups
