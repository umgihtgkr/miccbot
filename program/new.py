import pyrogram
import time
import os
from pyrogram import Client, filters

@Client.on_message(filters.command("رتبتي"))
def forward(client, message):
  chat_id = message.chat.id
  user_id = message.from_user.id
  rank =  await.get_chat_member(chat_id, user_id)
  rank = rank.status
  if rank == "administrator":
    await.send_message(chat_id,"مسؤال")
  elif rank == "creator":
    await.send_message(chat_id,"المنشئ يعم")
  elif rank == "member":
    await.send_message(chat_id,"عضو زليل")
  elif rank == "restricted":
    await.send_message(chat_id,"عضو متقيد")
  elif rank == "left":
    await.send_message(chat_id,"انتا مغادر يعم")
  elif rank == "kicked":
    await.send_message(chat_id,"الراجل ده واخد بالجزمه ومحظور")
