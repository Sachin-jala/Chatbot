from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower()

        #Simple rule-based bot
        if "hello" in user_message:
            reply = "Hi there! 👋 How can I help you today?"
        elif "bye" in user_message:
            reply = "Goodbye! 👋 Have a grate day!"
        elif "name" in user_message:
            reply = "I'M yoour frendly ChatBot Parth 🤖"
        else:
            reply = "Hmm... I'm not sure I understand 🤔"

        return JsonResponse({"reply": reply})
    return JsonResponse({"error": "POST request required"},
status = 400)
