class Album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track
    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play
        

def solution(genres, plays):
    answer = []
    album_cnt = {}
    album_list = []
    
    for i in range(len(genres)):
        album_cnt[genres[i]] = album_cnt.get(genres[i], 0) + plays[i]
        album_list.append(Album(genres[i], plays[i], i))
    
    album_cnt = sorted(album_cnt.items(), key=lambda x: -x[1])
    album_list = sorted(album_list, reverse=True)
    
    while len(album_cnt) > 0:
        g = album_cnt.pop(0)
        cnt = 0
        for al in album_list:
            if g[0] == al.genre:
                answer.append(al.track)
                cnt += 1
            if cnt == 2:
                break
    
    return answer