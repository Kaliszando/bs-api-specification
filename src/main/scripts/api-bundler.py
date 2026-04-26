import os
import yaml

def sort_key(item):
    schema_name, schema_content = item

    x_order = float('inf')

    if isinstance(schema_content, dict):
        if 'x-order' in schema_content:
            try:
                x_order = int(schema_content['x-order'])
            except (ValueError, TypeError):
                x_order = float('inf')

    return x_order, schema_name

def read_directory(directory):
    data = {}
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as file:
            content = yaml.safe_load(file)
            data.update(content)
    return data


def read_directory_recursive(directory, prefix=''):
    data = {}
    
    try:
        entries = sorted(os.listdir(directory))
    except FileNotFoundError:
        return data
    
    for entry in entries:
        full_path = os.path.join(directory, entry)
        
        if os.path.isdir(full_path):
            dir_prefix = entry.capitalize() if not prefix else prefix + '_' + entry.capitalize()
            sub_data = read_directory_recursive(full_path, dir_prefix)
            data.update(sub_data)
        elif entry.endswith('.yaml') or entry.endswith('.yml'):
            try:
                with open(full_path, 'r') as file:
                    content = yaml.safe_load(file)
                    if content:
                        key_name = entry.replace('.yaml', '').replace('.yml', '')
                        if prefix:
                            key_name = prefix + '__' + key_name
                        
                        if isinstance(content, dict):
                            if len(content) > 1 or list(content.keys())[0] != key_name:
                                data.update(content)
                            else:
                                data[key_name] = content[key_name] if key_name in content else content
                        else:
                            data[key_name] = content
            except Exception as e:
                print(f"Warning: Could not read {full_path}: {e}")
    
    return data


def read_directory_sorted(directory):
    data = read_directory_recursive(directory)
    return dict(sorted(data.items(), key=sort_key))


def generate_openapi_spec(paths_directory, schemas_directory, output_file):
    with open('../openapi-template.yaml', 'r') as template_file:
        template = yaml.safe_load(template_file)
    template['paths'] = read_directory(paths_directory)
    template['components']['schemas'] = read_directory_sorted(schemas_directory)

    with open(output_file, 'w') as file:
        yaml.dump(template, file, sort_keys=False)


generate_openapi_spec('../paths', '../schemas', '../openapi.yaml')
