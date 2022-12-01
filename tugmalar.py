from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


kunlik = InlineKeyboardButton(text="1 kunlik", callback_data="kunlik")
kunlik3 = InlineKeyboardButton(text="3 kunlik", callback_data="kunlik3")
kunlik10 = InlineKeyboardButton(text="10 kunlik", callback_data="kunlik10")
oylik = InlineKeyboardButton(text="1 oylik", callback_data="oylik")


natija1 = InlineKeyboardMarkup().add(kunlik,kunlik3, kunlik10, oylik)

andi = KeyboardButton(text="Andijan")
bux = KeyboardButton(text="Bukhara")
far = KeyboardButton(text="Ferghana")
jiz = KeyboardButton(text="Jizzakh")
xor = KeyboardButton(text="Khiva")
nam = KeyboardButton(text="Namangan")
qash = KeyboardButton(text="Karshi")
nuk = KeyboardButton(text="Nukus")
sam = KeyboardButton(text="Samarkand")
sir = KeyboardButton(text="Gulistan")
sur = KeyboardButton(text="Termez")
tosh = KeyboardButton(text="Tashkent")

natija = ReplyKeyboardMarkup(resize_keyboard=True).add(andi,bux,far,jiz,xor,nam,qash,nuk,sam,sir,sur,tosh)

