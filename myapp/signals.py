from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from myapp.models import Item_Information, ItemAttribute, Supplier, Customer, Stockin, Stockout, Adjust  # Import your models here

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    # Define all permissions to be created with the associated models
    permissions = [
        ("create_item", "Can create item", Item_Information),
        ("edit_item", "Can edit item", Item_Information),
        ("delete_item", "Can delete item", Item_Information),
        ("create_attribute", "Can create attribute", ItemAttribute),
        ("edit_attribute", "Can edit attribute", ItemAttribute),
        ("delete_attribute", "Can delete attribute", ItemAttribute),
        ("create_partner", "Can create partner", Supplier),
        ("edit_partner", "Can edit partner", Supplier),
        ("delete_partner", "Can delete partner", Supplier),
        ("create_stockin", "Can create stock in", Stockin),
        ("create_stockout", "Can create stock out", Stockout),
        ("create_adjust", "Can create adjust", Adjust),
    ]

    # Create or update permissions
    for codename, name, model in permissions:
        content_type = ContentType.objects.get_for_model(model)
        Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)

    # Define groups and their permissions
    groups_permissions = {
        'ItemManager': ['create_item', 'edit_item', 'delete_item'],
        'AttributeManager': ['create_attribute', 'edit_attribute', 'delete_attribute'],
        'PartnerManager': ['create_partner', 'edit_partner', 'delete_partner'],
        'StockinUser': ['create_stockin'],
        'StockoutUser': ['create_stockout'],
        'AdjustUser': ['create_adjust'],
    }

    # Create or update groups and assign permissions
    for group_name, perms in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm in perms:
            codename, model = next((p[0], p[2]) for p in permissions if p[0] == perm)
            content_type = ContentType.objects.get_for_model(model)
            permission = Permission.objects.get(codename=perm, content_type=content_type)
            group.permissions.add(permission)
