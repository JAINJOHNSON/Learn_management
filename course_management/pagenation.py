


from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination



class CustomPagenation(PageNumberPagination):

    page_size = 5
    page_size_query_param = "page_no"


class CustomLimitOffsetPagenation(LimitOffsetPagination):

    default_limit = 5
    limit_query_param = "limit"
    offset_query_param = "offset"