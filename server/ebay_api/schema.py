import graphene

from django.conf import settings

from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError


class SearchResultType(graphene.ObjectType):
    title = graphene.String()
    price = graphene.String()


class Query(graphene.ObjectType):
    search = graphene.List(SearchResultType,
                            argument=graphene.String(required=True))

    def resolve_search(root, info, argument):
        try:
            api = Finding(
                appid=settings.APPID, config_file=None)
            response = api.execute('findItemsAdvanced', {'keywords': argument})
        except ConnectionError as e:
            print(e)

        result = []
        for item in response.dict().get("searchResult", {}).get("item"):
            title = item.get("title")
            
            price_data = item.get("sellingStatus", {}).get("currentPrice", {})
            currency = price_data.get("_currencyId")
            price = price_data.get("value")

            result.append({
                "title": title,
                "price": f"{price} {currency}",
            })

        return result
