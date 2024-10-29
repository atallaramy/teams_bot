from botbuilder.core import ActivityHandler, MessageFactory, TurnContext


class SimpleBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        text = turn_context.activity.text.lower()
        if text == "how are you?":
            options = ["I'm fine, how about you?", "Let's talk later."]
            await turn_context.send_activity(MessageFactory.suggested_actions(options))
        else:
            await turn_context.send_activity("I'm here to chat!")
