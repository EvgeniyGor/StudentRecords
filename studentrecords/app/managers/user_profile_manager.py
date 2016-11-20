from django.db import models
from django.contrib.auth.models import UserManager


class UserProfileManager(models.Manager):
    def filter(self, *args, **kwargs):

        def filter_condition(profile):

            profile_fields = profile.__dict__.items()
            user_fields = profile.user.__dict__.items()

            # merge profile and user fields dicts
            fields = dict(profile_fields + user_fields +
                          [(k, profile_fields[k] + user_fields[k])
                           for k in set(profile_fields) & set(user_fields)])

            for arg_name, arg_value in kwargs.items():
                if arg_name not in fields:
                    continue

                if arg_value != fields[arg_name]:
                    return False

            return True

        return list(filter(filter_condition, super(UserProfileManager, self).all()))

    def get_by_login(self, login):
        return super(UserProfileManager, self).get(username=login)

    def create(self, username, password, email, **kwargs):

        user_manager = UserManager()

        user = user_manager.create_user(username=username, password=password, email=email)
        user.first_name = kwargs.get('first_name')
        user.last_name = kwargs.get('last_name')
        user.is_superuser = kwargs.get('is_superuser', False)
        user.save()

        user_profile = self.create(
            user=user,
            patronymic=kwargs.get('patronymic'),
            birth_date=kwargs.get('birth_date'),
            study_group=kwargs.get('study_group'),
            github_id=kwargs.get('github_id'),
            stepic_id=kwargs.get('stepic_id'),
            role=kwargs.get('role', 's'),
            election_date=kwargs.get('election_date'),
            position=kwargs.get('position'),
            contract_date=kwargs.get('contract_date'),
            academic_degree=kwargs.get('academic_degree'),
            year_of_academic_degree=kwargs.get('year_of_academic_degree'),
            academic_status=kwargs.get('academic_status'),
            year_of_academic_status=kwargs.get('year_of_academic_status')
        )

        user_profile.save()

        return user_profile
