class Pizza:
    '''
    Pizza class to define Pizza Objects
    '''

    def __init__(self,id,title,overview,image,vote_average,vote_count):
        self.id = id
        self.title= title
        self.overview = overview
        self.vote_average = vote_average
        self.vote_count = vote_count
