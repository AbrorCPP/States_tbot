from aiogram import types
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext

from router import router

class UserRegistrationForm(StatesGroup):
    fullname = State()
    age = State()
    address = State()

@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await message.answer("Assalomu alaykum !")

    await state.set_state(UserRegistrationForm.fullname)
    await message.answer("Ismingizni kiriting: ")

@router.message(UserRegistrationForm.fullname)
async def save_fullname(message: types.Message, state: FSMContext):
    await message.answer("Ismingiz qabul qilindi ✅")

    await state.set_state(UserRegistrationForm.age)
    await message.answer("Yoshingizni kiriting: ")

@router.message(UserRegistrationForm.age)
async def save_age(message: types.Message, state: FSMContext):
    age = message.text

    if age.isdigit() and int(age)>0:
        await message.answer("Yoshingiz qabul qilindi ✅")

        await state.set_state(UserRegistrationForm.address)
        await message.answer("Manzilingizni kiriting 3 ta qism \nShahar,MFY,Ko'cha va manzil shu ko'rinishda \n(,) bilan ajratib: ")
    elif age.isdigit() and int(age)>60:
        await message.answer("Rostdan shuncha yoshdamisiz🫨🫨🫨")
    else:
        await message.answer("Yosh xato kiritildi")

@router.message(UserRegistrationForm.address)
async def save_address(message: types.Message, state: FSMContext):
    address = message.text
    solo = address.split(",")
    if len(solo)==3:
        await message.answer("Manzil qabul qilindi✅")
        await state.clear()
    else:
        await message.answer("Joylashuv xato kiritildi🤦‍♂️🤦‍♂️🤦‍♂️")