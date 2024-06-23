from flask import request

def get_params (*keys):
    results = {}
    
    for key in set(keys):
        value = request.args.get(key)
        
        if not isinstance(key, str):
            raise Exception(f"data type of key must be string, but '{ type(key) }' received !")
        if not value:
            raise Exception (f"parameter '{ key }' is doesn't passed")
        if len(keys) == 1:
            return value
        results[key] = value
        
    return results

def get_post (*keys):
    results = {}
    for key in set(keys):
        form = request.form
        if not form[key]:
            raise Exception(f"the value of '{ key }' is doesn't exists!")
        if len(keys) == 1:
            return form[key]
        results[key] = form[key]
        
    return results