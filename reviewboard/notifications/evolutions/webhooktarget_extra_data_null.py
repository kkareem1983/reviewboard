from django_evolution.mutations import ChangeField


MUTATIONS = [
    ChangeField('WebHookTarget', 'extra_data', initial=None, null=True)
]
