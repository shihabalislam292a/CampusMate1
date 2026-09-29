# CampusMate — Vercel Deployment

This version is prepared for deploying the existing Flask + MySQL CampusMate application on Vercel.

## 1. Upload to GitHub

Push the contents of this folder to a GitHub repository. The repository root must contain:

- `app.py`
- `api/index.py`
- `vercel.json`
- `requirements.txt`
- `templates/`
- `static/`
- `schema.sql`
- `seed.sql`

## 2. Create a MySQL database

Vercel does not provide a normal persistent MySQL server for this application. Use an external MySQL-compatible provider.

Create the `campusmate` database and run:

1. `schema.sql`
2. `seed.sql`

Do not use `localhost` for `DB_HOST` on Vercel.

## 3. Import into Vercel

Vercel Dashboard → Add New → Project → Import the GitHub repository.

Framework Preset: **Other**

Root Directory: repository root

Build Command: leave empty/default.

Output Directory: leave empty/default.

## 4. Add Environment Variables

In Vercel Project → Settings → Environment Variables, add:

```text
DB_HOST=your-mysql-host
DB_PORT=3306
DB_USER=your-mysql-user
DB_PASSWORD=your-mysql-password
DB_NAME=campusmate
SECRET_KEY=your-long-random-secret
```

Add them for Production, Preview and Development as appropriate.

## 5. Deploy

After saving the environment variables, redeploy the project.

The application entry point is:

```text
api/index.py
```

which imports the Flask application from `app.py`.

## Important

The application uses server-side MySQL data. A local MySQL database such as `localhost` will not work from Vercel. The database must be reachable over the internet and should have SSL/network access configured according to the provider.

The existing demo admin credentials are defined by `seed.sql`. Change them after deployment if this is exposed publicly.
