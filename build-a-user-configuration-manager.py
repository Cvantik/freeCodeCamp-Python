
def add_setting(settings: dict, key_value: tuple):
    key = key_value[0].lower()
    val = key_value[1].lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = val
    
    return f"Setting '{key}' added with value '{val}' successfully!"

def update_setting(settings: dict, key_value: tuple):
    # key and val, converted to lower case
    key = key_value[0].lower()
    val = key_value[1].lower()
    
    if key in settings:
        settings[key] = val
        return f"Setting '{key}' updated to '{val}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key: str):
    key = key.lower()

    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(settings: dict):
    
    if not settings:
        return "No settings available."
    
    out = "Current User Settings:\n"
    
    for key in settings:
        out += f"{key.capitalize()}: {settings[key]}\n"
    
    return out
    
test_settings = {
    'theme': 'light', 
    'volume': 'high'
 }

print(view_settings(test_settings))


