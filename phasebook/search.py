from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    
    search_result = []

    for user in USERS:
        if (args.get("id") is not None and user.get("id") == args.get("id")) or \
           (args.get("name") is not None and args.get("name").lower() in user.get("name").lower()) or \
           (args.get("age") is not None and abs(user.get("age") - int(args.get("age"))) <= 1) or \
           (args.get("occupation") is not None and args.get("occupation").lower() in user.get("occupation").lower()):
            search_result.append({
                "id": user["id"],
                "name": user["name"],
                "age": user["age"],
                "occupation": user["occupation"]
            })

    return search_result
