"""DjangoRestFramework Auth0 Views."""


class GroupsQuerysetFilterMixin():
    """
    Filter a queryset based on the groups asociated to the model instance...

    Filter the queryset defined in the viewset based on the groups asociated to
    user in Auth0 authorization plugin

    -If authorization groups exists in the payload and in the model we're
    filtering, this function returns all the instances of the model that the
    current user can access to .
    -If authorization groups exists in the payload but not in the attrib in the
    model, none (empty array) is returned.
    """

    def get_queryset(self):
        """
        Filter the queryset of a view by an specific group...

        Filter the get queryset to show only instances asociated with an
        specific group.
        """
        original_queryset = self.queryset
        try:
            queryset = original_queryset.filter(
                groups__in=self.request.user.groups.all()
            )

        except Exception as e:
            queryset = []

        return queryset
