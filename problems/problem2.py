class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def measure_depth(data, depth_data, level=1):
    object_type = type(data)
    if object_type not in (dict, Person) or not data:
        return depth_data
    if object_type == Person:
        data = data.__dict__
    for key in data:
        depth_data.append(f"{key} {level}")
        measure_depth(data[key], depth_data, level+1)
    return depth_data


def print_depth(data):
    depth_data = measure_depth(data, [])
    for data in depth_data:
        print(data)


if __name__ == '__main__':
    person_a = Person("A", "B", "C")
    person_b = Person("E", "F", {"mega": 5})

    the_dict = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": person_a,
                "key6": person_b
            }
        }
    }

    print_depth(the_dict)
