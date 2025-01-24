from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination, CursorPagination
from rest_framework.request import Request

class DefaultLimitOffsetPagination(LimitOffsetPagination):
    """
    A custom LimitOffsetPagination class that enforces minimum and maximum limits
    for pagination. This ensures that the limit parameter passed in the query
    is within the specified bounds.

    Attributes:
        min_limit (int): The minimum allowed limit for pagination.
        max_limit (int): The maximum allowed limit for pagination.
        default_limit (int): The default limit if none is provided in the request.
    """

    min_limit: int = 1
    max_limit: int = 100
    default_limit: int = 10

    def get_limit(self, request: Request) -> int:
        """
        Override the `get_limit` method to enforce minimum and maximum limits.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            int: The limit to be used for pagination. This will be within the
                 specified min_limit and max_limit bounds.
        """
        if self.limit_query_param and request.query_params.get(self.limit_query_param):
            try:
                limit_value = request.query_params.get(self.limit_query_param)
                
                # Skip if the limit value is non-numeric (e.g., alphabetic)
                if limit_value.isalpha():
                    pass
                # Ensure the limit is greater than 0 and within the allowed range
                elif int(limit_value) > 0:
                    return min(max(int(limit_value), self.min_limit), self.max_limit)
            except (KeyError, ValueError):
                pass

        # Return the default limit if no valid limit is provided
        return self.default_limit


class DefaultPageNumberPagination(PageNumberPagination):
    """
    A custom PageNumberPagination class that allows clients to control the page size
    via query parameters. It enforces a maximum page size to prevent excessive data retrieval.

    Attributes:
        page_size (int): The default page size if none is provided.
        page_size_query_param (str): The query parameter used to control the page size.
        max_page_size (int): The maximum allowed page size.
    """

    page_size: int = 10
    page_size_query_param: str = 'page_size'
    max_page_size: int = 100

    def get_page_size(self, request: Request) -> int:
        """
        Override the `get_page_size` method to enforce a maximum page size.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            int: The page size to be used for pagination. This will be within the
                 specified max_page_size bound.
        """
        if self.page_size_query_param and request.query_params.get(self.page_size_query_param):
            try:
                page_size_value = request.query_params.get(self.page_size_query_param)
                
                # Skip if the page size value is non-numeric (e.g., alphabetic)
                if page_size_value.isalpha():
                    pass
                # Ensure the page size is greater than 0 and within the allowed range
                elif int(page_size_value) > 0:
                    return min(int(page_size_value), self.max_page_size)
            except (KeyError, ValueError):
                pass

        # Return the default page size if no valid page size is provided
        return self.page_size


class DefaultCursorPagination(CursorPagination):
    """
    A custom CursorPagination class that uses a cursor-based approach for pagination.
    It ensures consistent and efficient pagination for large datasets by ordering
    results based on a specific field (e.g., `id`).

    Attributes:
        page_size (int): The default page size if none is provided.
        page_size_query_param (str): The query parameter used to control the page size.
        max_page_size (int): The maximum allowed page size.
        ordering (str): The field used for ordering results (default is `-id`).
    """

    page_size: int = 10
    page_size_query_param: str = 'page_size'
    max_page_size: int = 100
    ordering: str = '-id'

    def get_page_size(self, request: Request) -> int:
        """
        Override the `get_page_size` method to enforce a maximum page size.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            int: The page size to be used for pagination. This will be within the
                 specified max_page_size bound.
        """
        if self.page_size_query_param and request.query_params.get(self.page_size_query_param):
            try:
                page_size_value = request.query_params.get(self.page_size_query_param)
                
                # Skip if the page size value is non-numeric (e.g., alphabetic)
                if page_size_value.isalpha():
                    pass
                # Ensure the page size is greater than 0 and within the allowed range
                elif int(page_size_value) > 0:
                    return min(int(page_size_value), self.max_page_size)
            except (KeyError, ValueError):
                pass

        # Return the default page size if no valid page size is provided
        return self.page_size