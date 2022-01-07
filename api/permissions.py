from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Permitie al usuario editar su propio perfil """

    def has_object_permission(self, request, view, obj):
        """ Verificar si usuario esta intentando editar su propio perfil """

        if request.method in permissions.SAFE_METHODS:
            return True

        # return obj.owner == request.user
        return obj.id == request.user.id