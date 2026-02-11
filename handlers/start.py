from aiogram import types
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from router import router
from states.registration import UserRegistrationForm

@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await message.answer("Assalomu alaykum !")

    await state.set_state(UserRegistrationForm.fullname)
    await message.answer("Ismingizni kiriting: ")
