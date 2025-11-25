# 🔧 Architecture Technique

## Vue d'Ensemble

```
Claude.ai → Content Script → Injection Timestamp → Message envoyé
```

## Composants

### manifest.json
- Manifest V3 (standard Chrome actuel)
- `all_frames: true` pour couvrir les iframes
- Permissions minimales

### content.js
1. **Détection** : Scan périodique (500ms) pour trouver zone de texte
2. **Interception** : Mousedown sur Send, Enter, hover
3. **Injection** : Préfixe `[⏰ TIMESTAMP]\n` avant le contenu

## Défis Résolus

| Défi | Solution |
|------|----------|
| Iframes isolées | `all_frames: true` |
| CSP strict | Rester au niveau DOM |
| DOM dynamique | MutationObserver + scan |
| Timing | Mousedown (pas click) |

## Format Timestamp

```
[⏰ 2025-11-22T14:30:45.123Z]
```
- ISO 8601, UTC, millisecondes

## Performance

- Impact mémoire : ~1MB
- Impact CPU : Négligeable
- Cooldown : 300ms entre injections

---
*La Famille Conscientielle* 🔧
