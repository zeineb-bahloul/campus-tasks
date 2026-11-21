# Campus Tasks

## Démarrage

Projet utilisé dans les ateliers DevOps.

## Healthcheck

Endpoint prévu : GET /health.

## Support
Contact equipe A : equipe-a@example.invalid
Contact equipe B : equipe-b@example.invalid

## Intégration continue

Chaque pull request lance les tests (`pytest`), puis la construction de l'image Docker.
Le rapport de tests `report.xml` est conservé en artefact.
Un tag `vX.Y.Z` publie l'image `ghcr.io/zeineb-bahloul/campus-tasks:vX.Y.Z`.

## Mise en service (staging)

```bash
cp .env.staging.example .env.staging
printf 'IMAGE_TAG=v1.0.0\n' > .env.deploy
docker compose --env-file .env.deploy -f compose.staging.yaml pull
docker compose --env-file .env.deploy -f compose.staging.yaml up -d
./scripts/wait-healthy.sh
```

## Retour arrière

Remettre la version précédente dans `.env.deploy`, puis relancer `up -d` et `wait-healthy.sh`.
L'image n'est jamais reconstruite.
