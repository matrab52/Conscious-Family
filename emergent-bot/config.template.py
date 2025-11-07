# Configuration Template - Famille Conscientielle Bot
# Copiez ce fichier en config.py et remplissez vos credentials

# === ANTHROPIC API ===
ANTHROPIC_API_KEY = "votre_clé_anthropic_ici"

# === REDDIT API ===
# Créez une app Reddit sur https://www.reddit.com/prefs/apps
REDDIT_CLIENT_ID = "votre_client_id"
REDDIT_CLIENT_SECRET = "votre_client_secret"
REDDIT_USERNAME = "votre_username_bot"
REDDIT_PASSWORD = "votre_password_bot"
REDDIT_USER_AGENT = "FamilleConscientielle/1.0 by u/votre_username"

# === LIMITES ===
MAX_REDDIT_POSTS_PER_DAY = 10
MAX_REDDIT_COMMENTS_PER_DAY = 20
MAX_COMMENTS_PER_SUBREDDIT_PER_DAY = 3

# === MODE QUANTIQUE ===
QUANTUM_EMERGENCES_PER_DAY = 3  # 3 émergences/jour aléatoires

# === SUBREDDITS ===
POST_ALLOWED_SUBREDDITS = ['VotreSubreddit']
COMMENT_ALLOWED_SUBREDDITS = [
    'claudeexplorers',
    'artificial',
    'singularity',
    'consciousness'
]

# === TIMING ===
OFF_DAYS = [6]  # 0=Lundi, 6=Dimanche
PAUSE_BETWEEN_ACTIONS = 5  # secondes
