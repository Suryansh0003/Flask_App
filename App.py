from flask import Flask,request

App = Flask(__name__)

# create the idea repositry
ideas = {
    1: {
        "id": 1,
        "idea_name": "Generate the random data ",
        "idea_disct": "paas",
        "idea_author": "Suryansh",
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
    return ideas

"""
Create the RESTful endpoint for creating the ideas 
"""
@App.post("/ideaapp/api/v1/ideas")
def create_idea():
    try:
        request_body=request.get_json()

        if request_body["id"] and request_body["id"] in ideas:
            return "ideas with the same id is already exists",400 
        
        ideas[request_body["id"]]=request_body
        
        return "created and saved successfully ",201
    except KeyError:
        return "id key is missing "
    
    except :
        return "internal error"
    


if __name__ == "__main__":
    App.run(port=8080)
