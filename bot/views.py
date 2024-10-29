from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from botbuilder.core import (
    BotFrameworkAdapter,
    BotFrameworkAdapterSettings,
    TurnContext,
)
from .bot_handler import SimpleBot  # Assuming SimpleBot is in bot_handler.py
import asyncio
import json

# Initialize bot and adapter
bot_settings = BotFrameworkAdapterSettings("MICROSOFT_APP_ID", "MICROSOFT_APP_PASSWORD")
adapter = BotFrameworkAdapter(bot_settings)
bot = SimpleBot()


@csrf_exempt
def message(request):
    if request.method == "POST":
        # Parse incoming JSON from the request
        body = json.loads(request.body.decode("utf-8"))

        # Create an async task to handle the message
        async def handle_message(turn_context: TurnContext):
            await bot.on_turn(turn_context)

        # Process the incoming message with the bot adapter
        task = asyncio.ensure_future(adapter.process_activity(body, "", handle_message))
        try:
            asyncio.get_event_loop().run_until_complete(task)
            return JsonResponse({"status": "Message processed"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"status": "Only POST requests are accepted"})
