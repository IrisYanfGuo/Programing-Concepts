# Object Oriented Programming

class Song(object):
    def __init__(self,artist,title,duration):
        self._artist = artist
        self._title = title
        self._duration = duration

    def duration(self):
        return self._duration


class Album(object):
    def __init__(self,title):
        self._title = title
        self._songlist= []

    def addSong(self,song):
        self._songlist.append(song)

    def duration(self):
        self._duration = 0
        for x in self._songlist:
            self._duration += x.duration()
        return self._duration



class Library(object):
    def __init__(self,title):
        self._title = title
        self._albumlist= []

    def addAlbum(self,album):
        self._albumlist.append(album)

    def find_by_artist(self,artist):
        result = []
        for x in self._album:
            for y in x._songlist:
                if y._artist == artist:
                    result.append([y._title,y._artist])
        return result




a = Song("jielun","motianlun",300)
b = Song("wangfei","hongcheng",400)
c = Album("AH")
c.addSong(a)
c.addSong(b)
d = Library("AHA")
d.addAlbum(c)
print(d.find_by_artist("jielun"))
print(c.duration())