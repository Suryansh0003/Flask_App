from flask import Flask

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


if __name__ == "__main__":
    App.run(port=8080)
