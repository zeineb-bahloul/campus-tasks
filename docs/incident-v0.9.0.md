# Compte rendu d'incident — mise en service de v0.9.0

1. **Ce qui s'est passé** : la version v0.9.0 a été mise en service en staging ; le service n'a plus répondu sur `/health`.
2. **Quand je l'ai su** : juste après le `docker compose up -d`, `scripts/wait-healthy.sh` a échoué au bout de 60 s. Première erreur utile des journaux : `À COMPLÉTER`.
3. **Ce que j'ai fait** : retour arrière en remettant `IMAGE_TAG=v1.0.0` dans `.env.deploy`, puis `docker compose up -d`, sans reconstruire l'image ; `wait-healthy.sh` a de nouveau affiché « staging sain ».
4. **Durée d'indisponibilité** : environ `À COMPLÉTER` minutes, entre la mise en service de v0.9.0 et le contrôle de santé réussi de v1.0.0.
5. **Pour éviter que cela se reproduise** : n'accepter une version que si le contrôle de santé réussit, et automatiser le retour arrière quand il échoue.
