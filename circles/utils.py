from circles.models import Circle, CircleUser
from django.utils.text import slugify


def create_circle(circle_name, added_by_user):
    '''
    :param circle_name: str - Name of the circle to be created
    :param added_by_user: User object - User that will be 
    related to the circle and circle user.
    :return: Returns a Circle and CircleUser objects as a tuple

    
    Creates a Circle and a CircleUser.
    Slugifies the parameter circle_name for the field Circle.slug

    The user passed as parameter added_by_user will be set 
    as a manager by setting the field CircleUser.is_manager to True.

    '''
    circle = Circle.objects.create(
        name=circle_name,
        slug=slugify(circle_name),
        added_by=added_by_user
        )
    
    circle_user = CircleUser.objects.create(
        circle=circle,
        user=added_by_user,
        can_manage=True
    )
    return circle, circle_user
