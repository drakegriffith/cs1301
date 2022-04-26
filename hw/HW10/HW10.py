class Video:
    def __repr__(self): #provided
        return f"Video({self.sound}, {self.likes}, {len(self.comments)}, {self.minutes})"
    
class Account:
    def __repr__(self): #provided
        return f"Account({self.username}, {self.password}, {len(self.followers)}, {len(self.following)}, {len(self.videos)}, {self.isPrivate})"

class TikTok:
    def __init__(self): #provided
        self.accounts = []
        self.followers = []
        self.following = []
        self.videos = []
        self.soundBase = []
    
    def __repr__(self): #provided
        return f"TikTok Object with {len(self.accounts)} accounts and {len(self.videos)} videos"
        
            
