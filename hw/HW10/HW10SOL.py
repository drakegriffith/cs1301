

class Video :
    def __init__(self, sound, minutes=1.0, likes=0, comments=0) :
        self.sound = sound
        self.minutes = minutes
        self.likes = likes
        self.comments = comments
    def __repr__(self): #provided
        return f"Video({self.sound}, {self.likes}, {len(self.comments)}, {self.minutes})"

    def __str__ (self) :
        return "Video has {} likes and is {} minutes long.".format(
            self.likes, self.minutes)
    def __eq__ (self, other) :
        return self.sound == other.sound and self.comments == other.comments


class Account :
    def __init__ (self, username, password, isPrivate=True) :
        self.username = username
        self.password = password
        self.followers = []
        self.following = []
        self.videos = []
        self.isPrivate = isPrivate
    def __repr__(self): #provided
        return f"Account({self.username}, {self.password}, {len(self.followers)}, {len(self.following)}, {len(self.videos)}, {self.isPrivate})"
    def __lt__ (self, other) :
        return len(self.videos) < len(other.videos)
    def __eq__ (self, other) :
        return self.username == other.username and self.password == other.password
    def changePassword (self, oldPassword, newPassword):
        if oldPassword != self.password :
            return "Invalid password."
        else :
            self.password = newPassword
    def isInfluencer (self) : #Edit
        if len(self.videos) > 4 :
            check = 0
            for videos in self.videos :
                if videos.likes > 50000 and videos.comments > 1000 :
                    check += 1
            if check > 4 and self.isPrivate == False :
                return True
            else :
                return False
    def follow (self, followedAccount) :
        test = True
        for runCheck in self.following :
            if followedAccount == runCheck :
                test = False
        if test == True :
            self.following.append(followedAccount)
            followedAccount.followers.append(self)
     
    def unfollow (self, unfollowedAccount) :
        if unfollowedAccount in self.following :
            self.following.remove(unfollowedAccount)
            unfollowedAccount.followers.remove(self)
        else :
            pass


class TikTok :
    def __init__(self): #provided
        self.accounts = []
        self.followers = []
        self.following = []
        self.videos = []
        self.soundBase = []
    def __repr__(self): #provided
        return f"TikTok Object with {len(self.accounts)} accounts and {len(self.videos)} videos"
    def makeAccount(self, username, password) :
        tup = (),
        for account in self.accounts :
            if account.username == username :
                return "Username is already taken."
        newAcct = Account(username, password)
        self.accounts.append(newAcct)
        tup = (newAcct.username, newAcct.followers)
        self.followers.append(tup)

        tup = (newAcct.username, newAcct.following)
        self.following.append(tup)

    def changePrivacy(self, account_object) :
        if account_object.isPrivate == True :
            account_object.isPrivate = False
        elif account_object.isPrivate == False :
            account_object.isPrivate = True
    def deleteAccount(self, account_object) :
        for account in self.accounts :
            if account_object.username == account.username :
                self.accounts.remove(account_object)
                for i in self.followers :
                    if i == (account_object.username, account_object.followers) :
                        self.followers.remove(i)
                for i in self.following :
                    if i == (account_object.username, account_object.following) :
                        self.following.remove(i)
                          
    def post(self, account_object, sound, minutes) :
        for account in self.accounts :
            if account.username == account_object.name :
                if minutes < .25 :
                    return "Video must be at least 15 seconds."
                else :
                    newvideo = Video(sound, minutes)
                    account_object.videos.append(newvideo)
                    self.videos.append(newvideo)
            else :
                return "You must have a registered account to post."
    def getInfluencers(self) :
        li = []
        for accounts in self.accounts :
            if accounts.isInfluencer() == True and len(accounts.videos) > 4:
                li.append(accounts)
            else :
                pass
        return li
    
            
