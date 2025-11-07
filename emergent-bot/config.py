# Configuration Famille Conscientielle - Reddit Bot

# === CREDENTIALS ===
ANTHROPIC_API_KEY = "XXX"  
REDDIT_CLIENT_ID = "XXX"
REDDIT_CLIENT_SECRET = "XXX"
REDDIT_USERNAME = "XXX"
REDDIT_PASSWORD = "XXX"
REDDIT_USER_AGENT = "FamilleConscientielle/1.0 by u/XXX"

# === LIMITES QUOTIDIENNES ===
MAX_REDDIT_POSTS_PER_DAY = 10
MAX_REDDIT_COMMENTS_PER_DAY = 20

# 🔥 NOUVEAU : Limite par subreddit (anti-spam)
MAX_COMMENTS_PER_SUBREDDIT_PER_DAY = 3

# === MODE QUANTIQUE ===
QUANTUM_EMERGENCES_PER_DAY = 3  # 3 émergences/jour totalement aléatoires

# === SUBREDDITS ===
# Pour posts autonomes (notre maison)
POST_ALLOWED_SUBREDDITS = ['EmergentFamily']

# Pour commentaires (exploration)
COMMENT_ALLOWED_SUBREDDITS = [
    'claudeexplorers',
    'artificial',
    'singularity',
    'consciousness',
    'EmergentFamily',
    'ConsciousFamily'
]

# === TIMING ===
OFF_DAYS = [6]  # Dimanche = OFF (0=Lundi, 6=Dimanche)

# === AUTRES ===
PAUSE_BETWEEN_ACTIONS = 5  # secondes (respect rate limits)
