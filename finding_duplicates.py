# RangaD
print("RanugaD")
list_given = [1,2,2,3,3,3,3,2,5,6,56]


def find_duplicate(head: list) -> "A List without any duplicate number":
    copied_list = head.copy()
    new_list = []
    duplicate_number_dict = {}
    for a in copied_list:
        duplicate_number_dict[a] = 0
    already_exist_numbers = []
    duplicate_number = []
    for number in copied_list:
        if number in already_exist_numbers:
            duplicate_number_dict[number] = duplicate_number_dict[number] + 1
            if number in duplicate_number:
                pass
            else:
                duplicate_number.append(number)
        new_list.append(number)
        already_exist_numbers.append(number)
    return {
        "Duplicated Numbers": duplicate_number,
        "Duplicated Number Of Times": duplicate_number_dict,
    }


print(find_duplicate(list_given))
print("RanugaD")
# RangaD
