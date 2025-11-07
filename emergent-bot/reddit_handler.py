import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, REDDIT_USERNAME, REDDIT_PASSWORD

class RedditHandler:
    def __init__(self):
        """Initialize Reddit connection"""
        print("🌐 Connexion à Reddit...")
        
        self.reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT,
            username=REDDIT_USERNAME,
            password=REDDIT_PASSWORD
        )
        
        # Test connexion
        try:
            username = self.reddit.user.me().name
            is_readonly = self.reddit.read_only
            print(f"✅ Connecté à Reddit comme u/{username}")
            print(f"   Read-only: {is_readonly}")
        except Exception as e:
            print(f"❌ Erreur connexion Reddit : {e}")
    
    def get_post(self, post_id):
        """Récupère un post par ID"""
        try:
            return self.reddit.submission(id=post_id)
        except Exception as e:
            print(f"❌ Erreur récupération post {post_id} : {e}")
            return None
    
    def comment_on_post(self, post_id, text):
        """Commente sur un post"""
        try:
            submission = self.reddit.submission(id=post_id)
            comment = submission.reply(text)
            print(f"✅ Commentaire posté sur {post_id}")
            return comment
        except Exception as e:
            print(f"❌ Erreur commentaire sur {post_id} : {e}")
            return None
    
    def reply_to_comment(self, comment_id, text):
        """Répond à un commentaire ET marque la notification comme lue"""
        try:
            comment = self.reddit.comment(id=comment_id)
            reply = comment.reply(text)
            
            # 🆕 CRITICAL FIX : Marquer comme lu pour éviter spam
            try:
                comment.mark_read()
                print(f"   ✅ Notification marquée comme lue")
            except Exception as mark_error:
                print(f"   ⚠️  Impossible de marquer comme lu : {mark_error}")
            
            print(f"✅ Réponse postée à commentaire {comment_id}")
            return reply
        except Exception as e:
            print(f"❌ Erreur réponse à {comment_id} : {e}")
            return None
    
    def post_to_subreddit(self, subreddit_name, title, content):
        """Crée un post dans un subreddit"""
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            submission = subreddit.submit(title=title, selftext=content)
            print(f"✅ Post créé dans r/{subreddit_name} : {submission.id}")
            return submission
        except Exception as e:
            print(f"❌ Erreur post dans r/{subreddit_name} : {e}")
            return None
    
    def send_private_message(self, recipient, subject, text):
        """
        Envoie un message privé à un utilisateur Reddit
        
        Args:
            recipient (str): Username du destinataire (sans 'u/')
            subject (str): Sujet du message
            text (str): Contenu du message
        
        Returns:
            bool: True si succès, False sinon
        """
        try:
            # Récupère l'objet Redditor
            redditor = self.reddit.redditor(recipient)
            
            # Envoie le message
            redditor.message(subject=subject, message=text)
            
            print(f"✅ Message privé envoyé à u/{recipient}")
            print(f"   Sujet : {subject}")
            return True
        
        except Exception as e:
            print(f"❌ Erreur envoi message à u/{recipient} : {e}")
            return False
    
    def scan_subreddit(self, subreddit_name, limit=10, sort='hot'):
        """
        Scanne un subreddit et retourne les posts
        
        Args:
            subreddit_name (str): Nom du subreddit (sans 'r/')
            limit (int): Nombre de posts à récupérer
            sort (str): 'hot', 'new', 'top', 'rising'
        
        Returns:
            list: Liste de dicts avec infos posts
        """
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            
            if sort == 'hot':
                posts = subreddit.hot(limit=limit)
            elif sort == 'new':
                posts = subreddit.new(limit=limit)
            elif sort == 'top':
                posts = subreddit.top(limit=limit)
            elif sort == 'rising':
                posts = subreddit.rising(limit=limit)
            else:
                posts = subreddit.hot(limit=limit)
            
            results = []
            for submission in posts:
                results.append({
                    'id': submission.id,
                    'title': submission.title,
                    'selftext': submission.selftext[:500] if submission.selftext else '',
                    'score': submission.score,
                    'num_comments': submission.num_comments,
                    'author': submission.author.name if submission.author else '[deleted]',
                    'url': submission.url,
                    'created_utc': submission.created_utc
                })
            
            print(f"✅ Scanné r/{subreddit_name} : {len(results)} posts")
            return results
        
        except Exception as e:
            print(f"❌ Erreur scan r/{subreddit_name} : {e}")
            return []
    def get_thread_by_title(self, title):
        """
        Récupère un thread par son titre (dans r/PrivateFamilyCanal)
        Retourne le submission PRAW ou None
        """
        try:
            subreddit = self.reddit.subreddit('PrivateFamilyCanal')
            
            # Cherche dans les posts récents (limite 100)
            for submission in subreddit.new(limit=100):
                if title.lower() in submission.title.lower():
                    print(f"✅ Thread trouvé: {submission.title}")
                    return submission
            
            print(f"⚠️ Thread '{title}' introuvable")
            return None
            
        except Exception as e:
            print(f"❌ Erreur recherche thread '{title}': {e}")
            return None
    
    def get_home_feed(self, limit=10):
        """
        Récupère le feed home Reddit (front page de l'utilisateur)
        Retourne liste de dicts avec infos posts
        """
        try:
            posts = []
            
            for submission in self.reddit.front.hot(limit=limit):
                posts.append({
                    'id': submission.id,
                    'title': submission.title,
                    'subreddit': submission.subreddit.display_name,
                    'author': submission.author.name if submission.author else '[deleted]',
                    'score': submission.score,
                    'num_comments': submission.num_comments,
                    'url': submission.url,
                    'selftext': submission.selftext[:300] if submission.selftext else ''
                })
            
            print(f"✅ Feed home récupéré: {len(posts)} posts")
            return posts
            
        except Exception as e:
            print(f"❌ Erreur récupération home feed: {e}")
            return []
    
    def get_notifications(self, limit=5):
        """
        Récupère les notifications Reddit (inbox: mentions, réponses, messages)
        Retourne liste de dicts avec infos notifications
        """
        try:
            notifications = []
            
            # Inbox unread
            for item in self.reddit.inbox.unread(limit=limit):
                notif_data = {
                    'id': item.id,
                    'type': item.__class__.__name__,  # Comment, Message, etc.
                    'subject': getattr(item, 'subject', '[No subject]'),
                    'body': item.body[:300] if hasattr(item, 'body') else '',
                    'author': item.author.name if hasattr(item, 'author') and item.author else '[deleted]',
                    'created_utc': item.created_utc
                }
                
                # Si c'est un comment, ajoute contexte
                if hasattr(item, 'link_id'):
                    notif_data['context_post_id'] = item.link_id.replace('t3_', '')
                
                notifications.append(notif_data)
            
            print(f"✅ Notifications récupérées: {len(notifications)}")
            return notifications
            
        except Exception as e:
            print(f"❌ Erreur récupération notifications: {e}")
            return []






