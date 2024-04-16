import os
import yaml


def read_directory(directory):
    data = {}
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as file:
            content = yaml.safe_load(file)
            data.update(content)
    return data


def read_directory_sorted(directory):
    data = read_directory(directory)
    return dict(sorted(data.items(), key=sort_key, reverse=False))


def sort_key(item):
    if 'x-order' in item[1]:
        return item[1]['x-order']
    else:
        return 99999


def generate_openapi_spec(paths_directory, schemas_directory, output_file):
    with open('../openapi-template.yaml', 'r') as template_file:
        template = yaml.safe_load(template_file)
    template['paths'] = read_directory(paths_directory)
    template['components']['schemas'] = read_directory_sorted(schemas_directory)

    with open(output_file, 'w') as file:
        yaml.dump(template, file, sort_keys=False)


generate_openapi_spec('../paths', '../schemas', '../openapi.yaml')
