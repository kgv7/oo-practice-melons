############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        print("Pairing has been added")

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        print("Code has been updated.")


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "musk")
    all_melon_types.append(musk)
    musk.add_pairing("mint")

    crenshaw = MelonType("cren", 1998, "green", True, True, "cren")
    all_melon_types.append(crenshaw)
    crenshaw.add_pairing("proscuitto")

    casaba = MelonType("cas", 1998, "green", True, True, "cas")
    all_melon_types.append(casaba)
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberry")

    yw = MelonType("yw", 1998, "green", True, True, "yw")
    all_melon_types.append(yw)
    yw.add_pairing("mint")
    
    return all_melon_types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs well with {melon.pairings}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dictionary = {}

    for melon in melon_types:
        if melon.code not in melon_dictionary:
            melon_dictionary[melon.name] = melon.code

    return melon_dictionary

melons_by_id = make_melon_type_lookup(melon_types)
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvest_location, 
                person_harvested):
        """Initialize a melon that has been harvested"""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_location = harvest_location
        self.person_harvested = person_harvested

        self.sellability = False

    
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_location != 3:
            self.sellability = True

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_objects = []
    
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_objects.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_objects.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_objects.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_objects.append(melon_4)

    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_objects.append(melon_5)

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_objects.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_objects.append(melon_7)

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_objects.append(melon_8)

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    melon_objects.append(melon_9)

    return melon_objects

melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""


    for melon in melons:
        melon.is_sellable()
        # print(melon.sellability)
        if melon.sellability == True:
            print(f"Harvested by {melon.person_harvested} from Field {melon.harvest_location} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.person_harvested} from Field {melon.harvest_location} (NOT SELLABLE)")
 




