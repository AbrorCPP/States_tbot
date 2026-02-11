from aiogram import types
from aiogram.fsm.context import FSMContext
from utils import banlist
from router import router
from states.registration import UserRegistrationForm
from keyboards.reply.confirm_info_keyboard import generate_user_info_confirmation_keyboard

@router.message(UserRegistrationForm.fullname)
async def save_fullname(message: types.Message, state: FSMContext):
    if message.text.lower() in banlist.Banned_names:
        print(message.text.lower())
        await message.answer("Siz oq qilindingiz😂😂😂")
    else:
        await state.update_data(fullname=message.text.capitalize())
        await message.answer("Ismingiz qabul qilindi ✅")
        await state.set_state(UserRegistrationForm.age)
        await message.answer("Yoshingizni kiriting: ")

@router.message(UserRegistrationForm.age)
async def save_age(message: types.Message, state: FSMContext):
    age = message.text

    if age.isdigit() and int(age) > 60:
        await message.answer("Rostdan shuncha yoshdamisiz🫨🫨🫨")
    elif age.isdigit() and int(age)>0:
        await state.update_data(age= int(message.text.strip()))
        await message.answer("Yoshingiz qabul qilindi ✅")
        await state.set_state(UserRegistrationForm.address)
        await message.answer("Manzilingizni kiriting 3 ta qism \nShahar,MFY,Ko'cha va manzil shu ko'rinishda \n(,) bilan ajratib: ")
    else:
        await message.answer("Yosh xato kiritildi")

@router.message(UserRegistrationForm.address)
async def save_address(message: types.Message, state: FSMContext):
    address = message.text
    solo = address.split(",")
    if len(solo)==3:
        await state.update_data(address = message.text.strip())
        await message.answer("Manzil qabul qilindi✅")

        collect_data = await state.get_data()  # {"fullname": "asdwdawdawd"}

        full_info  = "\n ----- Sizni ma'lumotlaringiz -----"
        full_info += f"\n\n FISH = {collect_data.get('fullname')}"
        full_info += f"\n YOSH = {collect_data.get('age')}"
        full_info += f"\n MANZIL = {collect_data.get('address')}"
        full_info += f"\n\n Ma'lumotlar to'g'ri kiritildimi ? ✨"

        await message.answer(full_info, reply_markup=generate_user_info_confirmation_keyboard())
        await state.set_state(UserRegistrationForm.confirmation)
        #29

    else:
        await message.answer("Joylashuv xato kiritildi🤦‍♂️🤦‍♂️🤦‍♂️")


@router.message(UserRegistrationForm.confirmation)
async def save_confirm(message: types.Message, state: FSMContext):
    answer = message.text.lower()

    if answer not in ["ha",'yo\'q']:
        await message.answer("""Javob faqat "Ha" yoki "yo\'q" da kiriting""")
    elif answer == "ha":
        await message.answer("Muvaffaqiyatli ro'yxatdan o'tdingiz!")
        await state.clear()
    else:
        await state.set_state(UserRegistrationForm.fullname)