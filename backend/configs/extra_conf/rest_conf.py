REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'core.permissions.user_permissions.IsSuperUser',
        'core.permissions.user_permissions.IsOwnerPermissionOrReadOnly',
        'core.permissions.user_permissions.IsOwnerPermission',
    ],
    'EXCEPTION_HANDLER': 'core.handlers.error_handler.error_handler'
}
