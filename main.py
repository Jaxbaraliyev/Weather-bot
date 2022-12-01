from bs4 import BeautifulSoup
import requests
import logging
from aiogram import Bot, Dispatcher, executor, types
from tugmalar import natija
logging.basicConfig(level=logging.INFO)


API_TOKEN = "#"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    ism = message.from_user.full_name
    await message.answer(f"Assalomu alaykum <i>{ism}</i>.Ob-havo🌥 botimizga xush kelibsiz!\n "
                         f"Bugungi, ob-havo ma`lumotini bilish uchun o`z shaxringizni kiriting:👇", parse_mode="HTML", reply_markup=natija)


@dp.message_handler(commands=['admin'])
async def admin(message:types.Message):
    await message.answer("Bot admini: @Ramziddin_17_17")

@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.answer("Bu bot sizga faqatgina O`zbekistondagi🇺🇿 1 kunlik ob-havo ma`lumotini chiqarib beradi!")


@dp.message_handler()
async def andi(message:types.Message):
    try:
        if message.text == "Andijan":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                             f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                             f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                             f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Bukhara":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                             f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                             f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                             f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Ferghana":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                         f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                         f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                         f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Jizzakh":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                                 f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                                 f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                                 f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Khiva":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                                 f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                                 f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                                 f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Namangan":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                                 f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                                 f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                                 f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Karshi":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                                 f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                                 f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                                 f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Nukus":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                                 f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                                 f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                                 f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Samarkand":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                                 f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                                 f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                                 f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")
        elif message.text == "Gulistan":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                                 f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                                 f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                                 f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Termez":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                                 f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                                 f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                                 f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

        elif message.text == "Tashkent":
            kunlik = f"https://obhavo.uz/{message.text.lower()}"
            agent = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(kunlik, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            max = part.findAll("strong")
            min = part.findAll("span", {"class": "forecast-night"})
            yogin = part.findAll("td", {"class": "weather-row-desc", "class": "weather-row-pop"})
            tavsif = part.findAll("td", {"class": "weather-row-desc"})
            await message.answer(f"<b>{message.text}</b> dagi bugungi havo⛅ harorati:\n"
                                 f"Minimum {min[0].text}C ga teng\n Maximum {max[0].text} ga teng bo`ladi\n"
                                 f"Yog`ingarchilik🌧:  {yogin[0].text.strip()}\n"
                                 f"Tavsifi: {tavsif[0].text.strip()}", parse_mode="HTML")

    except:
        await message.answer("Afsuski bunday shahar topilmadi")


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)