if __name__ == "__main__":

    pokemon_types = {
        #Key  :  Value
        'Pikachu': 'electric',
        'Bulbasaur': 'grass',
        'Charmanader': 'fire'

    }
    pokemon_types['Mew'] = 'psychic'
    print(pokemon_types)

    pokemon_type_pair = (
        ('Pikachu', 'electric'),
        ('Bulbasaur', 'grass'),
        ('Charmander', 'fire')
    )
    pokemon_types_from_tuple = dict(pokemon_type_pair)
    print(pokemon_types_from_tuple)