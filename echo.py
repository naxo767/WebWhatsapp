	
# -*- coding: utf-8 -*-
import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

def dump(obj):
   for attr in dir(obj):
       if hasattr( obj, attr ):
           print( "obj.%s = %s" % (attr, getattr(obj, attr)))
           
driver = WhatsAPIDriver(client="chrome")
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

message = u"Estamos haciendo una investigación en la UPM para analizar los modelos de comportamiento, nos ayudaría mucho si respondieras, son solo 8 minutos!"
Formularios = [ 
   "https://docs.google.com/forms/d/e/1FAIpQLSdUO9BqMn2uAXnmzwg9iLoihMqfr8w_y6VbzxHKyu0Q9DPOmw/viewform",
   "https://docs.google.com/forms/d/e/1FAIpQLSeN6sCFRrpqeOCndm09zGadOhAwn_yOmsSQuuc9-0qQxmJuUw/viewform"  
   ]
destinatarios = [     
  "Cristina Luna", "Juan"    
]    
num_messages = 0
p_form = 0
#for contact in driver.get_contacts():
for chat in driver.get_all_chats():
    # Se trabaja con chats ya que no se puede enviar mensajes a contactos cuyos chats no estén "abiertos"
    #dump(chat) # Necesario para conocer las propiedades y metodos del objeto chat
    if chat._js_obj['isGroup'] == False: # Solo trabajamos con chats NO grupales
        print(chat._js_obj['name'])
        if chat._js_obj['name'] in destinatarios:
            print("\n[CONTACT %d][%s][FORMULARIO %d][%s]" % (num_messages,
                  chat._js_obj['name'],
                  p_form,
                  Formularios[p_form]))
    
            chat.send_message(message)
            chat.send_message('Formulario: '+Formularios[p_form])
        
            print(message)
            print('Formulario: '+Formularios[p_form])
            
    
            p_form = p_form + 1
    
            if p_form >= 4: # vamos asignando formularios secuencialmente
                p_form = 0 # al agotar los 20 disponibles volvemos a asignar desde el primero
            
            num_messages = num_messages + 1
       
       


    #if contact.formatted_name in destinatarios:    
        #print(contact.short_name)
        #if contact.short_name == u"María Del Mar":
            #print("ENVIANDO MENSAJE A ", contact.short_name)
            #chat = contact.get_chat()
        #chat.send_message(message.encode('latin-1'))
        #for form in Formularios:
            #chat.send_message(form)
        #chat.send_message(Formularios[0])
    
while True:
    time.sleep(3)
    print('Checking for more messages')
    #for contact in driver.get_unread():
    #    for message in contact.messages:
    #        if isinstance(message, Message): # Currently works for text messages only.
    #            contact.chat.send_message(message.safe_content)
