# teams/services.py
from django.db import transaction
from django.db.models import F
from django.utils import timezone
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Team, Submission


def record_submission(team_code: str, device_ts=None) -> Submission:
    now = timezone.now()
    with transaction.atomic():
        # Lock the team row to prevent race conditions
        team = Team.objects.select_for_update().get(code=team_code)

        # Increment their level atomically
        Team.objects.filter(pk=team.pk).update(current_level=F('current_level') + 1)
        team.refresh_from_db(fields=['current_level'])

        # Create or update the Submission row for that team
        submission, created = Submission.objects.select_for_update().get_or_create(
            team=team,
            defaults={
                'team_code': team.code,
                'level_after': team.current_level,
                'device_submitted_at': device_ts or now,
            },
        )
        if not created:
            submission.level_after = team.current_level
            submission.device_submitted_at = device_ts or now
            submission.save(update_fields=['level_after', 'device_submitted_at', 'last_submitted_at'])

    # After commit, broadcast leaderboard update via Channels
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'leaderboard',  # the group name that all clients subscribe to
        {
            'type': 'leaderboard.update',  # event type handled by consumer
            'data': {
                'team': team.name,
                'team_code': team.code,
                'questions_solved': team.current_level,
                'ts': now.isoformat(),
            },
        },
    )

    return submission
