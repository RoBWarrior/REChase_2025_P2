from channels.generic.websocket import AsyncJsonWebsocketConsumer

class LeaderboardConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('leaderboard', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('leaderboard', self.channel_name)

    async def leaderboard_update(self, event):
        await self.send_json(event['data'])