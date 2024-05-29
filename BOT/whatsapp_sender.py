from twilio.rest import Client

# En desarrollo: Notificaciones por Whatsapp

# Tus credenciales de Twilio
account_sid = '' 
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Nueva oportunidad',
  to='whatsapp:+598' # Tu numero de Whatsapp
)

print(message.sid)