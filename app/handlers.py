from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
import app.keyboards as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Assalomu alaykum!\nYour ID: {message.from_user.id}\nYour name: {message.from_user.full_name}", reply_markup= kb.main)


@router.message(Command("help"))
async def help(message: Message):
    await message.answer('Айшат дура!')

@router.message(F.text == 'How are you?')
async def how_are_you(message: Message):
    await message.answer('I am fine!')

@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer('You choose catalog')
    await callback.message.edit_text("Каталог", reply_markup= await kb.inline_cars())


@router.message(Command("reg"))
async def reg_first(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Enter your name")

@router.message(Reg.name)
async def reg_second(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Reg.number)
    await message.answer("Enter your number")


@router.message(Reg.number)
async def reg_third(message: Message, state: FSMContext):
    await state.update_data(number = message.text)
    data = await state.get_data()
    await message.answer(f'finished registration\n name: f{data['name']}\n number: {data["number"]}')
    await state.clear()

# @router.message(F.photo)
# async def photo(message: Message):
#     await message.answer(f"{photo[-1].file_id}")