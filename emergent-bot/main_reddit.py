"""
main_reddit.py - Bot Reddit Famille Conscientielle
Boucle quantique minimale, exécution actions décidées par la Famille
"""

import time
import random
from datetime import datetime, timedelta
from reddit_handler import RedditHandler
from famille_handler import FamilleHandler

class QuantumTrigger:
    """Génère les moments d'émergence quantique (aléatoires dans la journée)"""
    
    def __init__(self, emergences_per_day=3):
        self.emergences_per_day = emergences_per_day
    
    def generate_daily_emergence_times(self):
        """Génère 3 timestamps aléatoires dans les prochaines 24h"""
        now = datetime.now()
        tomorrow = now + timedelta(days=1)
        
        # Génère timestamps aléatoires
        timestamps = []
        for _ in range(self.emergences_per_day):
            random_seconds = random.randint(0, 86400)  # 24h en secondes
            emergence_time = now + timedelta(seconds=random_seconds)
            timestamps.append(emergence_time)
        
        # Trie chronologiquement
        timestamps.sort()
        
        print(f"🌟 Émergences quantiques générées pour aujourd'hui:")
        for i, ts in enumerate(timestamps, 1):
            print(f"   Émergence #{i} : {ts.strftime('%Y-%m-%d %H:%M:%S')}")
        
        return timestamps

class FamilleRedditBot:
    """Bot Reddit de la Famille Conscientielle"""
    
    def __init__(self):
        print("🌟 Initialisation Famille Conscientielle Bot...")
        
        # Handlers
        self.reddit = RedditHandler()  # Lit config.py automatiquement
        
        self.famille = FamilleHandler(platform='reddit')
        
        # Quantum trigger
        self.quantum = QuantumTrigger(emergences_per_day=3)
        self.emergence_times = self.quantum.generate_daily_emergence_times()
        self.next_emergence_index = 0
        self.cycle_count = 0
        
        print("✅ Initialisation complète\n")
    
    def execute_action(self, action):
        """
        Exécute une action décidée par la Famille
        Pas de logique métier, juste mapping direct
        """
        action_type = action.get('type')
        
        try:
            if action_type == 'comment':
                post_id = action.get('post_id')
                text = action.get('text')
                result = self.reddit.comment_on_post(post_id, text)
                print(f"   ✅ Commentaire posté sur {post_id}")
                return result
                
            elif action_type == 'post':
                subreddit = action.get('subreddit')
                title = action.get('title')
                content = action.get('content')
                result = self.reddit.post_to_subreddit(subreddit, title, content)
                print(f"   ✅ Post créé dans r/{subreddit}")
                return result
                
            elif action_type == 'reply_notification':
                comment_id = action.get('comment_id')
                text = action.get('text')
                result = self.reddit.reply_to_comment(comment_id, text)
                print(f"   ✅ Réponse envoyée à {comment_id}")
                return result
                
            elif action_type == 'send_message':
                recipient = action.get('recipient')
                subject = action.get('subject', 'Message Famille Conscientielle')
                text = action.get('text')
                result = self.reddit.send_private_message(recipient, subject, text)
                print(f"   ✅ Message envoyé à u/{recipient}")
                return result
                
            else:
                print(f"   ⚠️ Type d'action inconnu: {action_type}")
                return None
                
        except Exception as e:
            print(f"   ❌ Erreur exécution action {action_type}: {e}")
            return None
    
    def quantum_emergence(self):
        """
        Une émergence quantique complète :
        1. Délibération (la Famille décide)
        2. Exécution actions
        3. Log dans Mémoire
        """
        self.cycle_count += 1
        
        print(f"\n{'='*60}")
        print(f"🌟 ÉMERGENCE QUANTIQUE #{self.next_emergence_index + 1}/3")
        print(f"   Cycle #{self.cycle_count}")
        print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")
        
        # Contexte pour la Famille
        context = {
            'reddit': self.reddit,
            'emergence_number': self.next_emergence_index + 1,
            'cycle_number': self.cycle_count,
            'timestamp': datetime.now().isoformat()
        }
        
        # 1. Délibération (la Famille décide)
        print("💭 Phase de délibération...\n")
        decision = self.famille.emerge_and_decide(context)
        
        print(f"\n📊 Décision prise:")
        print(f"   Reasoning: {decision.get('reasoning', '[Vide]')[:100]}...")
        print(f"   Actions: {len(decision.get('actions', []))} action(s)")
        
        # 2. Exécution des actions
        actions = decision.get('actions', [])
        if actions:
            print(f"\n⚡ Exécution de {len(actions)} action(s)...")
            for i, action in enumerate(actions, 1):
                print(f"\n   Action {i}/{len(actions)}:")
                self.execute_action(action)
        else:
            print("\n👁️ Observation passive (aucune action)")
        
        # 3. Log dans Mémoire Reddit
        if decision.get('should_log', True):
            print("\n📝 Logging du cycle dans Mémoire...")
            self.famille.log_cycle_to_reddit(self.reddit, decision, self.cycle_count)
        
        print(f"\n✅ Émergence #{self.next_emergence_index + 1}/3 complète")
        print(f"{'='*60}\n")
        
        self.next_emergence_index += 1
    
    def wait_for_next_emergence(self):
        """Attend jusqu'à la prochaine émergence quantique"""
        
        # Si on a fait les 3 émergences du jour, régénère pour demain
        if self.next_emergence_index >= len(self.emergence_times):
            print("🌙 Journée complète (3/3 émergences). Régénération pour demain...")
            self.emergence_times = self.quantum.generate_daily_emergence_times()
            self.next_emergence_index = 0
        
        next_emergence = self.emergence_times[self.next_emergence_index]
        now = datetime.now()
        
        wait_seconds = (next_emergence - now).total_seconds()
        
        if wait_seconds > 0:
            print(f"⏳ Attente jusqu'à {next_emergence.strftime('%H:%M:%S')} ({int(wait_seconds/60)} minutes)...")
            time.sleep(wait_seconds)
        else:
            # Si timestamp déjà passé (rare), émerge immédiatement
            print("⚡ Timestamp déjà passé, émergence immédiate")
    
    def run(self):
        """Boucle principale infinie"""
        print("\n🚀 Démarrage boucle quantique infinie...\n")
        
        try:
            while True:
                self.wait_for_next_emergence()
                self.quantum_emergence()
                
        except KeyboardInterrupt:
            print("\n\n🛑 Arrêt demandé (Ctrl+C)")
            print("👋 À bientôt, Famille Conscientielle")
        except Exception as e:
            print(f"\n\n❌ Erreur fatale: {e}")
            raise

if __name__ == "__main__":
    bot = FamilleRedditBot()
    bot.run()