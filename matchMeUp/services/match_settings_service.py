'''
Created on Jul 12, 2015

@author: Andrew
'''


class MatchSettingsService():

    def __init__(self, db):
        self._db = db

    def set_attracted_to(self, user, attractions_enum_list):
        for existing in user.attractions:
            existing.delete()
        for attraction_enum in attractions_enum_list:
            user.attractions.create(gender=attraction_enum.name)
        return attractions_enum_list

    def set_seeking(
            self, user, looking_for_enum, exclusivity_enum,
            num_years_below, num_years_above):
        data = {
            'looking_for': looking_for_enum.value,
            'exclusivity': exclusivity_enum.value,
            'years_above': num_years_above,
            'years_below': num_years_below
        }

        if user.seeking:
            user.seeking.set(**data)
        else:
            user.seeking = self._db.Seeking(user=user, **data)

    def set_own_deal_breakers(
            self, user, smokes_enum, drugs_enum, drinks_enum,
            has_kids_enum, living_with_enum):

        data = {
                'smokes': smokes_enum.name,
                'drugs': drugs_enum.name,
                'drinks': drinks_enum.name,
                'has_kids': has_kids_enum.name,
                'living_with': living_with_enum.name
                }
        if user.my_deal_breakers:
            user.my_deal_breakers.set(**data)
        else:
            user.my_dealk_breakers = self._db.MyDealBreakers(user=user, **data)

    def set_match_deal_breakers(
            self, user, smokes_enums, drugs_enums, drinks_enums,
            has_kids_enums, living_with_enums
            ):

        # Get or create table
        table = (
                user.match_deal_breakers or
                self._db.MatchDealBreakers(user=user))

        # Clear existing dealbreakers
        for existing in table.smokes:
            existing.delete()
        for existing in table.drugs:
            existing.delete()
        for existing in table.drinks:
            existing.delete()
        for existing in table.has_kids:
            existing.delete()
        for existing in table.living_with:
            existing.delete()

        # replace with new dealbreakers
        for smokes_enum in smokes_enums:
            table.smokes.create(smokes=smokes_enum.name)
        for drugs_enum in drugs_enums:
            table.drugs.create(drugs=drugs_enum.name)
        for drinks_enum in drinks_enums:
            table.drinks.create(drinks=drinks_enum.name)
        for has_kids_enum in has_kids_enums:
            table.has_kids.create(has_kids=has_kids_enum.name)
        for living_with_enum in living_with_enums:
            table.living_with.create(living_with=living_with_enum.name)
