class ObjectChar:
    '''An object class for the identified objects.'''
    name = "noname"
    gender = "genderless"
    ageGroup = "ageless"
    personality = "nopersonality"
    appearance = "nothing"
    voice = "novoice"

    def __init__(self, name, gender, ageGroup, personality, appearance, voice):
        '''Constructor'''
        self.name = name
        self.gender = gender
        self.ageGroup = ageGroup
        self.personality = personality
        self.appearance = appearance
        self.voice = voice