# --- Binary Search check target exists in field --- #
def exist(target,field):

    if isinstance(field, str):
        if " " in field:
            field = field.split(' ')
            field.sort()
        else:
            field = list(field)
            field.sort()

    elif isinstance(field, tuple):
        field = list(field)
        field.sort()

    elif isinstance(field, list):
        field.sort()

    else:
        raise TypeError('Must contain a list or string')

    upper_range = len(field)
    lower_range = 0

    if isinstance(target, int) and isinstance(target, float) and isinstance(target, str) == False:
        raise TypeError('Search must be either a Int, Float or String')
    
    if target == field[0]:
        return True
    while True:
        try:
            finder = ((upper_range - lower_range) / 2) + lower_range
            finder = int(finder)

            try:

                if field[finder] == target:
                    return True
                    
                elif field[finder] > target:
                        upper_range = finder

                elif field[finder] < target:
                    lower_range = finder
            except TypeError:
                raise TypeError('Target Type is not compatible with Field Type')
            if upper_range - lower_range == 1:
                return False
        except IndexError:
            return False



# --- Binary Search check where a target is located in field--- #
def location(target,field):

    if isinstance(field, str):
        if " " in field:
            field = field.split(' ')
            field.sort()
        else:
            field = list(field)
            field.sort()

    elif isinstance(field, tuple):
        field = list(field)
        field.sort()

    elif isinstance(field, list):
        field.sort()

    else:
        raise TypeError('Must contain a list or string')

    field.sort()
    upper_range = len(field)
    lower_range = 0

    if isinstance(target, int) and isinstance(target, float) and isinstance(target, str) == False:
        raise TypeError('Search must be either a Int, Float or String')
    
    if target == field[0]:
        return 0
    while True:
        try:
            finder = ((upper_range - lower_range) / 2) + lower_range
            finder = int(finder)

            try:

                if field[finder] == target:
                    return finder
                    
                elif field[finder] > target:
                        upper_range = finder

                elif field[finder] < target:
                    lower_range = finder
            except TypeError:
                raise TypeError('Target Type is not compatible with Field Type')
            if upper_range - lower_range == 1:
                return False
        except IndexError:
            return

