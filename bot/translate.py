from telegram import InlineKeyboardButton
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, InlineQueryHandler, ConversationHandler, CallbackQueryHandler
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from lot_kir import translate
import time
from datetime import date
from backend import Analiz
from random import randint

'''
Muhammadbobur

'''
data = Analiz()

translit = translate()

STATE_TRANSLATE = 0
STATE_TWO = 1


def delete_message(qu,context:CallbackContext):
    for i in range(3):
        try:
            context.bot.delete_message(chat_id=qu.message.chat_id, message_id=qu.message.message_id - i)
        except:
            pass

button= [[InlineKeyboardButton("♻️ Кириллча", callback_data='1'), InlineKeyboardButton("♻️ Lotincha", callback_data='2')]]


txt = "❇️AgroZamin'da nimalarni topish mumkin?\n\nAgroZamin - turli toifadagi qishloq xo‘jaligi mahsulotlarini topish va xarid qilish mumkin bo‘lgan qulay onlayn-platforma." \
    "\n\nMahsulotlarni hoziroq joylashtirish mumkin bo‘lgan bo‘limlar:\n" \
    "-  Agrokimyo\n" \
    "-  Veterinariya\n" \
    "-  Agrotexnika va uskunalar uchun butlovchi qismlar\n" \
    "-  Gʻalla, urug‘ va ozuqalar\n" \
    "-  Bog‘ va tomorqa mahsulotlari\n" \
    "-  Qishloq xo‘jaligi texnikasi\n" \
    "-  Chorva hayvonlari va parrandalar\n" \
    "-  Maxsus kiyimlar va maxsus texnika\n" \
    "-  О‘g‘itlar\n" \
    "-  Va boshqa ko‘plab mahsulotlar\n"


def start(update:Update, context:CallbackContext):
    #update.message.reply_html(f"🤖 Assalomu alaykum <b>{update.effective_user.first_name}</b>!\n\n♻️ Bot lotin matnni krilga o'girib beradi.\n✍🏻 Biror text kiriting...")
    id = update.effective_user.id
    user = update.effective_user
    #print(update)
    # try:
    #     context.bot.send_sticker(chat_id=update.message.chat_id,sticker='CAACAgIAAxkBAAIOkGL5wt8bO_ia5wABYiHpeSQAAVrCrzoAAqEYAAKVsYFI5u7kOTJpH94pBA')
    # except: pass
    sentens = 'lotin to kirill bot..'  # \n\nMening ismim Muhammadbobur sizga qanday \nyordam bera olaman.'
    ss = ''
    for i, j in enumerate(sentens):
        if ss:
            time.sleep(0.02)
            context.bot.edit_message_text(chat_id=update.message.chat_id, message_id=update.message.message_id + 1,
                                          text=f'🤖 <b>{ss}</b>|', parse_mode='HTML')
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text=f'🤖 {j}|')
            ss = j
        try:
            ss = ss + str(sentens[int(i) + 1])
        except:
            pass

    if data.chack_user(chat_id=update.message.chat_id) == 0:
        data.users_insert(chat_id=update.message.chat_id, username=update.effective_user.link)
    else:
        pass
    context.bot.send_message(chat_id=update.message.chat_id, text=f"🤖 <b>{update.effective_user.first_name}</b>!\n\n♻️ Bot lotin matnni krilga o'girib beradi.\n✍🏻 Biror text kiriting...", parse_mode='HTML')

    return STATE_TRANSLATE
def translate_text(text):
    l, k = 0, 0
    for i in text:
        if i in translit.lotin:
            l = l + 1
        elif i in translit.kril:
            k = k + 1
    if l > k:
        t = translit.lotin_to_kril(text=text)
    elif k > l:
        t = translit.kril_to_lotin(text=text)
    else:
        t = translit.lotin_to_kril(text=text)
    return t





def translat(update:Update, context:CallbackContext):
    text = update.message.text
    context.chat_data.update({'txt': txt})
    if text == 'change':
        context.bot.send_photo(update.message.chat_id, photo=open("photo.jpg", "rb"), caption=txt,reply_markup=InlineKeyboardMarkup(button))
        return STATE_TWO

    try:
        try:
            context.chat_data.update({'video_text': update.message['caption']})
            context.chat_data.update({'video': update.message['video']['file_id']})
            context.bot.send_video(chat_id=update.message.chat_id, video=update.message['video']['file_id'],caption=translate_text(text=update.message['caption']), reply_markup=InlineKeyboardMarkup(button))

            return STATE_TWO

        except:
            context.chat_data.update({'text': update.message['caption']})
            context.chat_data.update({'photo': update.message['photo'][0]['file_id']})
            #context.bot.send_photo(update.message.chat_id, photo=update.message['photo'][0]['file_id'], caption=translate_text(text=update.message['caption']))
            context.bot.send_photo(chat_id=update.message.chat_id, photo=update.message['photo'][0]['file_id'],caption=translate_text(text=update.message['caption']), reply_markup=InlineKeyboardMarkup(button))
            return STATE_TWO
    except:
        text = update.message.text
        update.message.reply_text(f"{translate_text(text=text)}")

def change(update:Update, context:CallbackContext):
    query = update.callback_query

    if query.data == '1':

        try:
            delete_message(qu=query, context=context)
            context.bot.send_photo(chat_id=query.message.chat_id,
                                   photo=context.chat_data['photo'],
                                   caption=translate_text(text=context.chat_data['text']),
                                   reply_markup=InlineKeyboardMarkup(button))
        except:
            pass
        try:
            context.bot.send_video(chat_id=query.message.chat_id, video=context.chat_data['video'], caption=translate_text(text=query.message['caption']), reply_markup=InlineKeyboardMarkup(button))
        except:
            pass

    else:
        try:
            delete_message(qu=query, context=context)
            context.bot.send_photo(chat_id=query.message.chat_id,
                                   photo=context.chat_data['photo'],
                                   caption=context.chat_data['text'],
                                   reply_markup=InlineKeyboardMarkup(button))
        except:
            pass
        try:
            context.bot.send_video(chat_id=query.message.chat_id, video=context.chat_data['video'], caption=query.message['caption'], reply_markup=InlineKeyboardMarkup(button))
        except:
            pass
def stop(update:Update, context:CallbackContext):
    update.message.reply_html("Hayr !")

def info(update:Update, context:CallbackContext):
    context.bot.send_photo(chat_id = update.effective_message.chat_id,
                           photo = open('diogramma.jpg','rb'),
                           caption =  f"Barcha foydalanuvchilar soni: <b>{data.count_users()}</b>\n"
                                      f"Bot ishga tushganiga <b>{(date.today() - date(2022, 9, 1)).days}</b> kun bo'ldi",
                           parse_mode="HTML")

def owner(update:Update, context:CallbackContext):
    phone_number = '+998909968395'
    first_name = 'Muhammadbobur'
    last_name = 'Umirov'
    context.bot.send_contact(chat_id=update.message.chat_id, phone_number=phone_number,
                               first_name=first_name, last_name=last_name)



updater = Updater('5794102410:AAFfM6IBWUbaMs0UyFXHcnyPPbxOQKEZ2Eo', use_context=True)
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('admin', owner))

conv_handler = ConversationHandler(
    entry_points=[
        #CommandHandler('start', start),
        MessageHandler(Filters.all, start)
    ],
    states = {
        STATE_TRANSLATE: [
            MessageHandler(Filters.all, translat)
        ],
        STATE_TWO: [
            CallbackQueryHandler(change),
            MessageHandler(Filters.all, translat)
        ]
    },
    fallbacks= [CommandHandler('stop', stop)]
)
updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()