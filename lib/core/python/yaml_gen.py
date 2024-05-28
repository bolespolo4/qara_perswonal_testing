import yaml

def load_env():
    try:
        with open('app.env', "r") as f:
            env_vars = {}
            for line in f:
                line = # The code snippet `line.strip()` is used to remove any leading or trailing
                # whitespaces from the `line` read from the file.
                line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    env_vars[key.strip()] = value.strip()
            return env_vars
    except FileNotFoundError:
        print(f"Error: File '{env_file}' not found.")

def generate_yaml(env_vars):
    yaml_structure = {
        'flavors': {
            'qc': {
                'app': {
                    'name': env_vars['APP_NAME']
                },
                'android': {
                    'applicationId': env_vars['QC_ANDROID_APPLICATION_ID'],
                    'firebase': {
                        'config': env_vars['QC_ANDROID_FIREBASE_CONFIG']
                    },
                    'resValues': {
                        'e_point': {
                            'type': env_vars['QC_ANDROID_RES_VALUES_E_POINT_TYPE'],
                            'value': env_vars['QC_ANDROID_RES_VALUES_E_POINT_VALUE']
                        }
                    }
                },
                'ios': {
                    'bundleId': env_vars['QC_IOS_BUNDLE_ID'],
                    'firebase': {
                        'config': env_vars['QC_IOS_FIREBASE_CONFIG']
                    }
                }
            },
            'production': {
                'app': {
                    'name': env_vars['PRODUCTION_APP_NAME']
                },
                'android': {
                    'applicationId': env_vars['PRODUCTION_ANDROID_APPLICATION_ID'],
                    'firebase': {
                        'config': env_vars['PRODUCTION_ANDROID_FIREBASE_CONFIG']
                    },
                    'resValues': {
                        'e_point': {
                            'type': env_vars['PRODUCTION_ANDROID_RES_VALUES_E_POINT_TYPE'],
                            'value': env_vars['PRODUCTION_ANDROID_RES_VALUES_E_POINT_VALUE']
                        }
                    }
                },
                'ios': {
                    'bundleId': env_vars['PRODUCTION_IOS_BUNDLE_ID'],
                    'firebase': {
                        'config': env_vars['PRODUCTION_IOS_FIREBASE_CONFIG']
                    }
                }
            },
            'dev': {
                'app': {
                    'name': env_vars['DEV_APP_NAME']
                },
                'android': {
                    'applicationId': env_vars['DEV_ANDROID_APPLICATION_ID'],
                    'firebase': {
                        'config': env_vars['DEV_ANDROID_FIREBASE_CONFIG']
                    },
                    'resValues': {
                        'e_point': {
                            'type': env_vars['DEV_ANDROID_RES_VALUES_E_POINT_TYPE'],
                            'value': env_vars['DEV_ANDROID_RES_VALUES_E_POINT_VALUE']
                        }
                    }
                },
                'ios': {
                    'bundleId': env_vars['DEV_IOS_BUNDLE_ID'],
                    'firebase': {
                        'config': env_vars['DEV_IOS_FIREBASE_CONFIG']
                    }
                }
            }
        }
    }
    return yaml_structure

def write_yaml(file_path, data):
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

env_file = '.env'
output_file = 'flavorizr.yaml'
env_vars = load_env()
if env_vars != None:

    yaml_data = generate_yaml(env_vars)
    write_yaml(output_file, yaml_data)
    print(f"YAML file has been generated ✅")