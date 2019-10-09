from django.core.paginator import Paginator as DjPaginator


class Paginator(DjPaginator):

    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True):
        self.object_list = object_list["info"]
        self._check_object_list_is_ordered()
        self.per_page = int(per_page)
        self.orphans = int(orphans)
        self.allow_empty_first_page = allow_empty_first_page

    def page(self, number):
        return self._get_page(self.object_list["dataList"], number, self)

    @property
    def count(self) -> int:
        return self.object_list["total"]
