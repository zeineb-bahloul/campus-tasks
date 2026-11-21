# Compte rendu d'incident — mise en service de v0.9.0

1. **Ce qui s'est passé** : la version v0.9.0 a été mise en service en staging ; le service n'a plus répondu sur `/health`.
2. **Quand je l'ai su** : juste après le `docker compose up -d`, `scripts/wait-healthy.sh` a échoué au bout de 60 s. Première erreur utile des journaux : `* Running on http://127.0.0.1:8080` (l'application n'écoute que sur 127.0.0.1, elle est injoignable depuis l'extérieur du conteneur).
3. **Ce que j'ai fait** : retour arrière en remettant `IMAGE_TAG=v1.0.0` dans `.env.deploy`, puis `docker compose up -d`, sans reconstruire l'image ; `wait-healthy.sh` a de nouveau affiché « staging sain ».
4. **Durée d'indisponibilité** : environ 3 minutes, entre la mise en service de v0.9.0 et le contrôle de santé réussi de v1.0.0.
5. **Pour éviter que cela se reproduise** : vérifier que l'application écoute sur `0.0.0.0`, n'accepter une version que si le contrôle de santé réussit depuis l'extérieur, et automatiser le retour arrière quand il échoue.