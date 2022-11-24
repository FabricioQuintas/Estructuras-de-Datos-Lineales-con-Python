from random import randint
from node_based_queue import Queue
from time import sleep


class Track:
    def __init__(self, title=None):
        self.title = title
        self.lenght = randint(5,6)

    
class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)
    
    def play(self):
        '''
        Play all songs of the Queue
        '''
        print(f'Count: {self.count}')
        while self.count > 0 and self.head != None:
            current_track_node = self.dequeue()
            print(f'Now playing {current_track_node.title}')
            sleep(current_track_node.lenght)
    

if __name__ == '__main__':
    quantity = int(input('How many songs do you want to add to the queue?: '))
    myPlayList = MediaPlayerQueue()

    for i in range(quantity):
        data = input(f'Say the name of the song number {i+1} item: ')
        myPlayList.enqueue(Track(data))

    myPlayList.play()