class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append (self)
        
        @property
        def pet_type(self):
            return self._pet_type
        
        @pet_type.setter
        def pet_type (self, pet_type):
            if pet_type not in Pet.PET_TYPES:
                raise ValueError ("Invalid type")
            self._pet_type = pet_type
            
    # pass

class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all]
    
    def add_pet(Self, pet):
        if not isinstance(pet, Pet):
            raise ValueError ("Must be a pet")
        pet.owner = Self
        
    def get_sorted_pets(self):
        return sorted (self.pets(), key = lambda pet : pet.name)    
    # pass