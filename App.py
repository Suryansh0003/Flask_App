from flask import Flask, request

App = Flask(__name__)

# create the idea repositry
ideas = {
    1: {
        "id": 1,
        "idea_name": "Generate the random data ",
        "idea_disct": "paas",
        "idea_author": "Rahul",
    },
    2: {
        "id": 2,
        "idea_name": "create a intractive plot",
        "idea_disct": "Intractive plot using plotly and metpoletleb",
        "idea_author": "Suryansh",
    },
}

"""
create an restful endpoint for fetecing the ideas 
"""


@App.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    # logic to fetech all the ideaa
    # I need to read quairy param
    idea_author = request.args.get("idea_author")
    # Logic to fetch all the ideas and support query params
    if idea_author:
        # Filter the ideas created by this author
        idea_res = {}
        for key, values in ideas.items():
            if values["idea_author"] == idea_author:
                idea_res[key] = values
        return idea_res
    return ideas


"""
Create the RESTful endpoint for creating the ideas 
"""


@App.post("/ideaapp/api/v1/ideas")
def create_idea():
    try:
        request_body = request.get_json()

        if request_body["id"] and request_body["id"] in ideas:
            return "ideas with the same id is already exists", 400

        ideas[request_body["id"]] = request_body

        return "created and saved successfully ", 201
    except KeyError:
        return "id key is missing "

    except:
        return "internal error"


"""
End point to fetch idea based on the idea id
"""


@App.get("/ideaapp/api/v1/ideas/<idea_id>")
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)], 200
        else:
            return "idea id passed in not present ", 400
    except:
        "some internal errror happend", 500

@App.put("/ideaapp/api/v1/ideas/<idea_id>")
def Update_idea(idea_id):
    idea_id=int(idea_id)
    if idea_id not in ideas:
        return "The idea_ID that was passed is not present.",400
    requst_body=request.get_json()
    ideas[idea_id].update(requst_body)
    return "idea updated successfully",200

@App.delete("/ideaapp/api/v1/ideas/<idea_id>")
def Delete_idea(idea_id):
    idea_id=int(idea_id)
    if idea_id not in ideas:
        return "The idea_ID that was passed is not present.",400
    del ideas[idea_id]
    return "idea deleted successfully",200


if __name__ == "__main__":
    App.run(port=8080)
