# social_media_api

This project contains a basic accounts app for a social media API.

Auth endpoints:
- POST /api/accounts/register/   -> register (returns token)
- POST /api/accounts/login/      -> obtain token
- GET  /api/accounts/users/<id>/ -> get user profile

Make sure to configure `MEDIA_ROOT` and run migrations before testing.
