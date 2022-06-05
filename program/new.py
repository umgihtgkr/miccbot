import pyrogram
import time
import os
from pyrogram import Client, filters

@Client.on_message(filters.command("رتبتي"))
def forward(client, message):
  chat_id = message.chat.id
  user_id = message.from_user.id
  rank = app.get_chat_member(chat_id, user_id)
  rank = rank.status
  if rank == "administrator":
   app.send_message(chat_id,"مسؤال")
  elif rank == "creator":
   app.send_message(chat_id,"المنشئ يعم")
  elif rank == "member":
   app.send_message(chat_id,"عضو زليل")
  elif rank == "restricted":
   app.send_message(chat_id,"عضو متقيد")
  elif rank == "left":
   app.send_message(chat_id,"انتا مغادر يعم")
  elif rank == "kicked":
   app.send_message(chat_id,"الراجل ده واخد بالجزمه ومحظور")