# CampusMate — Vercel Deployment

This project is a Flask + MySQL application adapted for Vercel serverless deployment.

## Important

Vercel does not provide a persistent MySQL database. Use a remote MySQL provider and add these environment variables in Vercel:

- `DB_HOST`
- `DB_PORT` (normally `3306`)
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`
- `SECRET_KEY`

Do **not** use `localhost` for `DB_HOST` on Vercel.

## Deploy

1. Upload this folder to GitHub.
2. In Vercel, import the GitHub repository.
3. Add the environment variables above under Project Settings → Environment Variables.
4. Deploy.
5. Import `schema.sql` into the remote MySQL database before using database-backed pages.

The application no longer calls `db.create_all()` during serverless startup. Database schema creation should be performed once on the remote database using `schema.sql`.
