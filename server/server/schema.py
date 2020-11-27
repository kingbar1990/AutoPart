import graphene

from ebay_api.schema import Query as EbayApiQuery

class Query(EbayApiQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query) # , mutation=Mutation)