def measure_depth(data, depth_data, level=1):
    if not isinstance(data, dict) or not data:
        return depth_data
    for key in data:
        depth_data.append(f"{key} {level}")
        measure_depth(data[key], depth_data, level+1)
    return depth_data


def print_depth(data):
    depth_data = measure_depth(data, [])
    for data in depth_data:
        print(data)


if __name__ == '__main__':
    the_dict = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }
    print_depth(the_dict)

