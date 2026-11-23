# Development environment

Historical baseline: FAIRF commit `da3404de0a8a055a961e98fffd900e5146d677d4`, inspected November 23, 2026. Verify the current checkout before running commands.

## Stack and boundaries

- Python >=3.11; container and Python CI use 3.13. Flask 3 with Jinja templates, ordinary CSS and JavaScript; no React/Next.js build is needed for this web UI.
- Flask-SQLAlchemy, PostgreSQL 17, psycopg, Flask-Migrate/Alembic. Pinned Python dependencies live in `requirements.txt`.
- Flask-Login, Flask-WTF/CSRF and Flask-Limiter support web authentication, forms and rate limits. Mobile uses a versioned bearer-token API at `/api/v1`.
- A separate Flask CLI identification worker processes durable photo jobs. Gunicorn serves HTTP; running only the development web server does not start the worker.
- Local private uploads or private S3-compatible storage. Pillow inspects images; pypdfium2 supports server PDF processing; openpyxl supports spreadsheet imports.
- Native Kotlin, Compose and Material 3 Android client; coroutines/lifecycle APIs and WorkManager support asynchronous and durable work. No JavaScript mobile framework.
- Docker Compose supports local services; Debian production uses Nginx, systemd, Gunicorn, PostgreSQL and a separate worker.

## Setup: choose one topology

First inspect `.env.example`, manifests, Compose and local port availability. Copy the example only if `.env` does not already exist; never overwrite working credentials. Keep AI in `mock` mode until an external workflow is intended.

### Entire stack in containers

From the target checkout, prepare `.env` from the example, then:

```sh
docker compose up --build
```

The recorded Compose app binds `127.0.0.1:8000`; PostgreSQL is internal at `db:5432`. App and worker receive the container database URL and share the uploads volume. App startup applies migrations; the worker waits for app health. Check `/api/v1/health`, service logs and a mock identification job.

### Python on the host

The historical README says to start only the Compose database and use localhost, but that Compose file publishes **no database port**. Resolve this explicitly: use an existing local PostgreSQL instance or a local Compose override publishing `127.0.0.1:5432:5432` (choose another host port if occupied). Keep the override outside tracked configuration unless requested. Do not expose PostgreSQL on all interfaces.

For example, an external `compose.local.yaml` can contain:

```yaml
services:
  db:
    ports:
      - "127.0.0.1:5432:5432"
```

Start it from the checkout with `docker compose -f docker-compose.yml -f /absolute/path/compose.local.yaml up -d db`. This override is a corrective setup suggestion, not a file shipped in the historical repository.

With a reachable development database and matching `DATABASE_URL`:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
flask --app run:app db upgrade
flask --app run:app run --debug
```

In a second terminal, activate the same environment and run:

```sh
flask --app run:app work-identification-jobs
```

Open `http://127.0.0.1:5000`. Use `create-admin` for the first intended admin. `seed-demo` is only for isolated development; it creates known demo credentials.

Migration helper: `scripts/migrate.sh current`, `heads`, `sql-upgrade`, `upgrade`, and `check`. Review generated migrations. Downgrades require a deliberate target; changing application code is not a database rollback.

## Android tooling

Recorded requirements: JDK 17, SDK Platform 37, `JAVA_HOME`, `ANDROID_HOME`, and the checked-in Gradle wrapper. The snapshot compiles SDK 37, targets 36, and supports API 26+. Resolve exact plugin/library versions from Gradle; do not upgrade them simply because this skill is invoked.

From `android/`:

```sh
./gradlew testDebugUnitTest lintDebug assembleDebug
./gradlew connectedDebugAndroidTest
```

The second command needs a running compatible emulator/device. The local evidence used Pixel 8 / API 36; recorded CI used API 35. These are different test environments.

The app's default API is production. For local development, set an explicit development **HTTPS** API:

```sh
./gradlew assembleDebug -PapiBaseUrl=https://your-dev-host.example/api/v1/
```

Use a reachable trusted development TLS endpoint; host loopback is not the emulator's loopback. Do not weaken the HTTPS-only app policy just to make a sample command work. Debug output is `app/build/outputs/apk/debug/app-debug.apk`.

## Verification layers

Inspect current CI rather than assuming tests passed in this run. Recorded server checks:

```sh
flask --app run:app db upgrade
node --test tests/js/*.test.cjs
pytest --cov=app --cov-report=term-missing
pip-audit -r requirements.txt
bandit -q -r app config.py run.py
```

Use a test database and mock providers. Install CI's audit tools in the development environment if needed. Node supplies its built-in test runner; this does not imply an npm-based frontend.

For accessibility changes, use the focused Python/JS tests, Android theme/preference unit tests, emulator layout tests and visual inspection. Test ordinary layouts plus combined preferences, navigation, restart, sign-out, failed persistence, keyboard and draft restoration. Do not equate a build or a contrast test with end-to-end accessibility.

## Production shape and release decisions

The Debian installer creates `/opt/skeinwise`, protected configuration in `/etc/skeinwise/skeinwise.env`, durable uploads in `/var/lib/skeinwise/uploads`, and web/worker services. These are conventions of the example, not universal paths. Configure TLS, trusted hosts, secure cookies and HSTS before private use. Set separate production secrets; do not copy a developer's live environment.

Recorded auto-deploy gates on successful main-branch CI and deploys the exact tested SHA. It serializes deploys, refuses stale commits, prepares a release, stops services, backs up database/local uploads, switches code, migrates, restarts both services and checks health. There is downtime. Database changes prevent blind automatic rollback; recovery must consider schema and data together. Replicate backups off-server and verify restores.

Restart both web and worker after AI/environment changes. A healthy HTTP endpoint does not prove a photo job completes.

Android distributions have distinct identities/signing paths. Keep signing keys external, version codes increasing, server compatibility deployed first, and the chosen distribution identity stable. Do not publish a debug build as a production release.
