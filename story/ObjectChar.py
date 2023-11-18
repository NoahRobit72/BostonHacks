# Reference: https://github.com/huangsam/ultimate-python/blob/master/ultimatepython/classes/basic_class.py
class ObjectChar:
    '''An object class for the identified objects.'''
    def __init__(self, name, gender, ageGroup, personality, appearance, voice):
        '''Constructor'''
        self.name = name
        self.gender = gender
        self.ageGroup = ageGroup
        self.personality = personality
        self.appearance = appearance
        self.voice = voice

    """ Potentially for dubgging
    def __repr__(self):
        '''Formal representation for developers.'''
        return f"<Name={self.name} ageGroup={self.ageGroup} personality={self.personality} appearance={self.appearance} voice={self.voice}>"
    def __str__(self):
        '''Informal representation for users.'''
        return f"{self.name} {self.ageGroup} {self.personality} {self.appearance} {self.voice}"
    """
