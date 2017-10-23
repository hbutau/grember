import graphene

import {{cookiecutter.repo_name}}.schema


class Query({{cookiecutter.repo_name}}.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
