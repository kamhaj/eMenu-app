from django.utils import timezone
from django.core.mail import send_mass_mail
from django.core.management import BaseCommand
#from django.utils.timezone import make_aware
from django.contrib.auth.models import User

from eMenu.models import Dish



class Command(BaseCommand):
    help = "Send Today's Orders Report to Admins"

    ## method run when email_report custom command is invoked
    def handle(self, *args, **options):
        # get dates range
        date_to = timezone.now()    # not naive, it include timezone stamp
        date_from = date_to - timezone.timedelta(days=1)

        # get all application users
        users = User.objects.all()
        users_email_list = [user.email for user in users]

        # get all dishes updated withing last 24 hours (inclding brand new dishes)
        dishes_updated_in_last_24hours = Dish.objects.filter(edition_date__range=[date_from, date_to])  # TODO check timezone issues?
        
        # if there are no users or not a single dish has changes withing last 24 hours 
        if not dishes_updated_in_last_24hours:
            # do nothing
            self.stdout.write("No dishes were changed withing the last 24 horus.")
        else:
            message = "Dishes that have changes withing last 24 hours: \n"

            for dish in dishes_updated_in_last_24hours:
                message += f"{dish} \n"

            subject = (
                f"Order Report for {date_to.strftime('%Y-%m-%d')} "
                f"to {date_from.strftime('%Y-%m-%d')}"
            )

            #  send mass mail; it uses a single connection for all of its messages
            messages = (
               'Notification on updated dishes',
                message,
                'eMenuApp@example.com',
                users_email_list
            )
            sent = send_mass_mail((messages,), fail_silently=False)
            self.stdout.write("Changed dishes detected. E-mail report was sent.")
            return 0
            